import json
from datetime import date, datetime
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from .models import CrmContacto, CrmColaWhatsapp


def get_cola_stats():
    """Calcula las métricas y el estado actual del banner para WhatsApp."""
    today = date.today()
    try:
        total_pendientes = CrmColaWhatsapp.objects.filter(estado='pendiente').count()
        total_procesando = CrmColaWhatsapp.objects.filter(estado='procesando').count()
        total_enviados = CrmColaWhatsapp.objects.filter(estado='enviado').count()
        total_enviados_hoy = CrmColaWhatsapp.objects.filter(estado='enviado', fecha_programada=today).count()
        total_errores = CrmColaWhatsapp.objects.filter(estado='error').count()

        if total_procesando > 0:
            banner_tipo = 'procesando'
            banner_icono = '🔵'
            banner_mensaje = f"El bot está enviando mensajes actualmente... (Quedan {total_pendientes + total_procesando})"
        elif total_pendientes > 0:
            banner_tipo = 'pendiente'
            banner_icono = '🟡'
            banner_mensaje = f"Hay {total_pendientes} mensaje(s) en cola listos para el envío nocturno."
        else:
            banner_tipo = 'exito'
            banner_icono = '🟢'
            banner_mensaje = "Todos los mensajes del día han sido enviados con éxito."

        return {
            'total_pendientes': total_pendientes,
            'total_procesando': total_procesando,
            'total_enviados': total_enviados,
            'total_enviados_hoy': total_enviados_hoy,
            'total_errores': total_errores,
            'banner_tipo': banner_tipo,
            'banner_icono': banner_icono,
            'banner_mensaje': banner_mensaje,
        }
    except Exception as e:
        return {
            'total_pendientes': 0,
            'total_procesando': 0,
            'total_enviados': 0,
            'total_enviados_hoy': 0,
            'total_errores': 0,
            'banner_tipo': 'error',
            'banner_icono': '🔴',
            'banner_mensaje': f"Error al consultar el estado de la cola: {str(e)}",
        }


def dashboard(request):
    """Vista principal del CRM de WhatsApp."""
    stats = get_cola_stats()
    
    # Obtener contactos activos
    try:
        contactos = list(CrmContacto.objects.filter(activo=True).order_by('tipo', 'nombre'))
    except Exception:
        contactos = []

    # Conteo por rubros
    rubros_counts = {
        'todos': len(contactos),
        'paciente': sum(1 for c in contactos if c.tipo == 'paciente'),
        'doctor': sum(1 for c in contactos if c.tipo == 'doctor'),
        'cliente': sum(1 for c in contactos if c.tipo == 'cliente'),
        'otro': sum(1 for c in contactos if c.tipo == 'otro'),
    }

    # Cola reciente (últimos 50 mensajes)
    try:
        cola_reciente = list(CrmColaWhatsapp.objects.all().order_by('-id')[:50])
    except Exception:
        cola_reciente = []

    today_str = date.today().isoformat()

    context = {
        'stats': stats,
        'contactos': contactos,
        'rubros_counts': rubros_counts,
        'cola_reciente': cola_reciente,
        'today_str': today_str,
    }
    return render(request, 'crm/dashboard.html', context)


@require_POST
def api_encolar_mensajes(request):
    """Encola mensajes en crm_cola_whatsapp reemplazando variables dinámicas."""
    try:
        try:
            data = json.loads(request.body.decode('utf-8'))
        except Exception:
            data = request.POST

        contactos_ids = data.get('contactos_ids', [])
        mensaje_template = data.get('mensaje', '').strip()
        fecha_programada_str = data.get('fecha_programada', '').strip()
        hora_cita = data.get('hora_cita', '').strip()

        if not mensaje_template:
            return JsonResponse({'ok': False, 'error': 'El mensaje no puede estar vacío.'}, status=400)

        if not contactos_ids:
            return JsonResponse({'ok': False, 'error': 'Debes seleccionar al menos un contacto.'}, status=400)

        if fecha_programada_str:
            try:
                fecha_programada = datetime.strptime(fecha_programada_str, '%Y-%m-%d').date()
            except ValueError:
                fecha_programada = date.today()
        else:
            fecha_programada = date.today()

        # Buscar contactos seleccionados
        contactos = CrmContacto.objects.filter(id__in=contactos_ids, activo=True)
        if not contactos.exists():
            return JsonResponse({'ok': False, 'error': 'No se encontraron contactos activos válidos seleccionados.'}, status=400)

        nuevos_mensajes = []
        for c in contactos:
            # Reemplazar variables dinámicas
            nombre_val = c.nombre.strip() if c.nombre else ''
            apellidos_val = c.apellidos.strip() if c.apellidos else ''
            nombre_completo_val = f"{nombre_val} {apellidos_val}".strip()
            telefono_val = c.telefono.strip() if c.telefono else ''
            fecha_val = fecha_programada.strftime('%d/%m/%Y')
            hora_val = hora_cita if hora_cita else ''

            msg = mensaje_template
            msg = msg.replace('{nombre}', nombre_val)
            msg = msg.replace('{apellidos}', apellidos_val)
            msg = msg.replace('{nombre_completo}', nombre_completo_val)
            msg = msg.replace('{telefono}', telefono_val)
            msg = msg.replace('{fecha}', fecha_val)
            msg = msg.replace('{hora}', hora_val)

            # Instanciar registro
            nuevo = CrmColaWhatsapp(
                telefono=telefono_val,
                nombre_contacto=nombre_completo_val or nombre_val,
                mensaje=msg,
                estado='pendiente',
                fecha_programada=fecha_programada,
                intentos=0,
                error_detalle=None
            )
            nuevos_mensajes.append(nuevo)

        # Inserción masiva en base de datos 'servicios'
        CrmColaWhatsapp.objects.bulk_create(nuevos_mensajes)

        stats = get_cola_stats()
        return JsonResponse({
            'ok': True,
            'creados': len(nuevos_mensajes),
            'stats': stats,
            'mensaje': f'Se encolaron {len(nuevos_mensajes)} mensaje(s) exitosamente para el {fecha_programada.strftime("%d/%m/%Y")}.'
        })

    except Exception as e:
        return JsonResponse({'ok': False, 'error': f'Error en el servidor: {str(e)}'}, status=500)


