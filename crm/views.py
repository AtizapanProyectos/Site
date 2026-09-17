import json
from datetime import date, datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from .models import CrmContacto, CrmColaWhatsapp


def get_cola_stats(usuario=None):
    """Calcula las métricas y el estado actual del banner para WhatsApp, filtrando por usuario si aplica."""
    today = date.today()
    try:
        qs = CrmColaWhatsapp.objects.all()
        if usuario:
            qs = qs.filter(usuario=usuario)

        total_pendientes = qs.filter(estado='pendiente').count()
        total_procesando = qs.filter(estado='procesando').count()
        total_enviados = qs.filter(estado='enviado').count()
        total_enviados_hoy = qs.filter(estado='enviado', fecha_programada=today).count()
        total_errores = qs.filter(estado='error').count()

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
            banner_mensaje = "Todos los mensajes programados están al día."

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


# =====================================================================
# Vistas de Autenticación
# =====================================================================

def login_view(request):
    """Pantalla de login minimalista para el CRM."""
    if request.user.is_authenticated:
        return redirect('/crm/')

    error_msg = None
    next_url = request.POST.get('next') or request.GET.get('next') or '/crm/'

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            error_msg = 'Por favor ingresa usuario y contraseña.'
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(next_url)
            else:
                error_msg = 'Usuario o contraseña incorrectos.'

    return render(request, 'crm/login.html', {
        'error_msg': error_msg,
        'next': next_url
    })


def logout_view(request):
    """Cierra la sesión y redirige a la pantalla de login."""
    logout(request)
    return redirect('/crm/login/')


# =====================================================================
# Dashboard Principal
# =====================================================================

@login_required
def dashboard(request):
    """Vista principal del CRM con aislamiento por usuario / asesor."""
    current_user = request.user
    is_admin = current_user.is_superuser or current_user.username == 'admin'

    # Lista de usuarios disponibles para el selector de admin
    usuarios_list = []
    if is_admin:
        try:
            usuarios_list = list(User.objects.all().values_list('username', flat=True).order_by('username'))
        except Exception:
            usuarios_list = ['admin', 'lidia']

    # Filtro opcional de usuario si es admin
    usuario_param = request.GET.get('usuario', '')
    if is_admin:
        usuario_activo = usuario_param if usuario_param and usuario_param != 'todos' else None
    else:
        usuario_activo = current_user.username

    # Métricas de la cola
    stats = get_cola_stats(usuario=usuario_activo)
    
    # Obtener contactos según permisos
    try:
        if usuario_activo:
            contactos = list(CrmContacto.objects.filter(activo=True, usuario=usuario_activo).order_by('organizacion', 'nombre'))
        else:
            contactos = list(CrmContacto.objects.filter(activo=True).order_by('organizacion', 'nombre'))
    except Exception:
        contactos = []

    # Extraer organizaciones únicas y conteo por organización
    organizaciones_map = {}
    sin_org_count = 0
    for c in contactos:
        org = (c.organizacion or '').strip()
        if org:
            organizaciones_map[org] = organizaciones_map.get(org, 0) + 1
        else:
            sin_org_count += 1

    organizaciones_list = sorted(organizaciones_map.keys())

    # Cola reciente
    try:
        if usuario_activo:
            cola_reciente = list(CrmColaWhatsapp.objects.filter(usuario=usuario_activo).order_by('-id')[:50])
        else:
            cola_reciente = list(CrmColaWhatsapp.objects.all().order_by('-id')[:50])
    except Exception:
        cola_reciente = []

    today_str = date.today().isoformat()

    context = {
        'stats': stats,
        'contactos': contactos,
        'organizaciones': organizaciones_list,
        'organizaciones_map': organizaciones_map,
        'sin_org_count': sin_org_count,
        'total_contactos': len(contactos),
        'cola_reciente': cola_reciente,
        'today_str': today_str,
        'current_user': current_user,
        'is_admin': is_admin,
        'usuarios_list': usuarios_list,
        'usuario_activo': usuario_activo or 'todos',
    }
    return render(request, 'crm/dashboard.html', context)