@require_GET
def api_estado_cola(request):
    """Retorna el estado en tiempo real de la cola y estadísticas."""
    stats = get_cola_stats()
    
    estado_filtro = request.GET.get('estado', '')
    query = CrmColaWhatsapp.objects.all()
    if estado_filtro and estado_filtro in ['pendiente', 'procesando', 'enviado', 'error']:
        query = query.filter(estado=estado_filtro)

    recientes = list(query.order_by('-id')[:50])
    items = []
    for r in recientes:
        items.append({
            'id': r.id,
            'telefono': r.telefono,
            'nombre_contacto': r.nombre_contacto or 'Sin nombre',
            'mensaje': r.mensaje,
            'estado': r.estado,
            'fecha_programada': r.fecha_programada.strftime('%Y-%m-%d') if r.fecha_programada else '',
            'intentos': r.intentos,
            'error_detalle': r.error_detalle,
            'creado_en': r.creado_en.strftime('%d/%m/%Y %H:%M') if r.creado_en else '',
            'enviado_en': r.enviado_en.strftime('%d/%m/%Y %H:%M') if r.enviado_en else '',
        })

    return JsonResponse({
        'ok': True,
        'stats': stats,
        'items': items
    })


@require_POST
def api_agregar_contacto(request):
    """Agrega un nuevo contacto a crm_contactos en 'servicios'."""
    try:
        try:
            data = json.loads(request.body.decode('utf-8'))
        except Exception:
            data = request.POST

        nombre = data.get('nombre', '').strip()
        apellidos = data.get('apellidos', '').strip()
        telefono = data.get('telefono', '').strip()
        tipo = data.get('tipo', 'paciente').strip().lower()
        notas = data.get('notas', '').strip()

        if not nombre or not telefono:
            return JsonResponse({'ok': False, 'error': 'Nombre y teléfono son obligatorios.'}, status=400)

        # Sanitizar teléfono (remover espacios, guiones)
        telefono = ''.join(c for c in telefono if c.isdigit())
        if len(telefono) < 10:
            return JsonResponse({'ok': False, 'error': 'El teléfono debe contener al menos 10 dígitos.'}, status=400)

        contacto = CrmContacto.objects.create(
            nombre=nombre,
            apellidos=apellidos or None,
            telefono=telefono,
            tipo=tipo if tipo in ['paciente', 'doctor', 'cliente', 'otro'] else 'paciente',
            activo=True,
            notas=notas or None
        )

        return JsonResponse({
            'ok': True,
            'contacto': {
                'id': contacto.id,
                'nombre': contacto.nombre,
                'apellidos': contacto.apellidos or '',
                'nombre_completo': contacto.nombre_completo,
                'telefono': contacto.telefono,
                'tipo': contacto.tipo,
                'notas': contacto.notas or '',
            },
            'mensaje': 'Contacto registrado correctamente.'
        })
    except Exception as e:
        return JsonResponse({'ok': False, 'error': f'Error al guardar contacto: {str(e)}'}, status=500)


@require_POST
def api_cancelar_mensaje(request, mensaje_id):
    """Cancela/elimina un mensaje en cola si está pendiente."""
    try:
        mensaje = get_object_or_404(CrmColaWhatsapp, id=mensaje_id)
        if mensaje.estado != 'pendiente':
            return JsonResponse({'ok': False, 'error': f'No se puede cancelar un mensaje con estado "{mensaje.estado}".'}, status=400)
        
        mensaje.delete()
        stats = get_cola_stats()
        return JsonResponse({'ok': True, 'stats': stats, 'mensaje': 'Mensaje eliminado de la cola.'})
    except Exception as e:
        return JsonResponse({'ok': False, 'error': str(e)}, status=500)


@require_POST
def api_reintentar_mensaje(request, mensaje_id):
    """Reintenta un mensaje que falló poniéndolo en pendiente e intentos=0."""
    try:
        mensaje = get_object_or_404(CrmColaWhatsapp, id=mensaje_id)
        mensaje.estado = 'pendiente'
        mensaje.intentos = 0
        mensaje.error_detalle = None
        mensaje.save()
        stats = get_cola_stats()
        return JsonResponse({'ok': True, 'stats': stats, 'mensaje': 'Mensaje restablecido a pendiente para reintento.'})
    except Exception as e:
        return JsonResponse({'ok': False, 'error': str(e)}, status=500)