# =====================================================================
# APIs de Dashboard
# =====================================================================

@csrf_exempt
@require_POST
def api_encolar_mensajes(request):
    """Encola mensajes en crm_cola_whatsapp asociándolos al usuario correspondiente."""
    if not request.user.is_authenticated:
        return JsonResponse({'ok': False, 'error': 'No has iniciado sesión.'}, status=401)

    try:
        try:
            data = json.loads(request.body.decode('utf-8'))
        except Exception:
            data = request.POST

        contactos_ids = data.get('contactos_ids', [])
        mensaje_template = data.get('mensaje', '').strip()
        fecha_programada_str = data.get('fecha_programada', '').strip()
        hora_cita = data.get('hora_cita', '').strip()
        poliza = data.get('poliza', '').strip()

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

        current_username = request.user.username
        is_admin = request.user.is_superuser or current_username == 'admin'

        # Buscar contactos seleccionados respetando el aislamiento de usuario
        if is_admin:
            contactos = CrmContacto.objects.filter(id__in=contactos_ids, activo=True)
        else:
            contactos = CrmContacto.objects.filter(id__in=contactos_ids, activo=True, usuario=current_username)

        if not contactos.exists():
            return JsonResponse({'ok': False, 'error': 'No se encontraron contactos activos disponibles.'}, status=400)

        nuevos_mensajes = []
        for c in contactos:
            # Reemplazar variables dinámicas
            nombre_val = c.nombre.strip() if c.nombre else ''
            apellidos_val = c.apellidos.strip() if c.apellidos else ''
            nombre_completo_val = f"{nombre_val} {apellidos_val}".strip()
            org_val = (c.organizacion or '').strip()
            telefono_val = c.telefono.strip() if c.telefono else ''
            fecha_val = fecha_programada.strftime('%d/%m/%Y')
            hora_val = hora_cita if hora_cita else ''

            msg = mensaje_template
            msg = msg.replace('{nombre}', nombre_val)
            msg = msg.replace('{apellidos}', apellidos_val)
            msg = msg.replace('{nombre_completo}', nombre_completo_val)
            msg = msg.replace('{organizacion}', org_val or 'su organización')
            msg = msg.replace('{empresa}', org_val or 'su empresa')
            msg = msg.replace('{poliza}', poliza or 'su póliza')
            msg = msg.replace('{telefono}', telefono_val)
            msg = msg.replace('{fecha}', fecha_val)
            msg = msg.replace('{hora}', hora_val)

            nuevo = CrmColaWhatsapp(
                telefono=telefono_val,
                nombre_contacto=nombre_completo_val or nombre_val,
                mensaje=msg,
                usuario=c.usuario or current_username,
                estado='pendiente',
                fecha_programada=fecha_programada,
                intentos=0,
                error_detalle=None
            )
            nuevos_mensajes.append(nuevo)

        # Inserción masiva en base de datos 'servicios'
        CrmColaWhatsapp.objects.bulk_create(nuevos_mensajes)

        stats = get_cola_stats(usuario=None if is_admin else current_username)
        return JsonResponse({
            'ok': True,
            'creados': len(nuevos_mensajes),
            'stats': stats,
            'mensaje': f'Se guardaron {len(nuevos_mensajes)} mensaje(s) en cola exitosamente para el {fecha_programada.strftime("%d/%m/%Y")}.'
        })

    except Exception as e:
        return JsonResponse({'ok': False, 'error': f'Error en el servidor: {str(e)}'}, status=500)


@require_GET
def api_estado_cola(request):
    """Retorna el estado en tiempo real de la cola y estadísticas respetando el usuario."""
    if not request.user.is_authenticated:
        return JsonResponse({'ok': False, 'error': 'No has iniciado sesión.'}, status=401)

    current_username = request.user.username
    is_admin = request.user.is_superuser or current_username == 'admin'

    usuario_param = request.GET.get('usuario', '')
    if is_admin:
        usuario_filtro = usuario_param if usuario_param and usuario_param != 'todos' else None
    else:
        usuario_filtro = current_username

    stats = get_cola_stats(usuario=usuario_filtro)
    
    estado_filtro = request.GET.get('estado', '')
    query = CrmColaWhatsapp.objects.all()
    if usuario_filtro:
        query = query.filter(usuario=usuario_filtro)

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
            'usuario': r.usuario,
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


@csrf_exempt
@require_POST
def api_agregar_contacto(request):
    """Agrega un nuevo contacto a crm_contactos asignado al usuario activo."""
    if not request.user.is_authenticated:
        return JsonResponse({'ok': False, 'error': 'No has iniciado sesión.'}, status=401)

    try:
        try:
            data = json.loads(request.body.decode('utf-8'))
        except Exception:
            data = request.POST

        nombre = data.get('nombre', '').strip()
        apellidos = data.get('apellidos', '').strip()
        organizacion = data.get('organizacion', '').strip()
        telefono = data.get('telefono', '').strip()
        tipo = data.get('tipo', 'cliente').strip().lower()
        notas = data.get('notas', '').strip()

        if not nombre or not telefono:
            return JsonResponse({'ok': False, 'error': 'Nombre y teléfono son obligatorios.'}, status=400)

        # Sanitizar teléfono
        telefono = ''.join(c for c in telefono if c.isdigit())
        if len(telefono) < 10:
            return JsonResponse({'ok': False, 'error': 'El teléfono debe contener al menos 10 dígitos.'}, status=400)

        current_username = request.user.username
        is_admin = request.user.is_superuser or current_username == 'admin'

        # Asignar usuario: si es admin y viene en data, usarlo; de lo contrario el usuario autenticado
        usuario_asignado = (data.get('usuario') or '').strip().lower() if is_admin else current_username
        if not usuario_asignado:
            usuario_asignado = current_username

        contacto = CrmContacto.objects.create(
            nombre=nombre,
            apellidos=apellidos or None,
            organizacion=organizacion or None,
            telefono=telefono,
            tipo=tipo or 'cliente',
            usuario=usuario_asignado,
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
                'organizacion': contacto.organizacion or '',
                'telefono': contacto.telefono,
                'usuario': contacto.usuario,
                'tipo': contacto.tipo,
                'notas': contacto.notas or '',
            },
            'mensaje': f'Contacto registrado correctamente para "{contacto.usuario}".'
        })
    except Exception as e:
        return JsonResponse({'ok': False, 'error': f'Error al guardar contacto: {str(e)}'}, status=500)


@csrf_exempt
@require_POST
def api_cancelar_mensaje(request, mensaje_id):
    """Cancela/elimina un mensaje en cola si está pendiente y pertenece al usuario."""
    if not request.user.is_authenticated:
        return JsonResponse({'ok': False, 'error': 'No autenticado.'}, status=401)

    try:
        current_username = request.user.username
        is_admin = request.user.is_superuser or current_username == 'admin'

        mensaje = get_object_or_404(CrmColaWhatsapp, id=mensaje_id)
        if not is_admin and mensaje.usuario != current_username:
            return JsonResponse({'ok': False, 'error': 'No tienes permiso para cancelar este mensaje.'}, status=403)

        if mensaje.estado != 'pendiente':
            return JsonResponse({'ok': False, 'error': f'No se puede cancelar un mensaje con estado "{mensaje.estado}".'}, status=400)
        
        mensaje.delete()
        stats = get_cola_stats(usuario=None if is_admin else current_username)
        return JsonResponse({'ok': True, 'stats': stats, 'mensaje': 'Mensaje eliminado de la cola.'})
    except Exception as e:
        return JsonResponse({'ok': False, 'error': str(e)}, status=500)


@csrf_exempt
@require_POST
def api_reintentar_mensaje(request, mensaje_id):
    """Reintenta un mensaje fallido."""
    if not request.user.is_authenticated:
        return JsonResponse({'ok': False, 'error': 'No autenticado.'}, status=401)

    try:
        current_username = request.user.username
        is_admin = request.user.is_superuser or current_username == 'admin'

        mensaje = get_object_or_404(CrmColaWhatsapp, id=mensaje_id)
        if not is_admin and mensaje.usuario != current_username:
            return JsonResponse({'ok': False, 'error': 'No tienes permiso para reintentar este mensaje.'}, status=403)

        mensaje.estado = 'pendiente'
        mensaje.intentos = 0
        mensaje.error_detalle = None
        mensaje.save()
        stats = get_cola_stats(usuario=None if is_admin else current_username)
        return JsonResponse({'ok': True, 'stats': stats, 'mensaje': 'Mensaje restablecido a pendiente para reintento.'})
    except Exception as e:
        return JsonResponse({'ok': False, 'error': str(e)}, status=500)


@csrf_exempt
@require_POST
def api_crear_usuario(request):
    """Permite al admin registrar nuevos usuarios/asesores directamente."""
    if not request.user.is_authenticated:
        return JsonResponse({'ok': False, 'error': 'No autenticado.'}, status=401)

    is_admin = request.user.is_superuser or request.user.username == 'admin'
    if not is_admin:
        return JsonResponse({'ok': False, 'error': 'Solo administradores pueden crear nuevos usuarios.'}, status=403)

    try:
        try:
            data = json.loads(request.body.decode('utf-8'))
        except Exception:
            data = request.POST

        username = data.get('username', '').strip().lower()
        password = data.get('password', '').strip()
        nombre = data.get('nombre', '').strip()

        if not username or not password:
            return JsonResponse({'ok': False, 'error': 'Usuario y contraseña son requeridos.'}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'ok': False, 'error': f'El usuario "{username}" ya existe.'}, status=400)

        user = User.objects.create_user(username=username, password=password, first_name=nombre)
        return JsonResponse({
            'ok': True,
            'mensaje': f'Usuario "{username}" creado exitosamente.',
            'usuario': {'id': user.id, 'username': user.username, 'nombre': user.first_name}
        })
    except Exception as e:
        return JsonResponse({'ok': False, 'error': f'Error al crear usuario: {str(e)}'}, status=500)


# =====================================================================
# Endpoints para el Bot de WhatsApp Nocturno (bot_nocturno.py)
# =====================================================================

@csrf_exempt
@require_GET
def bot_pendientes(request):
    """Devuelve los mensajes pendientes para procesar por el bot nocturno."""
    try:
        pendientes = CrmColaWhatsapp.objects.filter(estado='pendiente').order_by('id')[:100]
        lista = []
        for m in pendientes:
            lista.append({
                'id': m.id,
                'telefono': m.telefono,
                'nombre_contacto': m.nombre_contacto or 'Contacto',
                'mensaje': m.mensaje,
                'usuario': m.usuario,
                'fecha_programada': m.fecha_programada.strftime('%Y-%m-%d') if m.fecha_programada else '',
            })
        return JsonResponse({'ok': True, 'mensajes': lista, 'total': len(lista)})
    except Exception as e:
        return JsonResponse({'ok': False, 'error': str(e), 'mensajes': []}, status=500)


@csrf_exempt
@require_POST
def bot_actualizar(request):
    """El bot reporta el estado (procesando, enviado, error) de un mensaje."""
    try:
        try:
            data = json.loads(request.body.decode('utf-8'))
        except Exception:
            data = request.POST

        msg_id = data.get('id')
        nuevo_estado = data.get('estado')
        error_msg = data.get('error', '')

        if not msg_id or not nuevo_estado:
            return JsonResponse({'ok': False, 'error': 'ID y estado son requeridos.'}, status=400)

        mensaje = get_object_or_404(CrmColaWhatsapp, id=msg_id)
        mensaje.estado = nuevo_estado
        if error_msg:
            mensaje.error_detalle = error_msg
            mensaje.intentos = (mensaje.intentos or 0) + 1
        
        if nuevo_estado == 'enviado':
            mensaje.enviado_en = timezone.now()

        mensaje.save()
        return JsonResponse({'ok': True, 'mensaje': f'Estado de ID {msg_id} actualizado a {nuevo_estado}.'})
    except Exception as e:
        return JsonResponse({'ok': False, 'error': str(e)}, status=500)
