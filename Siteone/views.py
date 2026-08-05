from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
import time
from .models import *
import base64
from django.contrib.auth.hashers import make_password
import uuid
from django.contrib.auth.hashers import check_password
import hashlib
import re
import hmac
import binascii
from django.shortcuts import get_object_or_404, render
from .forms import *
import json
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.db.models.deletion import ProtectedError
import traceback 
from django.conf import settings
from django.utils import timezone
import datetime 
from django.http import JsonResponse
from django.db import connection
from .models import Municipios as MunicipioModel 
from .models import DocCandidatos as DocCandidatosModel
from django.db import IntegrityError
from django.db.models import Max
from django.db import IntegrityError
from django.core.exceptions import ValidationError
import os
from datetime import datetime 
from django.contrib import messages
from fpdf import FPDF
from babel.dates import format_date  # Importa la función format_date de la librería babel
import locale 
import qrcode
from PIL import Image
from io import BytesIO
import tempfile
from babel.dates import format_date, format_datetime, format_time
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import mysql.connector
import binascii

def Paquetes_armado_index (request):
     # Lógica para años
  hoy = datetime.today().date()
  año_actual = hoy.year

  años = []
  for i in range(año_actual, año_actual+11, +1):
    años.append(i)

  print(request.session['ID_USUARIO'])

  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])


  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos




  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion

  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
  context['años'] = años  # Agregar 'años' al diccionario de contexto


  return render(request, 'paquetes/armado_paquetes/Index.html', context)


def Computos_Agrecand_index (request):
  

     # Lógica para años
  hoy = datetime.today().date()
  año_actual = hoy.year

  idpartido = request.session['ID_PARTIDO']
  partido = Partidos.objects.get(idpartido=idpartido)
  nombre_partido = partido.desc_partido

  años = []
  for i in range(año_actual, año_actual+11, +1):
    años.append(i)

  print(request.session['ID_USUARIO'])
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
  context['años'] = años  # Agregar 'años' al diccionario de contexto
  context['nombre_partido'] = nombre_partido

  return render(request, 'computos/agregar_candidatos/Index.html', context)




def Pagina(request):



    return render(request, 'Pagina.html' )


def Login(request):
    try:
     id_usuario = request.session['ID_USUARIO']
    # Obtener el objeto que quieres actualizar
     usuario_obj = Inicio.objects.get(id_usuario=id_usuario)

    # Actualizar el campo que desees, por ejemplo, activar el usuario
     usuario_obj.activo = False

    # Guardar los cambios
     usuario_obj.save()
    except Exception:
        return render(request, 'Login.html')

    return render(request, 'Login.html')


def inicio(request):
   if request.session['ID_USUARIO']:
    id_estado = request.session['ID_ESTADO']

    logo = get_object_or_404(Oples, idestado=id_estado)
    print(logo.logo)

    print(request.session['ID_USUARIO'])
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

            
    context = {}
    if Usuario.per_regiscandidatura is not None:
        context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
    return render(request, 'base.html',context )



def verify_password(stored_password: str, input_password: str) -> bool:

    try:
        # Decodificar la contraseña almacenada y extraer el salt y el hash
        decoded_stored_password = base64.b64decode(stored_password)
        salt = decoded_stored_password[:16]  # Asumiendo que el salt es la primera parte
        stored_hash = decoded_stored_password[16:]  # El resto es el hash

        # Crear el hash de la contraseña ingresada usando el mismo salt
        input_hash = hashlib.pbkdf2_hmac(
            'sha256',  # Algoritmo de hash
            input_password.encode(),  # Contraseña ingresada en bytes
            salt,  # Salt en bytes
            100000  # Número de iteraciones
        )

        # Comparar el hash generado con el hash almacenado
        if hmac.compare_digest(input_hash, stored_hash):
            return True
        else:
            # Imprimir la contraseña ingresada y el valor esperado en caso de error
            print(f"Contraseña ingresada: {input_password}")
            print(f"Hash almacenado: {base64.b64encode(stored_hash).decode()}")
            print(f"Hash ingresado: {base64.b64encode(input_hash).decode()}")
            return False
    except (ValueError, TypeError) as e:
        # Captura errores de decodificación o de formato de datos
        print(f"Error al verificar la contraseña: {e}")
        print(f"Contraseña ingresada: {input_password}")
        return False
    
def hash_password(password: str) -> str:
    """
    Genera un hash seguro para una contraseña utilizando un salt aleatorio.

    Args:
        password (str): La contraseña que se desea hashear.

    Returns:
        str: La contraseña hasheada en formato base64 que incluye el salt y el hash.
    """
    # Generar un salt aleatorio de 16 bytes
    salt = os.urandom(16)
    
    # Crear el hash de la contraseña con el salt
    password_hash = hashlib.pbkdf2_hmac(
        'sha256',  # Algoritmo de hash
        password.encode(),  # Contraseña en bytes
        salt,  # Salt en bytes
        100000  # Número de iteraciones
    )
    
    # Combinar el salt y el hash en un solo byte string
    combined = salt + password_hash
    
    # Codificar el resultado en base64 para almacenamiento
    hashed_password = base64.b64encode(combined).decode()
    
    return hashed_password

def limpiar_entrada(entrada):
    # Eliminar caracteres peligrosos
    entrada_limpia = re.sub(r'[^\w\s]', '', entrada)
    
    # Verificar longitud mínima y máxima
    if len(entrada_limpia) < 3 or len(entrada_limpia) > 50:
        return "Error: Longitud de entrada no válida"
    
    # Verificar que no contenga solo espacios en blanco
    if entrada_limpia.strip() == "":
        return "Error: Entrada vacía o solo espacios en blanco"
    
    # Verificar que no contenga palabras clave peligrosas (ejemplo básico)
    palabras_peligrosas = ["SELECT", "INSERT", "DELETE", "DROP", "UPDATE", "SHOW", ]
    for palabra in palabras_peligrosas:
        if palabra.lower() in entrada_limpia.lower():
            return "Error: Intento de inyección SQL detectado"
    
    return entrada_limpia

def verification(request):
    if request.method == 'POST':
        peligro_entrada_usuario = request.POST.get('usuario')
        peligro_entrada_contraseña = request.POST.get('password')
        
        # Verificar y limpiar las entradas
        usuario_limpio = limpiar_entrada(peligro_entrada_usuario)
        contraseña_limpia = limpiar_entrada(peligro_entrada_contraseña)

        if "Error" in usuario_limpio:
            return HttpResponse(usuario_limpio, status=400)
        if "Error" in contraseña_limpia:
            return HttpResponse(contraseña_limpia, status=400)

        try:
            # 1. Se eliminó 'activo=False' para permitir buscar al usuario
            # independientemente de su estado actual en la BD.
            Usuario = Inicio.objects.get(usuario=usuario_limpio)
            
            # 2. Manejo de verificación con respaldo para contraseñas en texto plano
            try:
                es_valida = verify_password(Usuario.passencript, contraseña_limpia)
            except Exception:
                # Si falla el desencriptador (ej. texto plano como '123' en desarrollo),
                # se compara directamente en texto plano.
                es_valida = (Usuario.passencript == contraseña_limpia)

            if not es_valida:
                raise Inicio.DoesNotExist  # Salta al except si la contraseña no coincide

            # Limpieza de sesión previa
            request.session.pop('ID_PARTIDO', None)
            request.session.pop('ID_USUARIO', None)
            request.session.pop('ID_ESTADO', None)

            Pantallas = UsuariosPantallas.objects.get(id_usuario=Usuario.id_usuario)
            usuario_obj = Inicio.objects.get(id_usuario=Usuario.id_usuario)

            # Activar usuario
            usuario_obj.activo = True
            usuario_obj.save()

            context = {}
            if Usuario.per_regiscandidatura is not None:
                context['regiscandidatura'] = Usuario.per_regiscandidatura
            if Pantallas.revision_ople is not None:
                context['revision_ople'] = Pantallas.revision_ople
            if Pantallas.registro_de_gubernatura is not None:
                context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
            if Pantallas.registro_de_ayuntamiento is not None:
                context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
            if Pantallas.diputaciones_de_mayoria is not None:
                context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
            if Pantallas.diputaciones_de_rp is not None:
                context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
            if Pantallas.armado_de_documentacion is not None:
                context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
            if Pantallas.entrega_a_los_caes is not None:
                context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
            if Pantallas.caes_entrega_a_los_presidentes is not None:
                context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
            if Pantallas.entrega_de_paquetes_en_ca is not None:
                context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
            if Pantallas.resumen_de_paquetes is not None:
                context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
            if Pantallas.traslado_de_paquetes is not None:
                context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
            if Pantallas.registro_de_representantes is not None:
                context['registro_de_representantes'] = Pantallas.registro_de_representantes
            if Pantallas.representantes_ople is not None:
                context['representantes_ople'] = Pantallas.representantes_ople
            if Pantallas.registro_de_observadores is not None:
                context['registro_de_observadores'] = Pantallas.registro_de_observadores
            if Pantallas.agregar_candidatos is not None:
                context['agregar_candidatos'] = Pantallas.agregar_candidatos
            if Pantallas.computo_de_votos is not None:
                context['computo_de_votos'] = Pantallas.computo_de_votos
            if Pantallas.porcentajes_de_avances is not None:
                context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
            if Pantallas.resumen_de_actas is not None:
                context['resumen_de_actas'] = Pantallas.resumen_de_actas
            if Pantallas.votos_por_partido is not None:
                context['votos_por_partido'] = Pantallas.votos_por_partido
            if Pantallas.principios is not None:
                context['principios'] = Pantallas.principios
            if Pantallas.acciones_afirmativas is not None:
                context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
            if Pantallas.documentos is not None:
                context['documentos'] = Pantallas.documentos
            if Pantallas.entidades_federativas is not None:
                context['entidades_federativas'] = Pantallas.entidades_federativas
            if Pantallas.distritos is not None:
                context['distritos'] = Pantallas.distritos
            if Pantallas.municipios is not None:
                context['municipios'] = Pantallas.municipios
            if Pantallas.cargos_entrega is not None:
                context['cargos_entrega'] = Pantallas.cargos_entrega
            if Pantallas.partidos is not None:
                context['partidos'] = Pantallas.partidos
            if Pantallas.casillas is not None:
                context['casillas'] = Pantallas.casillas
            if Pantallas.centros_de_acopio is not None:
                context['centros_de_acopio'] = Pantallas.centros_de_acopio
            if Pantallas.usuarios is not None:
                context['usuarios'] = Pantallas.usuarios
            if Pantallas.tipo_eleccion is not None:
                context['tipo_eleccion'] = Pantallas.tipo_eleccion
            if Pantallas.partidos_coaliciones is not None:
                context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
            if Pantallas.eleccion_documentos is not None:
                context['eleccion_documentos'] = Pantallas.eleccion_documentos
            if Usuario.per_paquetes is not None:
                context['paquetes'] = Usuario.per_paquetes
            if Usuario.per_reprecomputos is not None:
                context['reprecomputos'] = Usuario.per_reprecomputos
            if Usuario.per_computoselectorales is not None:
                context['computoselectorales'] = Usuario.per_computoselectorales
            if Usuario.per_observadores is not None:
                context['observadores'] = Usuario.per_observadores
            if Usuario.per_configuracion is not None:
                context['configuracion'] = Usuario.per_configuracion

            request.session['ID_PARTIDO'] = Usuario.idpartido.idpartido
            request.session['ID_USUARIO'] = Usuario.id_usuario
            print('La variable global sesión es: ' + str(request.session['ID_USUARIO']))
            
            poder = 0
            try: 
                if Usuario.idestado:
                    poder = 1
            except Exception:   
                poder = 0  

            if poder == 1:
                request.session['ID_ESTADO'] = Usuario.idestado.idestado
                logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
                context['logo'] = logos.logo
            else:
                request.session['ID_ESTADO'] = 0
                context['logo'] = 'images/logo.png'     

            return render(request, 'base.html', context)
        
        except (Inicio.DoesNotExist, Exception) as e:
            request.session['ID_USUARIO'] = 0
            print(f'Error en autenticación: {e}')
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def principio(request):

    print(request.session['ID_USUARIO'])
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])
    print('LE VAIBELE EGLOBAL SESION es: ' + str(request.session['ID_USUARIO']))

    context = {}
    if Usuario.per_regiscandidatura is not None:
        context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

    principio = Principio.objects.all()

    context['principios_mostrar'] = principio  # Agregar 'años' al diccionario de contexto
    
    return render(request, 'configuracion/principio/Index.html', context)

def paridades(request):
     # Obtener todos los objetos Paridad
    print(request.session['ID_USUARIO'])
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])


    context = {}
    if Usuario.per_regiscandidatura is not None:
        context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

    paridades = Paridad.objects.all()
    context['paridades_mostrar'] = paridades  # Agregar 'años' al diccionario de contexto

    # Pasar los objetos como contexto a la plantilla
    return render(request, 'configuracion/paridad/Index.html', context)


def documentos(request):
     # Obtener todos los objetos tipodoc
    print(request.session['ID_USUARIO'])
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])


    context = {}
    if Usuario.per_regiscandidatura is not None:
        context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion
    doc = Tipodoc.objects.all()
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

    context['documentos_mostrar'] = doc  # Agregar 'años' al diccionario de contexto


    return render(request, 'configuracion/documentos/Index.html',context)

def documentos_editar(request, id):
    doc = get_object_or_404(Tipodoc, idtipo_doc=id)
    formulario = TipodocForm(request.POST or None, request.FILES or None, instance=doc)
    print(request.session['ID_USUARIO'])
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])


    context = {}
    if Usuario.per_regiscandidatura is not None:
        context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion
    doc = Tipodoc.objects.all()
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

    context['formulario'] = formulario
    context['doc'] = doc

    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('documentos')
    return render(request, 'configuracion/documentos/editar.html', context)

def documentos_agregar(request):
    formulario = TipodocForm(request.POST or None, request.FILES or None)
    print(request.session['ID_USUARIO'])
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])


    context = {}
    if Usuario.per_regiscandidatura is not None:
        context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos  
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion
    doc = Tipodoc.objects.all()
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

    context['formulario'] = formulario

    if formulario.is_valid():
        formulario.save()
        return redirect ('documentos')
    return render(request, 'configuracion/documentos/crear.html',context)



def Errorllave(request):
   return render(request, 'Vistas_Error/LlaveForanea.html',)


def documentos_eliminar(request, id):
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])


  context = {}
  if Usuario.per_regiscandidatura is not None:
        context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion
  doc = Tipodoc.objects.all()
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
  
  try:
    doc_obj = Tipodoc.objects.get(idtipo_doc=id)  
    doc_obj.delete()

  except IntegrityError:
    mensaje = "No se puede eliminar este Documento, debido a que esta asignado a una elección"
    messages.error(request, mensaje)
    Doc = Tipodoc.objects.all()
    print(request.session['ID_USUARIO'])

    context['documentos_mostrar'] = Doc

    return render(request, 'configuracion/documentos/index.html', context)  

  return redirect('documentos')



def estados(request):
    # Obtén el valor de ID_ESTADO desde settings
    id_estado = request.session['ID_ESTADO']

    estado_filtrado = Estados.objects.filter(idestado=id_estado)
    print(request.session['ID_USUARIO'])
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])


    context = {}
    if Usuario.per_regiscandidatura is not None:
        context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion
    doc = Tipodoc.objects.all()
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

    context['estados_mostrar'] = estado_filtrado

    return render(request, 'configuracion/estados/Index.html',context)


def estados_editar(request, id):
    estado = get_object_or_404(Estados, idestado=id)
    formulario = EstadosForm(request.POST or None, request.FILES or None, instance=estado)
    print(request.session['ID_USUARIO'])
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])


    context = {}
    if Usuario.per_regiscandidatura is not None:
        context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion
    doc = Tipodoc.objects.all()
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

    context['formulario'] = formulario
    context['doc'] = doc

    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('estados')
    return render(request, 'configuracion/estados/editar.html',context)




def estados_agregar(request):
    formulario = EstadosForm(request.POST or None, request.FILES or None)
    print(request.session['ID_USUARIO'])
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])


    context = {}
    if Usuario.per_regiscandidatura is not None:
        context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion
    doc = Tipodoc.objects.all()

    context['formulario'] = formulario
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

    if formulario.is_valid():
        formulario.save()
        return redirect ('estados')
    return render(request, 'configuracion/estados/crear.html',context)


def estados_eliminar(request, id):
    try:
        # Obtener el objeto Tipodoc por su id
        estado_obj = Tipodoc.objects.get(idtipo_doc=id)
        estado_obj.delete()
        return redirect('documentos')
    except ProtectedError as e:
        # Manejar la excepción (por ejemplo, redirigir a una vista específica)
        return render(request, 'Errorllave.html')

def partidos(request):
     # Obtener todos los objetos Paridad

    partido=Partidos.objects.all()
    print(request.session['ID_USUARIO'])
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])


    context = {}
    if Usuario.per_regiscandidatura is not None:
        context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion
    doc = Tipodoc.objects.all()
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

    context['partidos_mostrar'] = partido
     
    return render(request, 'configuracion/partidos/Index.html', context)

# HASTA QUI VOY CON EL MENU 

def partidos_agregar(request):
    formulario = PartidosForm(request.POST or None, request.FILES or None)
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])


    context = {}
    if Usuario.per_regiscandidatura is not None:
        context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion
    doc = Tipodoc.objects.all()
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto


    context['formulario'] = formulario    
    if formulario.is_valid():
        formulario.save()
        return redirect ('partidos')
    return render(request, 'configuracion/partidos/crear.html',  context)

def partidos_eliminar(request,id):
  
   Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
   Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])


   context = {}
   if Usuario.per_regiscandidatura is not None:
        context['regiscandidatura'] = Usuario.per_regiscandidatura
   if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
   if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
   if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
   if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
   if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
   if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
   if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
   if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
   if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
   if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
   if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
   if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
   if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
   if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
   if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
   if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
   if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
   if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
   if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
   if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
   if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
   if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
   if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
   if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
   if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
   if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
   if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
   if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
   if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
   if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
   if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
   if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
   if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

   if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
   if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
   if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
   if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
   if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion
   doc = Tipodoc.objects.all()


   logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
   context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

   try:
    partido_obj = Partidos.objects.get(idpartido=id)  
    partido_obj.delete()

   # context['partidos_mostrar'] = partido
   except IntegrityError:
    mensaje = "No se puede eliminar este Partido, debido a que esta asignado a una elección"
    messages.error(request, mensaje)
    partido = Partidos.objects.all()

    return render(request, 'configuracion/partidos/index.html', context)  

   return redirect('partidos')

def partidos_editar(request,id):
    partido = get_object_or_404(Partidos, idpartido=id)
    formulario = PartidosForm(request.POST or None, request.FILES or None, instance=partido)
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])


    context = {}
    if Usuario.per_regiscandidatura is not None:
        context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion
    doc = Tipodoc.objects.all()
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto


    context['formulario'] = formulario        
    context['doc'] = partido
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('partidos')
    return render(request, 'configuracion/partidos/editar.html', context)




def paridades_agregar(request):
    formulario = ParidadForm(request.POST or None, request.FILES or None)
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])


    context = {}
    if Usuario.per_regiscandidatura is not None:
        context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion
    doc = Tipodoc.objects.all()
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto


    context['formulario'] = formulario        
    if formulario.is_valid():
        formulario.save()
        return redirect ('paridad')
    return render(request, 'configuracion/paridad/crear.html', context)


def principios_agregar(request):
    formulario = PrincForm(request.POST or None, request.FILES or None)
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])


    context = {}
    if Usuario.per_regiscandidatura is not None:
        context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion
    doc = Tipodoc.objects.all()

    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

    context['formulario'] = formulario    

    if formulario.is_valid():
        formulario.save()
        return redirect ('principio')
    return render(request, 'configuracion/principio/crear.html', context)





def principios_editar(request, id):
    principios = Principio.objects.get(idprinc=id)
    formulario = PrincForm(request.POST or None, request.FILES or None, instance=principios)
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])


    context = {}
    if Usuario.per_regiscandidatura is not None:
        context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion
    doc = Tipodoc.objects.all()
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto


    context['formulario'] = formulario    
    context['principios'] = principios    
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect ('principio')
    return render(request, 'configuracion/principio/editar.html', context)



def paridades_editar(request, id):
    paridad = Paridad.objects.get(idparidad=id)
    formulario = ParidadForm(request.POST or None, request.FILES or None, instance=paridad)
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])


    context = {}
    if Usuario.per_regiscandidatura is not None:
        context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion
    doc = Tipodoc.objects.all()

    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

    context['formulario'] = formulario    
    context['paridad'] = paridad
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect ('paridad')
    return render(request, 'configuracion/paridad/editar.html', context)



def paridades_eliminar(request, id):
   Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
   Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])


   context = {}
   if Usuario.per_regiscandidatura is not None:
        context['regiscandidatura'] = Usuario.per_regiscandidatura
   if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
   if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
   if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
   if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
   if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
   if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
   if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
   if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
   if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
   if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
   if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
   if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
   if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
   if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
   if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
   if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
   if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
   if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
   if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
   if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
   if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
   if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
   if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
   if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
   if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
   if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
   if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
   if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
   if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
   if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
   if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
   if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
   if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
   if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
   if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
   if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
   if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
   if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion
   doc = Tipodoc.objects.all()
   logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
   context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
     
   try:
    paridad_obj = Paridad.objects.get(idparidad=id)  
    paridad_obj.delete()


   except IntegrityError:
    mensaje = "No se puede eliminar esta Acción Afirmativa, debido a que esta asignado a una elección"
    messages.error(request, mensaje)
    paridad = Paridad.objects.all()

    return render(request, 'configuracion/paridad/index.html', {'paridades_mostrar': paridad, **context})  

   return redirect('paridad')

def principio_eliminar(request, id):
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])


  context = {}
  if Usuario.per_regiscandidatura is not None:
        context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion
  doc = Tipodoc.objects.all()
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
    
  try:
    principio_obj = Principio.objects.get(idprinc=id)  
    principio_obj.delete()

  except IntegrityError:
    mensaje = "No se puede eliminar este Principio, debido a que esta asignado a una elección"
    messages.error(request, mensaje)
    principio = Principio.objects.all()

    return render(request, 'configuracion/principio/index.html', {'principios_mostrar': principio, **context})  

  return redirect('principio')


def cargosentrega(request):
     # Obtener todos los objetos Paridad
    cargo=CargosEntrega.objects.all()
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])


    context = {}
    if Usuario.per_regiscandidatura is not None:
        context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion
    doc = Tipodoc.objects.all()

    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto


    context['cargos_mostrar'] = cargo
    return render(request, 'configuracion/cargosentrega/Index.html', context)

def cargosentrega_agregar(request):
    formulario = CargosEntregaForm(request.POST or None, request.FILES or None)
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])


    context = {}
    if Usuario.per_regiscandidatura is not None:
        context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion
    doc = Tipodoc.objects.all()
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto


    context['formulario'] = formulario    

    if formulario.is_valid():
        formulario.save()
        return redirect ('cargosentrega')
    return render(request, 'configuracion/cargosentrega/crear.html', context)


def cargosentrega_eliminar(request,id):
   Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
   Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])


   context = {}
   if Usuario.per_regiscandidatura is not None:
        context['regiscandidatura'] = Usuario.per_regiscandidatura
   if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
   if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
   if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
   if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
   if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
   if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
   if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
   if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
   if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
   if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
   if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
   if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
   if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
   if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
   if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
   if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
   if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
   if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
   if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
   if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
   if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
   if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
   if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
   if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
   if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
   if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
   if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
   if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
   if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
   if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
   if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
   if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
   if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
   if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
   if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
   if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
   if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
   if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion
   doc = Tipodoc.objects.all()
   logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
   context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
 
   try:
    cargo_obj = CargosEntrega.objects.get(id_cargo_entrega=id)  
    cargo_obj.delete()
   except IntegrityError:
    mensaje = "No se puede eliminar este Cargo , debido a que esta asignado a una Casilla"
    messages.error(request, mensaje)
    cargo = CargosEntrega.objects.all()

    return render(request, 'configuracion/cargosentrega/index.html', {'cargos_mostrar': cargo, **context})  

   return redirect('cargosentrega')

def cargosentrega_editar(request,id):
    cargo = get_object_or_404(CargosEntrega, id_cargo_entrega=id)
    formulario = CargosEntregaForm(request.POST or None, request.FILES or None, instance=cargo)
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])


    context = {}
    if Usuario.per_regiscandidatura is not None:
        context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion
    doc = Tipodoc.objects.all()
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto


    context['formulario'] = formulario    
    context['cargos'] = cargo    
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('cargosentrega')
    return render(request, 'configuracion/cargosentrega/editar.html', context)



def casilla_consulta(request, iddistrito, nombreeleccion):
    with connection.cursor() as cursor:
        estado_id = request.session['ID_ESTADO']

        # Consulta a reemplzar por un Procedure 
        sql = """
        SELECT folioC, direccion 
        FROM casillas
        WHERE idProceso = (SELECT idProceso 
                           FROM procesos 
                           WHERE descrip = %s AND idEstado = %s)
          AND idDistrito = %s;
        """

        # Ejecutamos la consulta con los parámetros
        cursor.execute(sql, (nombreeleccion, estado_id, iddistrito))
        
        # Obtenemos los resultados
        casilla = cursor.fetchall()

        if len(casilla) > 0:
           data = {'message': "Success", 'casilla': casilla}
        else:
            data = {'message': "Not found"}

    return JsonResponse(data)



def casillas(request):

  # Obtener casillas
  casillas_mostrar = Casillas.objects.all()  
  print(request.session['ID_USUARIO'])
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
  # Obtener distrito
  distrito_nombre = Distritos.objects.filter(idestado=request.session['ID_ESTADO']).values_list('nombredistrito', flat=True)

  # Obtener entidad federativa
  entidad_federativa = Estados.objects.filter(idestado=request.session['ID_ESTADO']).values_list('nombre_edo', flat=True)

  # Obtener elección
  eleccion = Procesos.objects.all().values_list('descrip', flat=True)

  # Lógica para años
  hoy = datetime.today().date()
  año_actual = hoy.year

  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto


  años = []
  for i in range(año_actual, año_actual+11, +1):
    años.append(i)

  return render(request, 'configuracion/casillas/Index.html', {
    
      'distrito_nombre': distrito_nombre,
      'entidad_federativa': entidad_federativa,
      'años': años,  
      'eleccion': eleccion,
      'años': años,
      **context

  })


def casillas_eliminar(request, id):
    try:
        casilla_obj = Casillas.objects.get(folioc=id)
        casilla_obj.delete()
        data = {'message': "Success"}
    except Casillas.DoesNotExist:
        data = {'message': "Not found"}
    except IntegrityError:
        data = {'message': "Cannot delete, already assigned"}

    return JsonResponse(data)


def centros_acopio_eliminar(request,id):
  try:
    casilla_obj = CentrosDeAcopio.objects.get(IdCentroAcopio=id)  
    casilla_obj.delete()

  except IntegrityError:
    mensaje = "No se puede eliminar este Centro de Acopio, debido a que ya esta asignado a una casilla"
    messages.error(request, mensaje)

    return render(request, 'configuracion/centros_acopio/index.html')  

  return redirect('centros_ca')


def casillas_editar(request,id, eleccion, iddistrito, anio):


    estado_id = request.session['ID_ESTADO']
    proceso = get_object_or_404(Procesos, descrip=eleccion, idestado=estado_id)

    estado = get_object_or_404(Estados, idestado=estado_id)

    print(request.session['ID_USUARIO'])
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion       
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto


    casilla = get_object_or_404(Casillas, folioc=id)
    formulario = CasillasForm(request.POST or None, request.FILES or None, instance=casilla)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('casillas')
    return render(request, 'configuracion/casillas/editar.html', {'formulario': formulario, 'cargo': casilla, 'nombreedo':estado.nombre_edo, 'eleccion':eleccion, 'anio':anio, **context})




def centros_acopio_editar(request, id, anio):
    estado_id = request.session['ID_ESTADO']
    estado = get_object_or_404(Estados, idestado=estado_id)

    print(request.session['ID_USUARIO'])
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion       
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto


    centro = get_object_or_404(CentrosDeAcopio, Clave_ca=id)

    if request.method == 'POST':
        formulario = CentrosdeAcopioForm(
            request.POST, 
            request.FILES or None, 
            instance=centro,
            estado_id=estado_id
        )
        if formulario.is_valid():
            instancia = formulario.save(commit=False)
            
            # Asignamos explícitamente a las propiedades del modelo (con Mayúsculas)
            instancia.idDistrito = formulario.cleaned_data.get('idDistrito')
            instancia.idMunicipio = formulario.cleaned_data.get('idMunicipio')

            instancia.save()
            return redirect('centros_ca')
        else:
            print("Errores al editar:", formulario.errors)
    else:
        formulario = CentrosdeAcopioForm(instance=centro, estado_id=estado_id)

    return render(
        request, 
        'configuracion/centros_acopio/editar.html', 
        {'formulario': formulario, 'nombreedo': estado.nombre_edo, 'anio': anio, **context}
    )



def centros_acopio(request):

  # Obtener casillas
  casillas_mostrar = Casillas.objects.all()  
  print(request.session['ID_USUARIO'])
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
  # Obtener distrito
  distrito_nombre = Distritos.objects.filter(idestado=request.session['ID_ESTADO']).values_list('nombredistrito', flat=True)

  # Obtener entidad federativa
  entidad_federativa = Estados.objects.filter(idestado=request.session['ID_ESTADO']).values_list('nombre_edo', flat=True)

  # Obtener elección
  eleccion = Procesos.objects.all().values_list('descrip', flat=True)

  # Lógica para años
  hoy = datetime.today().date()
  año_actual = hoy.year

  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto


  años = []
  for i in range(año_actual, año_actual+11, +1):
    años.append(i)

  return render(request, 'configuracion/centros_acopio/Index.html', {
    
      'distrito_nombre': distrito_nombre,
      'entidad_federativa': entidad_federativa,
      'años': años,  
      'eleccion': eleccion,
      'años': años,
      **context

  })

def centros_acopio_consulta(request, idestado):
    try:
        # Verificar qué id llega
        print("idestado recibido:", idestado)

        # Consultar los centros de acopio del estado
        centros_qs = CentrosDeAcopio.objects.filter(
            Idestado_id=idestado
        ).values(
            'Clave_ca',
            'Nombre_ca',
            'Direccion_ca',
            'Latitud_ca',
            'Longitud_ca',
            'Anio'
        )

        # Ver cuántos registros encontró
        print("Total encontrados:", centros_qs.count())

        centros_de_acopio = list(centros_qs)

        if centros_de_acopio:
            data = {
                'message': 'Success',
                'centros': centros_de_acopio
            }
        else:
            data = {
                'message': 'Not found',
                'centros': []
            }

        return JsonResponse(data)

    except Exception as e:
        print(f"Error en centros_acopio_consulta: {e}")
        return JsonResponse(
            {
                'message': 'Error',
                'error': str(e)
            },
            status=500
        )

def distritos(request):

  print(request.session['ID_USUARIO'])
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion 


  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

  with connection.cursor() as cursor:
    
    estado_id = request.session['ID_ESTADO']
    
    sql = f"SELECT idDistrito, nombreDistrito FROM distritos WHERE idEstado = {estado_id}"

    cursor.execute(sql)
    
    distritos = cursor.fetchall()

  return render(request, "configuracion/distritos/Index.html", {
    "distritos_mostrar": distritos, **context  
  })




def distritos_agregar(request):
    estado_id = request.session['ID_ESTADO']  # Obtén el ID_ESTADO de settings
    print(request.session['ID_USUARIO'])
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

    # Inicializa el formulario con el valor predeterminado para idestado
    formulario = DistritosForm(initial={'idestado': estado_id})

    if request.method == 'POST':
        formulario = DistritosForm(request.POST)
        if formulario.is_valid():
            estado = formulario.cleaned_data['idestado']
            distrito = formulario.save(commit=False)
            distrito.idestado_id = estado.idestado 
            distrito.save()
            return redirect('distritos')

    return render(request, 'configuracion/distritos/crear.html', {
        'formulario': formulario,
        'estado_id': estado_id,
        **context
    })


def distritos_eliminar(request,id):
  estado_id = request.session['ID_ESTADO']
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])


  context = {}
  if Usuario.per_regiscandidatura is not None:
        context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion
  doc = Tipodoc.objects.all()
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

  try:
    principio_obj = Distritos.objects.get(iddistrito=id)  
    principio_obj.delete()

  except IntegrityError:
    mensaje = "No se puede eliminar este Distriro, debido a que esta asignado"
    messages.error(request, mensaje)
    principio = Distritos.objects.filter(idestado=estado_id)
    context['distritos_mostrar'] = principio

    return redirect('distritos')

  return redirect('distritos')


def distritos_editar(request, id):

  print(request.session['ID_USUARIO'])
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion    

  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto


  distrito = get_object_or_404(Distritos, iddistrito=id)
  formulario = DistritosForm(request.POST or None, 
                             instance=distrito)

  municipio= MunicipioModel.objects.filter(iddistrito=id)



  if formulario.is_valid() and request.POST:
     formulario.save()
     return redirect('distritos')

  return render(request, 'configuracion/distritos/editar.html', {'formulario': formulario, 'municipios_mostrar': municipio, **context
})

def Elecciones(request):

  # Generar años
  hoy = datetime.today().date()
  año_actual = hoy.year
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])


  context = {}
  if Usuario.per_regiscandidatura is not None:
        context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion

  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

  doc = Tipodoc.objects.all()
    
  años = []
  for i in range(año_actual, año_actual+11, +1):
    años.append(i)
  context['años'] = años

  return render(request, 'elecciones/Index.html', {
    **context
  })


def Elecciones_consultar(request, nombreeleccion):
   with connection.cursor() as cursor:
        
        estado_id = request.session['ID_ESTADO']

        # Consulta a reemplzar por un Procedure 
        sql = """
         SELECT idProceso, descrip 
FROM dbsite.procesos 
WHERE idEstado = %s 
AND anio = %s 
AND idProceso NOT BETWEEN 1 AND 38;

        """
        # Ejecutamos la consulta con los parámetros
        cursor.execute(sql, (estado_id, nombreeleccion))
        
        # Obtenemos los resultados
        Eleccion = cursor.fetchall()

        if len(Eleccion) > 0:
           data = {'message': "Success", 'eleccion': Eleccion}
        else:
            data = {'message': "Not found"}

   return JsonResponse(data)




def Elecciones_agregar(request, anio):
  
  estado_id = request.session['ID_ESTADO']

  formulario = ProcesosFrom(initial={'idestado': estado_id, 'anio': anio})
  if request.method == 'POST':
    formulario = ProcesosFrom(request.POST)
    if formulario.is_valid():
      
      estado = formulario.cleaned_data['idestado'] 
      principio = formulario.cleaned_data['idprinc']
      paridad = formulario.cleaned_data['idparidad']
      añoelec= formulario.cleaned_data['anio']
      proceso = formulario.save(commit=False)
      descrip = 'Proceso Electoral '+str(formulario.cleaned_data['idestado'])+' '+str(añoelec)
      proceso.idestado_id = estado.idestado 
      proceso.descrip = descrip
      proceso.idprinc_id = principio.idprinc
      proceso.idparidad_id = paridad.idparidad
      proceso.save()
      return redirect('elecciones_vista')

  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion    

  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto


  return render(request, 'elecciones/crear.html', {'formulario': formulario,  **context})

def Elecciones_eliminar(request,id):
  try:
    eleccion_obj = Procesos.objects.get(idproceso=id)  
    eleccion_obj.delete()

  except IntegrityError:
    mensaje = "No se puede eliminar este Proceso, debido a que esta en Curso"
    messages.error(request, mensaje)

    return render(request, 'elecciones/index.html')  

  return redirect('elecciones_vista')


def Elecciones_editar(request, id):
  proceso = get_object_or_404(Procesos, idproceso=id)
  formulario = ProcesosFrom(request.POST or None, instance=proceso)

  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion    

  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

  if formulario.is_valid() and request.POST:
     
     congreso = formulario.cleaned_data['congreso']
     ayuntamiento = formulario.cleaned_data['ayuntamiento']
     gubernatura = formulario.cleaned_data['gubernatura']  

     if not congreso: 
        num_eleco = Procesoscargo.objects.filter(idproceso=id, idtipo_cargo=2).first()
        if num_eleco:
            context['error'] = 'El registro no se puede guardar porque ya está asociado a un distrito.'
            return render(request, 'elecciones/editar.html', {'formulario': formulario, **context}) 
     if not ayuntamiento:
        num_eleca = Procesoscargo.objects.filter(idproceso=id, idtipo_cargo=1).first()      
        if num_eleca:
            context['error'] = 'El registro no se puede guardar porque ya está asociado a un municipio.'
            return render(request, 'elecciones/editar.html', {'formulario': formulario, **context})             
     if not gubernatura: 
        num_elec = Procesoscargo.objects.filter(idproceso=id, idtipo_cargo=3).first()
        if num_elec:
            context['error'] = 'El registro no se puede guardar porque ya está asociado a un estado.'
            return render(request, 'elecciones/editar.html', {'formulario': formulario, **context})              
     
     formulario.save()
     return redirect('elecciones_vista')
  


  return render(request, 'elecciones/editar.html', {'formulario': formulario, **context})







def Elecciones_editar_cargos(request, id, anio,idestado):
  proceso = get_object_or_404(Procesos, idproceso=id)
  estado = get_object_or_404(Estados, idestado=idestado)

  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion    

  
  

  if proceso.ayuntamiento:
      print ("Holaaa si hay de ayuntamiento ")

      numelec_ayuntamiento = Procesoscargo.objects.filter(idproceso=id, idtipo_cargo=1)
      municipios_excluidos = numelec_ayuntamiento.values_list('idMunicipio', flat=True)
      context['numelec_ayuntamiento'] = numelec_ayuntamiento
      context['municipio'] = MunicipioModel.objects.filter(idestado=idestado).exclude(idmunicipio__in=municipios_excluidos)
      
  if proceso.congreso:
      print ("Holaaa si hay congreso")
      
      numelec_congreso = Procesoscargo.objects.filter(idproceso=id, idtipo_cargo=2)
      distritos_excluidos = numelec_congreso.values_list('idDistrito', flat=True)
      context['numelec_congreso'] = numelec_congreso
      context['distrito'] = Distritos.objects.filter(idestado=idestado).exclude(iddistrito__in=distritos_excluidos)


  if proceso.gubernatura:
      print ("Holaaa si hay congreso")
      context['estado'] = Estados.objects.filter(idestado=idestado)    
      context['numelec_gubernatura'] = Procesoscargo.objects.filter(idproceso=id, idtipo_cargo=3)

  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
  context['años']= [anio]
  context['estado']= [estado.nombre_edo]
  context['eleccion'] = [proceso.descrip]

  if request.method == 'POST':
    # Recoger todos los IDs enviados en las listas
    municipio_ids = request.POST.getlist('municipio_ids')
    municipio_tabla = request.POST.get('municipio_tabla')
    distrito_ids = request.POST.getlist('distrito_ids')
    distrito_tabla = request.POST.get('distrito_tabla')
    estado_ids = request.POST.getlist('estado_ids')
    estado_tabla = request.POST.get('estado_tabla')

    # Insertar Municipios
    print("Intentando insertar Municipios:")
    for municipio_id in municipio_ids:
        # Verifica si ya existe un registro con los mismos idproceso, idtipo_cargo y idMunicipio
        if not Procesoscargo.objects.filter(idproceso=id, idtipo_cargo=1, idMunicipio=municipio_id).exists():
            # Si no existe, insertar el nuevo registro
            Procesoscargo.objects.create(
                idproceso=id,
                idestado_id=idestado,
                idDistrito_id=None,  # Puedes ajustar esto si es necesario
                idMunicipio_id=municipio_id,
                anio=anio,
                idtipo_cargo_id=1
            )
            print(f"Municipio ID {municipio_id} insertado.")
        else:
            print(f"Municipio ID {municipio_id} ya existe. No se inserta.")

    # Insertar Distritos
    print("Intentando insertar Distritos:")
    for distrito_id in distrito_ids:
        # Verifica si ya existe un registro con los mismos idproceso, idtipo_cargo y idDistrito
        if not Procesoscargo.objects.filter(idproceso=id, idtipo_cargo=2, idDistrito=distrito_id).exists():
            # Si no existe, insertar el nuevo registro
            Procesoscargo.objects.create(
                idproceso=id,
                idestado_id=idestado,
                idDistrito_id=distrito_id,
                idMunicipio_id=None,  # Puedes ajustar esto si es necesario
                anio=anio,
                idtipo_cargo_id=2
            )
            print(f"Distrito ID {distrito_id} insertado.")
        else:
            print(f"Distrito ID {distrito_id} ya existe. No se inserta.")

    print("Estado IDs:")
    for estado_id in estado_ids:
        print(f"ID: {estado_id}, Tabla: {estado_tabla}")

    # Lógica adicional según sea necesario
    # Aquí puedes recorrer las listas y guardar cada conjunto de datos en la base de datos, por ejemplo.


    
 

  return render(request, 'elecciones/editar-cargos.html', {**context})




def Municipios(request):
  print(request.session['ID_USUARIO'])
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion    
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
  return render(request, "configuracion/municipios/Index.html", context)




def Municipios_consultar(request): 

  with connection.cursor() as cursor:
    
    estado_id = request.session['ID_ESTADO']
    
   # Consulta a reemplzar por un Procedure 
    sql = """
      SELECT idMunicipio, nombre_mpo FROM dbsite.municipios where idEstado=%s;
        """

        # Ejecutamos la consulta con los parámetros
    cursor.execute(sql, (estado_id))
        
        # Obtenemos los resultados
    Municipios = cursor.fetchall()


    if len(Municipios) > 0:
        data = {'message': "Success", 'municipios': Municipios}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)

#hasta aca voy lkadsjfnsda

def municipios_agregar(request):
    estado_id = request.session['ID_ESTADO']  # Obtén el ID_ESTADO de la sesión
    distritosEstado = Distritos.objects.filter(idestado=estado_id)
    print(distritosEstado)
    
    # Inicializa el formulario con el valor predeterminado para idestado
    print(request.session['ID_USUARIO'])
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
        context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion    

    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo  # Agregar 'logo' al diccionario de contexto

    if request.method == 'POST':
        formulario = MunicipioForm(request.POST, estado_id=estado_id)
        if formulario.is_valid():
            estado = formulario.cleaned_data['idestado']
            distrito = formulario.cleaned_data['iddistrito']
            municipio = formulario.save(commit=False)
            municipio.idestado_id = estado.idestado
            municipio.iddistrito_id = distrito.iddistrito
            municipio.save()
            return redirect('municipios')
    else:
        formulario = MunicipioForm(initial={'idestado': estado_id}, estado_id=estado_id)

    return render(request, 'configuracion/municipios/crear.html', {
        'formulario': formulario, **context
    })



def casillas_agregar(request, eleccion, iddistrito, anio, idestado):
    # Obtén el objeto de Procesos basado en la variable 'eleccion' y 'idestado'
    print(request.session['ID_USUARIO'])
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion    
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
    estado_id = request.session['ID_ESTADO']
    proceso = get_object_or_404(Procesos, descrip=eleccion, idestado=estado_id)

    estado = get_object_or_404(Estados, idestado=estado_id)
    # Filtra el conjunto de datos para idproceso en el formulario
    formulario = CasillasForm(initial={'idestado': estado_id, 'idproceso': proceso,  'iddistrito': iddistrito }, estado_id=estado_id)

    if request.method == 'POST':
        formulario = CasillasForm(request.POST)
        if formulario.is_valid():
            
            municipio = formulario.cleaned_data['idmunicipio']  
            distrito = formulario.cleaned_data['iddistrito']

            casilla = formulario.save(commit=False)
            casilla.idestado_id = estado.idestado
            casilla.idmunicipio_id = municipio.idmunicipio
            casilla.iddistrito_id = distrito.iddistrito
            casilla.idproceso_id = proceso.idproceso
            
            casilla.save()
            
            return redirect('casillas')

    return render(request, 'configuracion/casillas/crear.html', {'formulario': formulario, 'nombreedo':estado.nombre_edo, 'eleccion':eleccion,  'anio':anio, **context})






def Centros_acopio_agregar(request, anio, idestado):
    # Obtén el objeto de Procesos basado en la variable 'eleccion' y 'idestado'
    print(request.session['ID_USUARIO'])
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion    
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
    estado_id = request.session['ID_ESTADO']
  
    estado = get_object_or_404(Estados, idestado=estado_id)
    # Filtra el conjunto de datos para idproceso en el formulario
    formulario = CentrosdeAcopioForm(
    estado_id=estado_id
)

    if request.method == 'POST':
        formulario = CentrosdeAcopioForm(request.POST, request.FILES or None, estado_id=estado_id)
        if formulario.is_valid():
            casilla = formulario.save(commit=False)
            casilla.Idestado = estado
            casilla.Anio = anio
            casilla.idMunicipio = formulario.cleaned_data.get('idMunicipio')
            casilla.idDistrito = formulario.cleaned_data.get('idDistrito')
            casilla.save()
            return redirect('centros_ca')
    else:
        # AQUÍ: Pasamos estado_id en la petición GET para filtrar distritos/municipios iniciales
        formulario = CentrosdeAcopioForm(estado_id=estado_id)

    return render(
        request, 
        'configuracion/centros_acopio/crear.html', 
        {'formulario': formulario, 'nombreedo': estado.nombre_edo, 'anio': anio, **context}
    )





def Municipios_eliminar(request,id):
   Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
   Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

   context = {}
   if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
   if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
   if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
   if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
   if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
   if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
   if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
   if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
   if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
   if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
   if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
   if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
   if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
   if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
   if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
   if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
   if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
   if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
   if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
   if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
   if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
   if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
   if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
   if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
   if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
   if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
   if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
   if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
   if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
   if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
   if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
   if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
   if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
   if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
   if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
   if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
   if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
   if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
   if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
   logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
   context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto    
   try:
     principio_obj = MunicipioModel.objects.get(idmunicipio=id)  
     principio_obj.delete()


   except IntegrityError:
    mensaje = "No se puede eliminar este Municipio, debido a que esta asignado a algun Distrito"
    messages.error(request, mensaje)
    principio = MunicipioModel.objects.all()

    return render(request, 'configuracion/municipios/index.html', {'municipios_mostrar': principio, **context})  

   return redirect('municipios')


def Municipios_editar(request, id):
  municipio = get_object_or_404(MunicipioModel, idmunicipio =id)
  estado_id = request.session['ID_ESTADO']
  formulario = MunicipioForm(request.POST or None, 
                             instance=municipio, estado_id=estado_id)
  print(request.session['ID_USUARIO'])
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
  if formulario.is_valid() and request.POST:
     formulario.save()
     return redirect('municipios')

  return render(request, 'configuracion/municipios/editar.html', {'formulario': formulario, **context})


def partidos_coaliciones(request):
  hoy = datetime.today().date()
  año_actual = hoy.year

  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  

  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
  idpartido = request.session['ID_PARTIDO']
  partido = Partidos.objects.get(idpartido=idpartido)
  nombre_partido = partido.desc_partido


  años = []
  for i in range(año_actual, año_actual+11, +1):
    años.append(i)

  return render(request, 'configuracion/partidos_coaliciones/Index.html', {
    
      'años': años,
      'nombre_partido': nombre_partido,
      **context
  })


def Usuarios_Index(request):
  hoy = datetime.today().date()
  año_actual = hoy.year

  idpartido = request.session['ID_PARTIDO']
  partido = Partidos.objects.get(idpartido=idpartido)
  nombre_partido = partido.desc_partido
  print(request.session['ID_USUARIO'])
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion   
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
  años = []
  for i in range(año_actual, año_actual+11, +1):
    años.append(i)

  return render(request, 'configuracion/Usuarios/Index.html', {
    
      'años': años,
      'nombre_partido': nombre_partido,
      **context
  })


def Usuarios_eliminar(request,id):
  try:
    Usuario_obj = Inicio.objects.get(id_usuario=id)  
    Usuario_obj.delete()

  except IntegrityError:
    mensaje = "No se puede Este Usuario, Code: 54"
    messages.error(request, mensaje)

    return render(request, 'configuracion/Usuarios/Index.html')  

  return redirect('Usuarios_Index')



def partidos_coaliciones_eliminar(request,id):
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])  
  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado) 
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto      
  
  try:
    Procesopartidos_obj = Procesopartidos.objects.get(idprocesopartido=id)  
    Procesopartidos_obj.delete()

  except IntegrityError:
    mensaje = "No se puede eliminar esta Coalición, debido a que ya esta asignada"
    messages.error(request, mensaje)

    return render(request, 'configuracion/partidos_coaliciones/index.html', {**context})  

  return redirect('partidoscolas_coaliciones')



def partidos_coaliciones_editar(request,id):
    procesopartido = get_object_or_404(Procesopartidos, idprocesopartido=id)
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
    formulario = ProcesosPartidos(request.POST or None, request.FILES or None, instance=procesopartido)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('partidoscolas_coaliciones')
    return render(request, 'configuracion/partidos_coaliciones/editar.html', {'formulario': formulario, 'cargo': procesopartido, **context})



def Usuarios_editar(request,id):
    Usuario = get_object_or_404(Inicio, id_usuario=id)
    print(request.session['ID_USUARIO'])
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion   
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
    formulario = Usuarios_Agregar(request.POST or None, request.FILES or None, instance=Usuario)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('Usuarios_Index')
    return render(request, 'configuracion/Usuarios/editar.html', {'formulario': formulario, 'cargo': Usuario, **context})

def partidos_coaliciones_agregar(request, anio):
    estado_id = request.session['ID_ESTADO']
    partidos = Partidos.objects.all()
    #proceso = get_object_or_404(Procesos, idestado=estado_id, anio=anio)
    formulario = ProcesosPartidos(initial={'idestado': estado_id, 'anio': anio})
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])


    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion   

    context['logo'] = get_object_or_404(Oples, idestado=Usuario.idestado.idestado).logo # Agregar 'años' al diccionario de contexto
    context['partidos_mostrar'] = partidos
    context['formulario']=formulario

    permisos = ['per_regiscandidatura', 'per_paquetes', 'per_reprecomputos', 'per_computoselectorales', 'per_observadores', 'per_configuracion']
    for permiso in permisos:
        if getattr(Usuario, permiso) is not None:
            context[permiso] = getattr(Usuario, permiso)

    if request.method == 'POST':
        formulario = ProcesosPartidos(request.POST)
        if formulario.is_valid():
            estado = formulario.cleaned_data['idestado']
            coalicion = formulario.save(commit=False)
            coalicion.idestado_id = estado.idestado
            #coalicion.idproceso_id = proceso.idproceso
            coalicion.anio = anio

            tipo = request.POST.get('tipo')
            partido_id = request.POST.get('partidos')
            selected_partidos_json = request.POST.get('selected_partidos')

            if tipo == 'P' and partido_id:
                partidoselect = get_object_or_404(Partidos, idpartido=partido_id)
                coalicion.coliacion = partidoselect.partido
                coalicion.save()

                PartidosCoaliciones.objects.create(
                    idprocesopartido=coalicion,
                    #idproceso=proceso,
                    idestado=estado,
                    anio=anio,
                    idpartido=partidoselect
                )

            elif tipo == 'C' and selected_partidos_json:
                selected_partidos = json.loads(selected_partidos_json)
                coalicion.save()

                for partido_siglas in selected_partidos:
                    partido = Partidos.objects.get(partido=partido_siglas)
                    PartidosCoaliciones.objects.create(
                        idprocesopartido=coalicion,
                        #idproceso=proceso,
                        idestado=estado,
                        anio=anio,
                        idpartido=partido
                    )
                    print('holaa: '+str(partido));

            return redirect('partidoscolas_coaliciones')

    return render(request, 'configuracion/partidos_coaliciones/crear.html', context)


def Usuarios_agregar(request, eleccion, idcargo, anio):
    estado_id = request.session['ID_ESTADO']
    proceso = get_object_or_404(Procesos, descrip=eleccion, idestado=estado_id)
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
    formulario = Usuarios_Agregar(initial={'idestado': estado_id, 'idproceso': proceso, 'idtipo_cargo': idcargo })

    if request.method == 'POST':
        formulario = Usuarios_Agregar(request.POST)
        if formulario.is_valid():
            estado = formulario.cleaned_data['idestado']
            proceso = formulario.cleaned_data['idproceso']
            cargo = formulario.cleaned_data['idtipo_cargo']


            contrasena = formulario.cleaned_data['passencript']
            
            # Verificar si idpartido está presente en los datos limpios del formulario
            if 'idpartido' in formulario.cleaned_data:
                partido = formulario.cleaned_data['idpartido']
            else:
                partido = 1  # Asignar None si idpartido no está presente
            
            usuario = formulario.save(commit=False)

            usuario.idestado_id = estado.idestado
            usuario.idproceso_id = proceso.idproceso
            usuario.idtipo_cargo_id = cargo.idtipo_cargo
            
            # Asignar partido solo si no es None
            if partido:
                usuario.idpartido_id = partido.idpartido

            usuario.anio = anio

            usuario.passencript = hash_password(contrasena)
            usuario.save()
            id_usuario=usuario.pk
             # Insertar en la tabla UsuariosPantallas
            nuevo_registro = UsuariosPantallas(
             id_usuario_id=id_usuario,
             revision_ople=True,
             registro_de_gubernatura=True,
             registro_de_ayuntamiento=True,
             diputaciones_de_mayoria=True,
             diputaciones_de_rp=True,
             armado_de_documentacion=True,
             entrega_a_los_caes=True,
             caes_entrega_a_los_presidentes=True,
             entrega_de_paquetes_en_ca=True,
             resumen_de_paquetes=True,
             traslado_de_paquetes=True,
             registro_de_representantes=True,
             representantes_ople=True,
             registro_de_observadores=True,
             agregar_candidatos=True,
             computo_de_votos=True,
             porcentajes_de_avances=True,
             resumen_de_actas=True,
             votos_por_partido=True,
             principios=True,
             acciones_afirmativas=True,
             documentos=True,
             entidades_federativas=True,
             distritos=True,
             municipios=True,
             cargos_entrega=True,
             partidos=True,
             casillas=True,
             centros_de_acopio=True,
             usuarios=True,
             tipo_eleccion=True,
             partidos_coaliciones=True,
             eleccion_documentos=True
             )
        
        # Guarda el nuevo registro en la base de datos
            nuevo_registro.save()


            return redirect('Usuarios_Index')

    return render(request, 'configuracion/Usuarios/crear.html', {'formulario': formulario, **context})

def docelecciones(request):

  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos  
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales 
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
  # Lógica para años
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto  
  hoy = datetime.today().date()
  año_actual = hoy.year

  años = []
  for i in range(año_actual, año_actual+11, +1):
    años.append(i)

  return render(request, 'configuracion/elecciones_documentos/Index.html', {
    
      'años': años,
        **context
  })


def docelecciones_consulta(request, nombreeleccion):
    with connection.cursor() as cursor:
        estado_id = request.session['ID_ESTADO']

        # Consulta a reemplzar por un Procedure 
        sql = """
SELECT dc.idProceso, td.descrip_doc, doc_candidatos_id
               FROM doc_candidatos dc
               JOIN tipodoc td ON dc.idtipo_doc = td.idtipo_doc
               WHERE dc.idProceso = (SELECT idProceso 
               FROM procesos 
               WHERE descrip = %s AND idEstado = %s);

        """

        # Ejecutamos la consulta con los parámetros
        cursor.execute(sql, (nombreeleccion, estado_id) )
        
        # Obtenemos los resultados
        doc = cursor.fetchall()

    if len(doc) > 0:
        data = {'message': "Success", 'doc': doc}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)



def docelecciones_agregar(request, nombreeleccion):
    estado_id = request.session['ID_ESTADO']
    proceso = get_object_or_404(Procesos, descrip=nombreeleccion, idestado=estado_id)
    # Filtra el conjunto de datos para idproceso en el formulario
    formulario = DocCandidatosFrom(initial={'idproceso': proceso })
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
    if request.method == 'POST':
        formulario = DocCandidatosFrom(request.POST)
        if formulario.is_valid():
            doc = formulario.cleaned_data['idtipo_doc']
            proceso = formulario.cleaned_data['idproceso']

            document = formulario.save(commit=False)
            document.idestado_id = doc.idtipo_doc
            document.idmunicipio_id = proceso.idproceso
            formulario.save()
            return redirect('docelecciones')

    return render(request, 'configuracion/elecciones_documentos/crear.html', {'formulario': formulario, **context})




def docelecciones_eliminar(request,id):
    
    docelec_obj = DocCandidatosModel.objects.get(doc_candidatos_id=id)
    docelec_obj.delete()
    return redirect('docelecciones')


def docelecciones_editar(request, id):
  doc  = get_object_or_404(DocCandidatosModel, doc_candidatos_id =id)
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos 
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion    
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto


  formulario = DocCandidatosFrom(request.POST or None, 
                             instance=doc)

  if formulario.is_valid() and request.POST:
     formulario.save()
     return redirect('docelecciones')
    
  return render(request, 'configuracion/elecciones_documentos/editar.html', {'formulario': formulario})


 
def regicadAy_consulta(request, cargo, nombreeleccion, estado, anio):
    idpartido = request.session['ID_PARTIDO']
    estado_id = request.session['ID_ESTADO']
    idcargo = get_object_or_404(Tipocargo, descrip_tcargo=cargo)
    proceso = get_object_or_404(Procesos, descrip=nombreeleccion, idestado=estado_id)

    with connection.cursor() as cursor:
        # Llamada al procedimiento almacenado
        cursor.callproc('obtener_info_candidato_en_coalicion', [proceso.idproceso, idpartido, idcargo.idtipo_cargo, estado, anio])

        # Obtenemos los resultados
        candidatos = cursor.fetchall()

    if len(candidatos) > 0:
        data = {'message': "Success", 'candidatos': candidatos}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)


 
def regicadGU_consulta(request, cargo, nombreeleccion, id):
    # Obtener el estado actual desde settings
    id_estado = request.session['ID_ESTADO']
    id_partido = request.session['ID_PARTIDO']

    proceso = get_object_or_404(Procesos, descrip=nombreeleccion, idestado=id_estado)
    # Obtener el año actual

    print("valor de id: "+ str(id))

    if cargo==3:
     num_elect= Procesoscargo.objects.get(idproceso=proceso.idproceso, idtipo_cargo=3)
     print("idestado: "+str(num_elect.num_elec))
    else:
     num_elect = Procesoscargo.objects.get(
     Q(idproceso=proceso.idproceso) &
    (Q(idDistrito=id) | Q(idMunicipio=id)))

     print("municipio o distrito: "+str(num_elect.num_elec))

    # Filtrar las elecciones por ID_ESTADO y por año
    candidatos = list(Candidatos.objects.filter(idestado=id_estado,  num_elec=num_elect.num_elec, idpartido=id_partido ).values())

    if len(candidatos) > 0:
        data = {'message': "Success", 'candidatos': candidatos}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)


def regicadMY_consulta(request, cargo, nombreeleccion, id):
    # Obtener el estado actual desde settings
    id_estado = request.session['ID_ESTADO']
    id_partido = request.session['ID_PARTIDO']

    proceso = get_object_or_404(Procesos, descrip=nombreeleccion, idestado=id_estado)

    if cargo == 3:
        num_elect = Procesoscargo.objects.get(idproceso=proceso.idproceso, idtipo_cargo=3)
    else:
        num_elect = Procesoscargo.objects.get(
            Q(idproceso=proceso.idproceso) &
            (Q(idDistrito=id) | Q(idMunicipio=id))
        )

    candidatos = Candidatos.objects.filter(idestado=id_estado, num_elec=num_elect.num_elec, idpartido=id_partido, idprinc='MY')

# Serializar los datos de los candidatos
    candidatos_list = []
    for candidato in candidatos:
        candidatos_list.append({
        'id_cand': str(candidato.id_cand),
        'idproceso': str(candidato.idproceso.idproceso) if candidato.idproceso else None,
        'anio': str(candidato.anio),
        'idprocesopartido': str(candidato.idprocesopartido),
        'idprinc': str(candidato.idprinc),
        'idparidad': str(candidato.idparidad),
        'idtipo_cargo': str(candidato.idtipo_cargo),
        'idpartido': str(candidato.idpartido),
        'idestado': str(candidato.idestado),
        'idmunicipio': str(candidato.idmunicipio),
        'iddistrito': str(candidato.iddistrito),
        'nombres': str(candidato.nombres),
        'apaterno': str(candidato.apaterno),
        'amaterno': str(candidato.amaterno),
        'apodo': str(candidato.apodo),
        'genero': str(candidato.genero),
        'idestado_nacimiento': str(candidato.idestado_nacimiento),
        'fecha_nac': str(candidato.fecha_nac),
        'tel': str(candidato.tel),
        'domicilio': str(candidato.domicilio),
        'tiempo_res': str(candidato.tiempo_res),
        'ocupacion': str(candidato.ocupacion),
        'reeleccion': str(candidato.reeleccion),
        'anos_cons': str(candidato.anos_cons),
        'grup_vul': str(candidato.grup_vul),
        'grup_vulne': str(candidato.grup_vulne),
        'correo': str(candidato.correo),
        'clave_elect': str(candidato.clave_elect),
        'cic': str(candidato.cic),
        'ocr': str(candidato.ocr),
        'num_elec': str(candidato.num_elec),
        'num_emicion': str(candidato.num_emicion),
        'curp': str(candidato.curp),
        'vig_ine': str(candidato.vig_ine),
        'aprobado': str(candidato.aprobado),
        'registrado': str(candidato.registrado),
        'verificado': str(candidato.verificado),
        'centinela': str(candidato.centinela),
        'fecha_de_captura': str(candidato.fecha_de_captura),
        'comentarios': str(candidato.comentarios),
        'ruta': str(candidato.ruta),
        'tipo': str(candidato.tipo),
        'num_prelacion': str(candidato.num_prelacion),
        'id_propietario': str(candidato.id_propietario),
    })

    if candidatos_list:
        data = {'message': "Success", 'candidatos': candidatos_list}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data, safe=False)

def regicadRP_consulta(request, cargo, nombreeleccion, id):
    # Obtener el estado actual desde settings
    id_estado = request.session['ID_ESTADO']
    id_partido = request.session['ID_PARTIDO']

    proceso = get_object_or_404(Procesos, descrip=nombreeleccion, idestado=id_estado)

    if cargo == 3:
        num_elect = Procesoscargo.objects.get(idproceso=proceso.idproceso, idtipo_cargo=3)
    else:
        num_elect = Procesoscargo.objects.get(
            Q(idproceso=proceso.idproceso) &
            (Q(idDistrito=id) | Q(idMunicipio=id))
        )

    candidatos = Candidatos.objects.filter(idestado=id_estado, num_elec=num_elect.num_elec, idpartido=id_partido, idprinc='RP')

# Serializar los datos de los candidatos
    candidatos_list = []
    for candidato in candidatos:
        candidatos_list.append({
        'id_cand': str(candidato.id_cand),
        'idproceso': str(candidato.idproceso.idproceso) if candidato.idproceso else None,
        'anio': str(candidato.anio),
        'idprocesopartido': str(candidato.idprocesopartido),
        'idprinc': str(candidato.idprinc),
        'idparidad': str(candidato.idparidad),
        'idtipo_cargo': str(candidato.idtipo_cargo),
        'idpartido': str(candidato.idpartido),
        'idestado': str(candidato.idestado),
        'idmunicipio': str(candidato.idmunicipio),
        'iddistrito': str(candidato.iddistrito),
        'nombres': str(candidato.nombres),
        'apaterno': str(candidato.apaterno),
        'amaterno': str(candidato.amaterno),
        'apodo': str(candidato.apodo),
        'genero': str(candidato.genero),
        'idestado_nacimiento': str(candidato.idestado_nacimiento),
        'fecha_nac': str(candidato.fecha_nac),
        'tel': str(candidato.tel),
        'domicilio': str(candidato.domicilio),
        'tiempo_res': str(candidato.tiempo_res),
        'ocupacion': str(candidato.ocupacion),
        'reeleccion': str(candidato.reeleccion),
        'anos_cons': str(candidato.anos_cons),
        'grup_vul': str(candidato.grup_vul),
        'grup_vulne': str(candidato.grup_vulne),
        'correo': str(candidato.correo),
        'clave_elect': str(candidato.clave_elect),
        'cic': str(candidato.cic),
        'ocr': str(candidato.ocr),
        'num_elec': str(candidato.num_elec),
        'num_emicion': str(candidato.num_emicion),
        'curp': str(candidato.curp),
        'vig_ine': str(candidato.vig_ine),
        'aprobado': str(candidato.aprobado),
        'registrado': str(candidato.registrado),
        'verificado': str(candidato.verificado),
        'centinela': str(candidato.centinela),
        'fecha_de_captura': str(candidato.fecha_de_captura),
        'comentarios': str(candidato.comentarios),
        'ruta': str(candidato.ruta),
        'tipo': str(candidato.tipo),
        'num_prelacion': str(candidato.num_prelacion),
        'id_propietario': str(candidato.id_propietario),
    })

    if candidatos_list:
        data = {'message': "Success", 'candidatos': candidatos_list}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data, safe=False)

def consulta_usuarios(request, nombreelecion, idcargo):
    # Obtener el estado actual desde settings
    id_estado = request.session['ID_ESTADO']
    proceso = get_object_or_404(Procesos, descrip=nombreelecion, idestado=id_estado)

    # Obtener el año actual
    hoy = datetime.today().date()
    año_actual = hoy.year

    # Filtrar las elecciones por ID_ESTADO y por año
    usuarios = list(Inicio.objects.filter(idproceso=proceso.idproceso, idtipo_cargo=idcargo).values())

    if len(usuarios) > 0:
        data = {'message': "Success", 'candidatos': usuarios}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)

"""
def agregar_usuarios(request, eleccion, idcargo, anio):
    # Obtén el objeto de Procesos basado en la variable 'eleccion' y 'idestado'
    estado_id = request.session['ID_ESTADO']
    proceso = get_object_or_404(Procesos, descrip=eleccion, idestado=estado_id)

    # Filtra el conjunto de datos para idproceso en el formulario
    formulario = Usuarios_Agregar(initial={'idestado': estado_id, 'idproceso': proceso, 'idtipo_cargo': idcargo })

    if request.method == 'POST':
        formulario = Usuarios_Agregar(request.POST)
        if formulario.is_valid():
            estado = formulario.cleaned_data['idestado']
            proceso = formulario.cleaned_data['idproceso']
            cargo = formulario.cleaned_data['idtipo_cargo']
            cargo = formulario.cleaned_data['idpartido']

          
            coalicion = formulario.save(commit=False)
            coalicion.idestado_id = estado.idestado
            coalicion.idproceso_id = proceso.idproceso
            coalicion.anio = anio
            coalicion.idtipo_cargo_id = cargo.idtipo_cargo
            coalicion.save()
            
            return redirect('partidoscolas_coaliciones')

    return render(request, 'configuracion/partidos_coaliciones/crear.html', {'formulario': formulario})

"""

def regicadCO_RP_consulta(request, cargo, eleccion):
    # Obtener el estado actual desde settings
    id_estado = request.session['ID_ESTADO']
    idpartido = request.session['ID_PARTIDO']


    # Obtener el año actual
    hoy = datetime.today().date()
    año_actual = hoy.year
   
    proceso = get_object_or_404(Procesos, descrip=eleccion, idestado=id_estado)
    print(proceso.idproceso)
    cargo= get_object_or_404(Tipocargo, descrip_tcargo=cargo)
    print(cargo.idtipo_cargo)
   # Obtén la instancia de PartidosCoaliciones basada en idpartido e idproceso
    procesopartido = get_object_or_404(PartidosCoaliciones, idpartido=idpartido,  idestado=id_estado)

    print(procesopartido.idprocesopartido.idprocesopartido) 
    candidatos = list(Candidatos.objects.filter(idestado=id_estado, idproceso=proceso.idproceso, idprinc='RP', idtipo_cargo=cargo.idtipo_cargo, idprocesopartido=procesopartido.idprocesopartido.idprocesopartido).values())

    if len(candidatos) > 0:
        data = {'message': "Success", 'candidatos': candidatos}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)


def regicadCO_MY_consulta(request, cargo, eleccion):
    # Obtener el estado actual desde settings
    id_estado = request.session['ID_ESTADO']
    idpartido = request.session['ID_PARTIDO']
    # Obtener el año actual
    hoy = datetime.today().date()
    año_actual = hoy.year
    proceso = get_object_or_404(Procesos, descrip=eleccion, idestado=id_estado)
    print(proceso.idproceso)
    cargo= get_object_or_404(Tipocargo, descrip_tcargo=cargo)
    print(cargo.idtipo_cargo)
    # Filtrar las elecciones por ID_ESTADO y por año
    # Obtén la instancia de PartidosCoaliciones basada en idpartido e idproceso
    procesopartido = get_object_or_404(PartidosCoaliciones, idpartido=idpartido,  idestado=id_estado)

    print(procesopartido.idprocesopartido.idprocesopartido) 

    candidatos = list(Candidatos.objects.filter(idestado=id_estado, idproceso=proceso.idproceso, idprinc='MY', idtipo_cargo=cargo.idtipo_cargo, idprocesopartido=procesopartido.idprocesopartido.idprocesopartido).values())

    if len(candidatos) > 0:
        data = {'message': "Success", 'candidatos': candidatos}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)





def Revicion_Ople_All(request, cargo, nombreeleccion, id):
    # Obtener el estado actual desde settings
    id_estado = request.session['ID_ESTADO']

    proceso = get_object_or_404(Procesos, descrip=nombreeleccion, idestado=id_estado)
    # Obtener el año actual

    print("valor de id: "+ str(id))

    if cargo==3:
     num_elect= Procesoscargo.objects.get(idproceso=proceso.idproceso, idtipo_cargo=3)
     print("idestado: "+str(num_elect.num_elec))
    else:
     num_elect = Procesoscargo.objects.get(
     Q(idproceso=proceso.idproceso) &
    (Q(idDistrito=id) | Q(idMunicipio=id)))

     print("municipio o distrito: "+str(num_elect.num_elec))

    # Filtrar las elecciones por ID_ESTADO y por año
    candidatos = list(Candidatos.objects.filter(idestado=id_estado,  num_elec=num_elect.num_elec ).values())

    if len(candidatos) > 0:
        data = {'message': "Success", 'candidatos': candidatos}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)




def regicand (request):
     # Lógica para años
  hoy = datetime.today().date()
  año_actual = hoy.year
  idpartido = request.session['ID_PARTIDO']
  partido = Partidos.objects.get(idpartido=idpartido)
  nombre_partido = partido.desc_partido
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion    
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
  años = []
  for i in range(año_actual, año_actual+11, +1):
    años.append(i)

  return render(request, 'registro_de_candidatura/Index.html', {
    
      'años': años,
      'nombre_partido': nombre_partido,
        **context
  })


def regicanRP (request):
     # Lógica para años
  hoy = datetime.today().date()
  año_actual = hoy.year
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
  idpartido = request.session['ID_PARTIDO']
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

  partido = Partidos.objects.get(idpartido=idpartido)
  nombre_partido = partido.desc_partido

  años = []
  for i in range(año_actual, año_actual+11, +1):
    años.append(i)

  return render(request, 'Registro_de Cadndidaturas_RP/Index.html', {
    
      'años': años,
      'nombre_partido': nombre_partido,
        **context
  })



def RevicionOple (request):
     # Lógica para años
  hoy = datetime.today().date()
  año_actual = hoy.year
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion    
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
  años = []
  for i in range(año_actual, año_actual+11, +1):
    años.append(i)

  return render(request, 'Revicion del Ople/Index.html', {
    
      'años': años,
        **context
  })



def regicanMY (request):
     # Lógica para años
  hoy = datetime.today().date()
  año_actual = hoy.year
  idpartido = request.session['ID_PARTIDO']
  partido = Partidos.objects.get(idpartido=idpartido)
  nombre_partido = partido.desc_partido
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
  años = []
  for i in range(año_actual, año_actual+11, +1):
    años.append(i)

  return render(request, 'regsitro_de_diputaciones_my/Index.html', {
    
      'años': años,
      'nombre_partido': nombre_partido,
        **context
  })


def regicandgu (request):
     # Lógica para años
  hoy = datetime.today().date()
  año_actual = hoy.year

  idpartido = request.session['ID_PARTIDO']
  partido = Partidos.objects.get(idpartido=idpartido)
  nombre_partido = partido.desc_partido
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
  años = []
  for i in range(año_actual, año_actual+11, +1):
    años.append(i)

  return render(request, 'Regsitro_de_Gubernatura/Index.html', {
    
      'años': años,
      'nombre_partido': nombre_partido,
        **context
  })


def regicandgo (request):
     # Lógica para años
  hoy = datetime.today().date()
  año_actual = hoy.year
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

  años = []
  for i in range(año_actual, año_actual+11, +1):
    años.append(i)

  return render(request, 'Regsitro_de_Gubernatura/Index.html', {
    
      'años': años,
        **context
  })


def regicad_my (request):
     # Lógica para años
  hoy = datetime.today().date()
  año_actual = hoy.year
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion    
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

  años = []
  for i in range(año_actual, año_actual+11, +1):
    años.append(i)

  return render(request, 'regsitro_de_diputaciones_my/Index.html', {
    
      'años': años,
        **context
  })






def Editar_Gu_Ople(request, id, anio, nombreeleccion, nombrecargo):
    idcand = id
    eleccion = nombreeleccion
    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion      
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
    candidato = get_object_or_404(Candidatos, id_cand=id)

    # Verificar si todos los documentos relacionados están aprobados
    documentos = DocumentosCandidatos.objects.filter(id_cand=id)
    documentos_aprobados = all(doc.estatus_revicion == 'Aprobado' for doc in documentos)
    formulario = CandidatosFormGUOple(request.POST or None, instance=candidato)


    if formulario.is_valid() and request.POST:
        comentario = formulario.cleaned_data['comentarios']
        print("Comentarios: "+ comentario)
        if comentario == 'Aprobado':
         if not documentos_aprobados:

            mensaje_error = "Todos los documentos deben estar aprobados antes de aprobar al candidato."
            return render(request, 'Revicion del Ople/editar.html', {'formulario': formulario, 'anio': anio, 'nombrecargo': nombrecargo, 'nombre_partido': nombre_partido,  'idcand': idcand, 'eleccion': eleccion, 'mensaje_error': mensaje_error,  **context})
         else:
            formulario.save()
            return redirect('RevicionOple')
        else:
            formulario.save()
            return redirect('RevicionOple')

    return render(request, 'Revicion del Ople/editar.html', {'formulario': formulario, 'anio': anio, 'nombrecargo': nombrecargo, 'nombre_partido': nombre_partido,  'idcand': idcand, 'eleccion': eleccion, **context})


def Editar_Gu(request, id, anio,nombreeleccion,nombrecargo):
  
    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
    candidato = Candidatos.objects.get(id_cand=id)  # Reemplaza 1 con el ID que estás buscando
    candidato = get_object_or_404(Candidatos, id_cand =id)
    # Verifica si el valor de 'aprobado' es "SI"
    if candidato.aprobado == "SI":
        # Hacer algo si 'aprobado' es "SI"
        print("El candidato está aprobado.")
        aprobado = True
        formulario = CandidatosFormGU(request.POST or None, 
                             instance=candidato, readonly_mode=True)
    elif candidato.aprobado == "NO":
        # Hacer algo si 'aprobado' es "NO"
        print("El candidato no está aprobado.")
        aprobado = False
        formulario = CandidatosFormGU(request.POST or None, 
                             instance=candidato)
    else:
        # Hacer algo si 'aprobado' no es ni "SI" ni "NO"
        aprobado = False
        print("El estado de aprobación es desconocido.")
        formulario = CandidatosFormGU(request.POST or None, 
                             instance=candidato)
    

    if formulario.is_valid() and request.POST:
     formulario.save()
     return redirect('regicangu')

    return render(request, 'Regsitro_de_Gubernatura/editar.html', {'formulario': formulario, 'anio': anio, 'nombrecargo': nombrecargo, 'nombre_partido': nombre_partido, 'aprobado': aprobado, **context})



def Editar_Ay_Ople(request, id, anio,nombreeleccion,nombrecargo):
    idcand=id
    eleccion=nombreeleccion
    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
    candidato = Candidatos.objects.get(id_cand=id)  # Reemplaza 1 con el ID que estás buscando
    candidato = get_object_or_404(Candidatos, id_cand =id)
    if candidato.tipo == 'P':
     titulo = "Candidato Propietario"
    else:
     titulo = ""    

    # Verificar si todos los documentos relacionados están aprobados
    documentos = DocumentosCandidatos.objects.filter(id_cand=id)
    documentos_aprobados = all(doc.estatus_revicion == 'Aprobado' for doc in documentos)

    formulario = CandidatosFormAyOple(request.POST or None, 
                             instance=candidato)
 
    if formulario.is_valid() and request.POST:
        comentario = formulario.cleaned_data['comentarios']
        print("Comentarios: "+ comentario)
        if comentario == 'Aprobado':
         if not documentos_aprobados:

            mensaje_error = "Todos los documentos deben estar aprobados antes de aprobar al candidato."
            return render(request, 'Revicion del Ople/editar.html', {'formulario': formulario, 'anio': anio, 'nombrecargo': nombrecargo, 'nombre_partido': nombre_partido,  'idcand': idcand, 'eleccion': eleccion, 'mensaje_error': mensaje_error, 'titulo': titulo, **context})
         else:
            formulario.save()
            return redirect('RevicionOple')
        else:
            formulario.save()
            return redirect('RevicionOple')

    return render(request, 'Revicion del Ople/editar.html', {'formulario': formulario, 'anio': anio, 'nombrecargo': nombrecargo, 'nombre_partido': nombre_partido, 'idcand': idcand, 'eleccion': eleccion, 'titulo': titulo, **context})




def Editar_Co_Ople(request, id, anio,nombreeleccion,nombrecargo):
  
    idcand=id
    eleccion=nombreeleccion
    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto       
    candidato = Candidatos.objects.get(id_cand=id)  # Reemplaza 1 con el ID que estás buscando
    candidato = get_object_or_404(Candidatos, id_cand =id)
    titulo= "Candidato Propietario"

    # Verificar si todos los documentos relacionados están aprobados
    documentos = DocumentosCandidatos.objects.filter(id_cand=id)
    documentos_aprobados = all(doc.estatus_revicion == 'Aprobado' for doc in documentos)

    formulario = CandidatosFormMY_Propietario_Ople(request.POST or None, 
                             instance=candidato)
 
    if formulario.is_valid() and request.POST:
        comentario = formulario.cleaned_data['comentarios']
        print("Comentarios: "+ comentario)
        if comentario == 'Aprobado':
         if not documentos_aprobados:

            mensaje_error = "Todos los documentos deben estar aprobados antes de aprobar al candidato."
            return render(request, 'Revicion del Ople/editar.html', {'formulario': formulario, 'anio': anio, 'nombrecargo': nombrecargo, 'nombre_partido': nombre_partido,  'idcand': idcand, 'eleccion': eleccion, 'mensaje_error': mensaje_error, 'titulo': titulo, **context})
         else:
            formulario.save()
            return redirect('RevicionOple')
        else:
            formulario.save()
            return redirect('RevicionOple')

    return render(request, 'Revicion del Ople/editar.html', {'formulario': formulario, 'anio': anio, 'nombrecargo': nombrecargo, 'nombre_partido': nombre_partido, 'idcand': idcand, 'eleccion': eleccion, 'titulo': titulo, **context})



def Editar_Co(request, id, anio,nombreeleccion,nombrecargo):
  
    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto        
    candidato = Candidatos.objects.get(id_cand=id)  # Reemplaza 1 con el ID que estás buscando
    # Verifica si el valor de 'aprobado' es "SI"
    if candidato.aprobado == "SI":
        # Hacer algo si 'aprobado' es "SI"
        print("El candidato está aprobado.")
        aprobado = True
        formulario = CandidatosFormMY_Propietario(request.POST or None, 
                             instance=candidato, readonly_mode=True)
    elif candidato.aprobado == "NO":
        # Hacer algo si 'aprobado' es "NO"
        print("El candidato no está aprobado.")
        aprobado = False
        formulario = CandidatosFormMY_Propietario(request.POST or None, 
                             instance=candidato)
    else:
        # Hacer algo si 'aprobado' no es ni "SI" ni "NO"
        print("El estado de aprobación es desconocido.")
        formulario = CandidatosFormMY_Propietario(request.POST or None, 
                             instance=candidato)
    

    if formulario.is_valid() and request.POST:
     formulario.save()
     print(candidato.idprinc.idprinc)
 
     if candidato.idprinc.idprinc == 'MY':
      return redirect('regicaMY')
     elif candidato.idprinc.idprinc == 'RP':
      return redirect('regicanRP')

    return render(request, 'Registro_de Cadndidaturas_RP/editar.html', {'formulario': formulario, 'anio': anio, 'nombrecargo': nombrecargo, 'nombre_partido': nombre_partido, 'aprobado': aprobado, **context})



def Editar_Co_Suplente_Ople(request, id, anio,nombreeleccion,nombrecargo):
  
    idcand=id
    eleccion=nombreeleccion
    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto        
    candidato = Candidatos.objects.get(id_cand=id)  # Reemplaza 1 con el ID que estás buscando
    titulo= "Candidato Suplente"
    titulopro= candidato.id_propietario

    # Verificar si todos los documentos relacionados están aprobados
    documentos = DocumentosCandidatos.objects.filter(id_cand=id)
    documentos_aprobados = all(doc.estatus_revicion == 'Aprobado' for doc in documentos)

    formulario = CandidatosFormMY_Suplente_Ople(request.POST or None, 
                             instance=candidato, candidato_id=candidato.id_propietario)
 
    if formulario.is_valid() and request.POST:
        comentario = formulario.cleaned_data['comentarios']
        print("Comentarios: "+ comentario)
        if comentario == 'Aprobado':
         if not documentos_aprobados:

            mensaje_error = "Todos los documentos deben estar aprobados antes de aprobar al candidato."
            return render(request, 'Revicion del Ople/editar.html', {'formulario': formulario, 'anio': anio, 'nombrecargo': nombrecargo, 'nombre_partido': nombre_partido,  'idcand': idcand, 'eleccion': eleccion, 'mensaje_error': mensaje_error, 'titulo': titulo, **context})
         else:
            formulario.save()
            return redirect('RevicionOple')
        else:
            formulario.save()
            return redirect('RevicionOple')

    return render(request, 'Revicion del Ople/editar.html', {'formulario': formulario, 'anio': anio, 'nombrecargo': nombrecargo, 'nombre_partido': nombre_partido, 'idcand': idcand, 'eleccion': eleccion, 'titulo': titulo, 'titulopro': titulopro, **context})


def Editar_Co_Suplente(request, id, anio,nombreeleccion,nombrecargo):
  
    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido

    candidato = Candidatos.objects.get(id_cand=id)  # Reemplaza 1 con el ID que estás buscando
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

    candidato = get_object_or_404(Candidatos, id_cand =id)
    # Verifica si el valor de 'aprobado' es "SI"
    if candidato.aprobado == "SI":
        # Hacer algo si 'aprobado' es "SI"
        print("El candidato está aprobado.")
        aprobado = True
        formulario = CandidatosFormMY_Suplente(request.POST or None, 
                             instance=candidato, readonly_mode=True, initial={'candidato_id': candidato.id_propietario})
    elif candidato.aprobado == "NO":
        # Hacer algo si 'aprobado' es "NO"
        print("El candidato no está aprobado.")
        aprobado = False
        formulario = CandidatosFormMY_Suplente(request.POST or None, 
                             instance=candidato, initial={'candidato_id': candidato.id_propietario})
    else:
        # Hacer algo si 'aprobado' no es ni "SI" ni "NO"
        print("El estado de aprobación es desconocido.")
        formulario = CandidatosFormMY_Suplente(request.POST or None, 
                             instance=candidato, initial={'candidato_id': candidato.id_propietario})


    if formulario.is_valid() and request.POST:
     formulario.save()
     if candidato.idprinc.idprinc == 'MY':
      return redirect('regicaMY')
     elif candidato.idprinc.idprinc == 'RP':
      return redirect('regicanRP')   

    return render(request, 'Registro_de Cadndidaturas_RP/editar.html', {'formulario': formulario, 'anio': anio, 'nombrecargo': nombrecargo, 'nombre_partido': nombre_partido, 'aprobado': aprobado, **context})



def Editar_Ay(request, id, anio,nombreeleccion,nombrecargo):
  
    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

    candidato = Candidatos.objects.get(id_cand=id)  # Reemplaza 1 con el ID que estás buscando
    candidato = get_object_or_404(Candidatos, id_cand =id)
    # Verifica si el valor de 'aprobado' es "SI"
    if candidato.aprobado == "SI":
        # Hacer algo si 'aprobado' es "SI"
        print("El candidato está aprobado.")
        aprobado = True
        formulario = CandidatosForm(request.POST or None, 
                             instance=candidato, readonly_mode=True)
    elif candidato.aprobado == "NO":
        # Hacer algo si 'aprobado' es "NO"
        print("El candidato no está aprobado.")
        aprobado = False
        formulario = CandidatosForm(request.POST or None, 
                             instance=candidato)
    else:
        # Hacer algo si 'aprobado' no es ni "SI" ni "NO"
        print("El estado de aprobación es desconocido.")
        formulario = CandidatosForm(request.POST or None, 
                             instance=candidato)
    

    if formulario.is_valid() and request.POST:
     formulario.save()
     return redirect('regican')

    return render(request, 'registro_de_candidatura/editar.html', {'formulario': formulario, 'anio': anio, 'nombrecargo': nombrecargo, 'nombre_partido': nombre_partido, 'aprobado': aprobado, **context})





def Editar_Ay_Suplente_Ople(request, id, anio,nombreeleccion,nombrecargo):
    idcand=id
    eleccion=nombreeleccion
    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

    candidato = Candidatos.objects.get(id_cand=id)  # Reemplaza 1 con el ID que estás buscando
    candidato = get_object_or_404(Candidatos, id_cand =id)
    titulo= "Candidato Suplente"
    # Verificar si todos los documentos relacionados están aprobados
    documentos = DocumentosCandidatos.objects.filter(id_cand=id)
    documentos_aprobados = all(doc.estatus_revicion == 'Aprobado' for doc in documentos)
    idpropietario = candidato.id_propietario

    formulario = CandidatosFormSuplenteOple(request.POST or None, instance=candidato, candidato_id=idpropietario)

 
    if formulario.is_valid() and request.POST:
        comentario = formulario.cleaned_data['comentarios']
        print("Comentarios: "+ comentario)
        if comentario == 'Aprobado':
         if not documentos_aprobados:

            mensaje_error = "Todos los documentos deben estar aprobados antes de aprobar al candidato."
            return render(request, 'Revicion del Ople/editar.html', {'formulario': formulario, 'anio': anio, 'nombrecargo': nombrecargo, 'nombre_partido': nombre_partido,  'idcand': idcand, 'eleccion': eleccion, 'mensaje_error': mensaje_error, 'titulo': titulo, **context})
         else:
            formulario.save()
            return redirect('RevicionOple')
        else:
            formulario.save()
            return redirect('RevicionOple')

    return render(request, 'Revicion del Ople/editar.html', {'formulario': formulario, 'anio': anio, 'nombrecargo': nombrecargo, 'nombre_partido': nombre_partido, 'idcand': idcand, 'eleccion': eleccion, 'titulo': titulo, **context})




def Editar_Ay_Suplente(request, id, anio,nombreeleccion,nombrecargo):
  
    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

    candidato = Candidatos.objects.get(id_cand=id)  # Reemplaza 1 con el ID que estás buscando

    candidato = get_object_or_404(Candidatos, id_cand =id)
    # Verifica si el valor de 'aprobado' es "SI"
    if candidato.aprobado == "SI":
        # Hacer algo si 'aprobado' es "SI"
        print("El candidato está aprobado.")
        aprobado = True
        formulario = CandidatosFormSuplente(request.POST or None, 
                             instance=candidato, readonly_mode=True, candidato_id=candidato.id_propietario)
    elif candidato.aprobado == "NO":
        # Hacer algo si 'aprobado' es "NO"
        print("El candidato no está aprobado.")
        aprobado = False
        formulario = CandidatosFormSuplente(request.POST or None, 
                             instance=candidato, candidato_id=candidato.id_propietario)
    else:
        # Hacer algo si 'aprobado' no es ni "SI" ni "NO"
        print("El estado de aprobación es desconocido.")
        formulario = CandidatosFormSuplente(request.POST or None, 
                             instance=candidato, candidato_id=candidato.id_propietario)


    if formulario.is_valid() and request.POST:
     formulario.save()
     return redirect('regican')

    return render(request, 'registro_de_candidatura/Editar_Suplente.html', {'formulario': formulario, 'anio': anio, 'nombrecargo': nombrecargo, 'nombre_partido': nombre_partido, 'aprobado': aprobado, **context})




def agregar_AY_Propietario(request, anio, nombreeleccion, nombrecargo, tipo, idpropietario, titulo):
    estado_id = request.session['ID_ESTADO']
    fecha_hora_actual_python = timezone.now()
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido
    eleccion = get_object_or_404(Procesos, descrip=nombreeleccion, idestado=estado_id)
    cargo = get_object_or_404(Tipocargo, descrip_tcargo=nombrecargo)
    print(eleccion.idproceso)
    print(cargo.idtipo_cargo)
    print(idpartido)
   
    print ("HOla es procesos: "+str(eleccion.idproceso))
    print ("HOla es el estado: "+str(estado_id))

    idprocesopart = get_object_or_404(PartidosCoaliciones, idpartido=idpartido, idestado=estado_id)

    print ("HOla es coaliciones: "+str(idprocesopart.idprocesopartido.idprocesopartido))
 
    formulario = CandidatosFormMY_Propietario(initial={'idestado': estado_id, 'idprocesopartido': idprocesopart.idprocesopartido.idprocesopartido,}, estado_id=estado_id)
    Estatus = "Falatante";
    CapturaOple = "Pendiente";


    try:
      
            if request.method == 'POST':
                formulario = CandidatosFormMY_Propietario(request.POST)
                if formulario.is_valid():
                    procesopartido = formulario.cleaned_data['idprocesopartido']
                    estado = formulario.cleaned_data['idestado']
                    distrito = formulario.cleaned_data['iddistrito']
                    estadonacimiento = formulario.cleaned_data['idestado']
                    

                    Candidato = formulario.save(commit=False)

                    Candidato.tipo = tipo
                    Candidato.fecha_de_captura = fecha_hora_actual_python
                    Candidato.anio = anio
                    Candidato.idpartido = partido

                    Candidato.registrado = "SI"
                    Candidato.verificado = "NO"
                    Candidato.aprobado = "NO"
              
      

                    Candidato.idproceso_id = eleccion.idproceso
                    Candidato.idprocesopartido_id = procesopartido.idprocesopartido
                    Candidato.idtipo_cargo_id = cargo.idtipo_cargo
                    Candidato.idestado_id = estado.idestado
                    
                    Candidato.iddistrito_id = distrito.iddistrito
                    Candidato.idestado_nacimiento_id = estadonacimiento.idestado
                    formulario.save()
                                    # Obtener el id_cand máximo
                max_id_cand = Candidatos.objects.all().aggregate(Max('id_cand'))
                nuevo_id_cand = max_id_cand['id_cand__max']

                # Obtener los resultados de documentos
                resultados = DocCandidatos.objects.filter(idproceso=eleccion.idproceso).values_list('idtipo_doc', flat=True)

                # Obtener instancias de Tipodoc según los resultados
                tipos_documentos = Tipodoc.objects.filter(idtipo_doc__in=resultados)

                # Crear instancias de DocumentosCandidatos y asignar la instancia de Candidatos
                documentos = [
                         DocumentosCandidatos(id_cand=Candidato, idproceso=eleccion, idtipo_doc=tipo_doc, estatus="Faltante", estatus_revicion="Pendiente")
                         for tipo_doc in tipos_documentos
                            ]

                DocumentosCandidatos.objects.bulk_create(documentos)


                return redirect('regican')
        
    except IntegrityError as e:
        print(f"Error de integridad al guardar el formulario: {e}")
    except ValidationError as e:
        print(f"Error de validación al guardar el formulario: {e}")
    except Exception as e:
        print(f"Error general al guardar el formulario: {e}")

    return render(request, 'regsitro_de_diputaciones_my/crear.html', {'formulario': formulario, 'anio': anio, 'nombreeleccion': nombreeleccion, 'nombrecargo': nombrecargo, 'nombre_partido': nombre_partido, 'tipo': tipo, 'titulo': titulo, **context})



def agregar_CO_MY_Propietario(request, anio, nombreeleccion, nombrecargo, tipo, idpropietario, titulo, distrito):
    estado_id = request.session['ID_ESTADO']
    fecha_hora_actual_python = timezone.now()
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido
    eleccion = get_object_or_404(Procesos, descrip=nombreeleccion, idestado=estado_id)
    cargo = get_object_or_404(Tipocargo, descrip_tcargo=nombrecargo)

   
    print ("HOla es procesos: "+str(eleccion.idproceso))
    print ("HOla es el estado: "+str(estado_id))

    idprocesopart = PartidosCoaliciones.objects.filter(idpartido=idpartido, idestado=estado_id, anio=anio).first()

    print ("HOla es coaliciones: "+str(idprocesopart.idprocesopartido.idprocesopartido))

 
    formulario = CandidatosFormMY_Propietario(initial={'idestado': estado_id, 'idprocesopartido': idprocesopart.idprocesopartido.idprocesopartido,'iddistrito':distrito }, estado_id=estado_id)
    Estatus = "Falatante";
    CapturaOple = "Pendiente";


    try:
      
            if request.method == 'POST':
                formulario = CandidatosFormMY_Propietario(request.POST)
                if formulario.is_valid():
                    procesopartido = formulario.cleaned_data['idprocesopartido']
                    estado = formulario.cleaned_data['idestado']
                    distrito = formulario.cleaned_data['iddistrito']
                    estadonacimiento = formulario.cleaned_data['idestado']
                    num_elect= Procesoscargo.objects.get(idproceso=eleccion.idproceso, idtipo_cargo=2, idDistrito=distrito)
                    principio = Principio.objects.get(idprinc='MY')

                    Candidato = formulario.save(commit=False)

                    Candidato.tipo = tipo
                    Candidato.fecha_de_captura = fecha_hora_actual_python
                    Candidato.anio = anio
                    Candidato.idpartido = partido

                    Candidato.registrado = "SI"
                    Candidato.verificado = "NO"
                    Candidato.aprobado = "NO"
                    Candidato.idprinc=principio
      

                    Candidato.idproceso_id = eleccion.idproceso
                    Candidato.idprocesopartido_id = procesopartido.idprocesopartido
                    Candidato.idtipo_cargo_id = cargo.idtipo_cargo
                    Candidato.idestado_id = estado.idestado
                    
                    Candidato.iddistrito_id = distrito.iddistrito
                    Candidato.idestado_nacimiento_id = estadonacimiento.idestado
                    Candidato.num_elec=num_elect
                    formulario.save()
                                    # Obtener el id_cand máximo
                max_id_cand = Candidatos.objects.all().aggregate(Max('id_cand'))
                nuevo_id_cand = max_id_cand['id_cand__max']

                # Obtener los resultados de documentos
                resultados = DocCandidatos.objects.filter(idproceso=eleccion.idproceso).values_list('idtipo_doc', flat=True)

                # Obtener instancias de Tipodoc según los resultados
                tipos_documentos = Tipodoc.objects.filter(idtipo_doc__in=resultados)

                # Crear instancias de DocumentosCandidatos y asignar la instancia de Candidatos
                documentos = [
                         DocumentosCandidatos(id_cand=Candidato, idproceso=eleccion, idtipo_doc=tipo_doc, estatus="Faltante", estatus_revicion="Pendiente")
                         for tipo_doc in tipos_documentos
                            ]

                DocumentosCandidatos.objects.bulk_create(documentos)


                return redirect('regicaMY')
        
    except IntegrityError as e:
        print(f"Error de integridad al guardar el formulario: {e}")
    except ValidationError as e:
        print(f"Error de validación al guardar el formulario: {e}")
    except Exception as e:
        print(f"Error general al guardar el formulario: {e}")

    return render(request, 'regsitro_de_diputaciones_my/crear.html', {'formulario': formulario, 'anio': anio, 'nombreeleccion': nombreeleccion, 'nombrecargo': nombrecargo, 'nombre_partido': nombre_partido, 'tipo': tipo, 'titulo': titulo, **context})




def agregar_CO_RP_Propietario(request, anio, nombreeleccion, nombrecargo, tipo, idpropietario, titulo, distrito):
    estado_id = request.session['ID_ESTADO']
    fecha_hora_actual_python = timezone.now()

    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
    principio = Principio.objects.get(idprinc='RP')
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto


    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido

    cargo = get_object_or_404(Tipocargo, descrip_tcargo=nombrecargo)
    eleccion = get_object_or_404(Procesos, descrip=nombreeleccion, idestado=estado_id)
    
    print ("HOla es procesos: "+str(eleccion.idproceso))
    print ("HOla es el estado: "+str(estado_id))

    idprocesopart = PartidosCoaliciones.objects.filter(idpartido=idpartido, idestado=estado_id, anio=anio).first()

  
    formulario = CandidatosFormMY_Propietario(initial={'idestado': estado_id, 'idprocesopartido': idprocesopart.idprocesopartido.idprocesopartido, 'iddistrito':distrito }, estado_id=estado_id)
    Estatus = "Falatante";
    CapturaOple = "Pendiente";


    try:
      
            if request.method == 'POST':
                formulario = CandidatosFormMY_Propietario(request.POST)
                if formulario.is_valid():
                    procesopartido = formulario.cleaned_data['idprocesopartido']
                    estado = formulario.cleaned_data['idestado']
                    distritos = formulario.cleaned_data['iddistrito']
                    
                    paridad = formulario.cleaned_data['idparidad']
                    estadonacimiento = formulario.cleaned_data['idestado']
                    num_elect= Procesoscargo.objects.get(idproceso=eleccion.idproceso, idtipo_cargo=2, idDistrito=distrito)
                    Candidato = formulario.save(commit=False)

                    Candidato.tipo = tipo
                    Candidato.fecha_de_captura = fecha_hora_actual_python
                    Candidato.anio = anio
                    Candidato.idpartido = partido

                    Candidato.registrado = "SI"
                    Candidato.verificado = "NO"
                    Candidato.aprobado = "NO"

                    Candidato.idproceso_id = eleccion.idproceso
                    Candidato.idprocesopartido_id = procesopartido.idprocesopartido
                    Candidato.idtipo_cargo_id = cargo.idtipo_cargo
                    Candidato.idprinc = principio
                    Candidato.idparidad_id = paridad.idparidad
                    Candidato.idestado_id = estado.idestado
                    Candidato.iddistrito_id = distritos.iddistrito
                    Candidato.idestado_nacimiento_id = estadonacimiento.idestado
                    Candidato.num_elec=num_elect
                    formulario.save()
                                    # Obtener el id_cand máximo
                max_id_cand = Candidatos.objects.all().aggregate(Max('id_cand'))
                nuevo_id_cand = max_id_cand['id_cand__max']

                # Obtener los resultados de documentos
                resultados = DocCandidatos.objects.filter(idproceso=eleccion.idproceso).values_list('idtipo_doc', flat=True)

                # Obtener instancias de Tipodoc según los resultados
                tipos_documentos = Tipodoc.objects.filter(idtipo_doc__in=resultados)

                # Crear instancias de DocumentosCandidatos y asignar la instancia de Candidatos
                documentos = [
                         DocumentosCandidatos(id_cand=Candidato, idproceso=eleccion, idtipo_doc=tipo_doc, estatus="Faltante", estatus_revicion="Pendiente")
                         for tipo_doc in tipos_documentos
                            ]

                DocumentosCandidatos.objects.bulk_create(documentos)


                return redirect('regicanRP')
        
    except IntegrityError as e:
        print(f"Error de integridad al guardar el formulario: {e}")
    except ValidationError as e:
        print(f"Error de validación al guardar el formulario: {e}")
    except Exception as e:
        print(f"Error general al guardar el formulario: {e}")

    return render(request, 'Registro_de Cadndidaturas_RP/crear.html', {'formulario': formulario, 'anio': anio, 'nombreeleccion': nombreeleccion, 'nombrecargo': nombrecargo, 'nombre_partido': nombre_partido, 'tipo': tipo, 'titulo': titulo, 'distrito': distrito, **context})





def agregar_CO_MY_Suplente(request , anio, nombreeleccion, nombrecargo, tipo, idpropietario, titulo, distrito):
    estado_id = request.session['ID_ESTADO']
    fecha_hora_actual_python = timezone.now()

    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido

    cargo = get_object_or_404(Tipocargo, descrip_tcargo=nombrecargo)
    eleccion = get_object_or_404(Procesos, descrip=nombreeleccion, idestado=estado_id)
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])
    num_elect= Procesoscargo.objects.get(idproceso=eleccion.idproceso, idtipo_cargo=2, idDistrito=distrito)
    #fprint("PRUEBA CON: "+str(num_elect.num_elec))

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion      
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto    
    principio = Principio.objects.get(idprinc='MY')
    print ("HOla es procesos: "+str(eleccion.idproceso))
    print ("HOla es el estado: "+str(estado_id))

    idprocesopart = PartidosCoaliciones.objects.filter(idpartido=idpartido, idestado=estado_id, anio=anio).first()

    print ("HOla es coaliciones: "+str(idprocesopart.idprocesopartido.idprocesopartido))

    if  idpropietario == 0:
       
        formulario = CandidatosFormMY_Suplente(initial={'idestado': estado_id, 'iddistrito': distrito}, estado_id=estado_id, num_elect=num_elect.num_elec, idpartido=idpartido, principio='MY')
        
    elif idpropietario != 0:
        Propietario = get_object_or_404(Candidatos, id_cand=idpropietario)
        formulario = CandidatosFormMY_Suplente(initial={'idestado': estado_id, 'id_propietario': Propietario.id_cand, 'genero': Propietario.genero, 'idprocesopartido': Propietario.idprocesopartido, 'iddistrito': Propietario.iddistrito}, estado_id=estado_id, idpartido=idpartido, principio='MY')
 
    try:
       
            if request.method == 'POST':
                formulario = CandidatosFormMY_Suplente(request.POST)
                if formulario.is_valid():
                    procesopartido = formulario.cleaned_data['idprocesopartido']
                    estado = formulario.cleaned_data['idestado']
                    distritos = formulario.cleaned_data['iddistrito']
                    paridad = formulario.cleaned_data['idparidad']
                    estadonacimiento = formulario.cleaned_data['idestado']
                    



                    Candidato = formulario.save(commit=False)

                    Candidato.id_propietario_id = idpropietario
                    Candidato.tipo = tipo
                    Candidato.fecha_de_captura = fecha_hora_actual_python
                    Candidato.anio = anio
                    Candidato.idpartido = partido

                    Candidato.registrado = "SI"
                    Candidato.verificado = "NO"
                    Candidato.aprobado = "NO"

                    Candidato.idproceso_id = eleccion.idproceso
                    Candidato.idprocesopartido_id = procesopartido.idprocesopartido
                    Candidato.idtipo_cargo_id = cargo.idtipo_cargo
                    Candidato.idestado_id = estado.idestado
                    Candidato.idprinc = principio
                    Candidato.idparidad_id = paridad.idparidad
                    Candidato.iddistrito_id = distritos.iddistrito
                    Candidato.idestado_nacimiento_id = estadonacimiento.idestado
                    Candidato.num_elec= Propietario.num_elec
                    Candidato.save()

                                    # Obtener el id_cand máximo
                max_id_cand = Candidatos.objects.all().aggregate(Max('id_cand'))
                nuevo_id_cand = max_id_cand['id_cand__max']

                # Obtener los resultados de documentos
                resultados = DocCandidatos.objects.filter(idproceso=eleccion.idproceso).values_list('idtipo_doc', flat=True)

                # Obtener instancias de Tipodoc según los resultados
                tipos_documentos = Tipodoc.objects.filter(idtipo_doc__in=resultados)

                # Crear instancias de DocumentosCandidatos y asignar la instancia de Candidatos
                documentos = [
                         DocumentosCandidatos(id_cand=Candidato, idproceso=eleccion, idtipo_doc=tipo_doc, estatus="Faltante", estatus_revicion="Pendiente")
                         for tipo_doc in tipos_documentos
                            ]

                DocumentosCandidatos.objects.bulk_create(documentos)
                return redirect('regicaMY')
                

    except IntegrityError as e:
        print(f"Error de integridad al guardar el formulario S: {e}")
    except ValidationError as e:
        print(f"Error de validación al guardar el formularioc S: {e}")
    except Exception as e:
        print(f"Error general al guardar el formulario S: {e}")

    return render(request, 'regsitro_de_diputaciones_my/Crear_Suplente.html', {'formulario': formulario, 'anio': anio, 'nombreeleccion': nombreeleccion, 'nombrecargo': nombrecargo, 'nombre_partido': nombre_partido, 'tipo': tipo, 'titulo': titulo, 'distrito':distrito, **context})




def agregar_CO_RP_Suplente(request , anio, nombreeleccion, nombrecargo, tipo, idpropietario, titulo, distrito):
    estado_id = request.session['ID_ESTADO']
    fecha_hora_actual_python = timezone.now()

    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido

    cargo = get_object_or_404(Tipocargo, descrip_tcargo=nombrecargo)
    eleccion = get_object_or_404(Procesos, descrip=nombreeleccion, idestado=estado_id)
    num_elect= Procesoscargo.objects.get(idproceso=eleccion.idproceso, idtipo_cargo=2, idDistrito=distrito)

    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion      
    principio = Principio.objects.get(idprinc='RP')
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

    print ("HOla es procesos: "+str(eleccion.idproceso))
    print ("HOla es el estado: "+str(estado_id))

    idprocesopart = PartidosCoaliciones.objects.filter(idpartido=idpartido, idestado=estado_id, anio=anio).first()

    print ("HOla es coaliciones: "+str(idprocesopart.idprocesopartido.idprocesopartido))

    if  idpropietario == 0:
       
        formulario = CandidatosFormMY_Suplente(initial={'idestado': estado_id, 'idprocesopartido':idprocesopart.idprocesopartido.idprocesopartido}, estado_id=estado_id, num_elect=num_elect, idpartido=idpartido,  principio='RP')
        
    elif idpropietario != 0:
        Propietario = get_object_or_404(Candidatos, id_cand=idpropietario)
        formulario = CandidatosFormMY_Suplente(initial={'idestado': estado_id, 'id_propietario': Propietario.id_cand, 'genero': Propietario.genero, 'idprocesopartido': Propietario.idprocesopartido, 'iddistrito': Propietario.iddistrito}, estado_id=estado_id, num_elect=num_elect, idpartido=idpartido,  principio='RP')
 
    try:
       
            if request.method == 'POST':
                formulario = CandidatosFormMY_Suplente(request.POST)
                if formulario.is_valid():
                    procesopartido = formulario.cleaned_data['idprocesopartido']
                    estado = formulario.cleaned_data['idestado']
                    distritos = formulario.cleaned_data['iddistrito']
                    paridad = formulario.cleaned_data['idparidad']
                    estadonacimiento = formulario.cleaned_data['idestado']
                   


                    Candidato = formulario.save(commit=False)

                    Candidato.id_propietario_id = idpropietario
                    Candidato.tipo = tipo
                    Candidato.fecha_de_captura = fecha_hora_actual_python
                    Candidato.anio = anio
                    Candidato.idpartido = partido

                    Candidato.registrado = "SI"
                    Candidato.verificado = "NO"
                    Candidato.aprobado = "NO"

                    Candidato.idproceso_id = eleccion.idproceso
                    Candidato.idprocesopartido_id = procesopartido.idprocesopartido
                    Candidato.idtipo_cargo_id = cargo.idtipo_cargo
                    Candidato.idestado_id = estado.idestado
                    Candidato.idprinc = principio
                    Candidato.idparidad_id = paridad.idparidad
                    Candidato.iddistrito_id = distritos.iddistrito
                    Candidato.idestado_nacimiento_id = estadonacimiento.idestado
                    Candidato.num_elec=Propietario.num_elec
                    Candidato.save()

                                    # Obtener el id_cand máximo
                max_id_cand = Candidatos.objects.all().aggregate(Max('id_cand'))
                nuevo_id_cand = max_id_cand['id_cand__max']

                # Obtener los resultados de documentos
                resultados = DocCandidatos.objects.filter(idproceso=eleccion.idproceso).values_list('idtipo_doc', flat=True)

                # Obtener instancias de Tipodoc según los resultados
                tipos_documentos = Tipodoc.objects.filter(idtipo_doc__in=resultados)

                # Crear instancias de DocumentosCandidatos y asignar la instancia de Candidatos
                documentos = [
                         DocumentosCandidatos(id_cand=Candidato, idproceso=eleccion, idtipo_doc=tipo_doc, estatus="Faltante", estatus_revicion="Pendiente")
                         for tipo_doc in tipos_documentos
                            ]

                DocumentosCandidatos.objects.bulk_create(documentos)
                return redirect('regicanRP')
                

    except IntegrityError as e:
        print(f"Error de integridad al guardar el formulario S: {e}")
    except ValidationError as e:
        print(f"Error de validación al guardar el formularioc S: {e}")
    except Exception as e:
        print(f"Error general al guardar el formulario S: {e}")

    return render(request, 'Registro_de Cadndidaturas_RP/Crear_Suplente.html', {'formulario': formulario, 'anio': anio, 'nombreeleccion': nombreeleccion, 'nombrecargo': nombrecargo, 'nombre_partido': nombre_partido, 'tipo': tipo, 'titulo': titulo, 'distrito':distrito, **context})




def agregar_AY_sinfromula(request, anio, nombreeleccion, nombrecargo, tipo, municipio):
    estado_id = request.session['ID_ESTADO']
    fecha_hora_actual_python = timezone.now()
    print(nombreeleccion)
    print(nombrecargo)

    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido

    cargo = get_object_or_404(Tipocargo, descrip_tcargo=nombrecargo)
    eleccion = get_object_or_404(Procesos, descrip=nombreeleccion, idestado=estado_id)
    print ("HOla es procesos: "+str(eleccion.idproceso))
    print ("HOla es el estado: "+str(estado_id))
  
    #idprocesopart = get_object_or_404(PartidosCoaliciones, idpartido=idpartido, idestado=estado_id, anio=anio)
    idprocesopart = PartidosCoaliciones.objects.filter(idpartido=idpartido, idestado=estado_id, anio=anio).first()
    print ("HOla es coaliciones: "+str(idprocesopart.idprocesopartido.idprocesopartido))
 
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])
    formulario = CandidatosForm(initial={'idestado': estado_id, 'idprocesopartido': idprocesopart.idprocesopartido.idprocesopartido, 'idmunicipio':municipio}, estado_id=estado_id )
    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
    try:
        if request.method == 'POST':
            formulario = CandidatosForm(request.POST)
            if formulario.is_valid():
                procesopartido = formulario.cleaned_data['idprocesopartido']
                estado = formulario.cleaned_data['idestado']
                municipio = formulario.cleaned_data['idmunicipio']
                estado_nacimiento = formulario.cleaned_data['idestado_nacimiento']
                num_elect= Procesoscargo.objects.get(idproceso=eleccion.idproceso, idtipo_cargo=1, idMunicipio=municipio)


                # Crear instancia de Candidatos y guardarla
                candidato = formulario.save(commit=False)
                candidato.tipo = tipo
                candidato.fecha_de_captura = fecha_hora_actual_python
                candidato.anio = anio
                candidato.idpartido = partido
                candidato.registrado = "SI"
                candidato.verificado = "NO"
                candidato.aprobado = "NO"
                candidato.idproceso_id = eleccion.idproceso
                candidato.idprocesopartido_id = procesopartido.idprocesopartido
                candidato.idtipo_cargo_id = cargo.idtipo_cargo
                candidato.idestado_id = estado.idestado
                candidato.idmunicipio_id = municipio.idmunicipio
                candidato.idestado_nacimiento_id = estado_nacimiento.idestado
                candidato.num_elec=num_elect
                candidato.save()

                # Obtener el id_cand máximo
                max_id_cand = Candidatos.objects.all().aggregate(Max('id_cand'))
                nuevo_id_cand = max_id_cand['id_cand__max']

                # Obtener los resultados de documentos
                resultados = DocCandidatos.objects.filter(idproceso=eleccion.idproceso).values_list('idtipo_doc', flat=True)

                # Obtener instancias de Tipodoc según los resultados
                tipos_documentos = Tipodoc.objects.filter(idtipo_doc__in=resultados)

                # Crear instancias de DocumentosCandidatos y asignar la instancia de Candidatos
                documentos = [
                         DocumentosCandidatos(id_cand=candidato, idproceso=eleccion, idtipo_doc=tipo_doc, estatus="Faltante", estatus_revicion="Pendiente")
                         for tipo_doc in tipos_documentos
                            ]

                DocumentosCandidatos.objects.bulk_create(documentos)


                return redirect('regican')
    except IntegrityError as e:
        print(f"Error de integridad al guardar el formulario: {e}")
    except ValidationError as e:
        print(f"Error de validación al guardar el formulario: {e}")
    except Exception as e:
        print(f"Error general al guardar el formulario: {e}")

    return render(request, 'registro_de_candidatura/crear sin formela.html', {'formulario': formulario, 'anio': anio, 'nombreeleccion': nombreeleccion, 'nombrecargo': nombrecargo, 'nombre_partido': nombre_partido, 'tipo': tipo, **context})



def agregar_GU_sinfromula(request, anio, nombreeleccion, nombrecargo, tipo, idpropietario):
    estado_id = request.session['ID_ESTADO']
    fecha_hora_actual_python = timezone.now()

    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion      

    cargo = get_object_or_404(Tipocargo, descrip_tcargo=nombrecargo)
    eleccion = get_object_or_404(Procesos, descrip=nombreeleccion, idestado=estado_id)
    print ("HOla es procesos: "+str(eleccion.idproceso))
    idprocesopart = PartidosCoaliciones.objects.filter(idpartido=idpartido, idestado=estado_id, anio=anio).first()

    print ("HOla es: "+str(idprocesopart.idprocesopartido.idprocesopartido))
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
    formulario = CandidatosFormGU(initial={'idestado': estado_id, 'idprocesopartido': idprocesopart.idprocesopartido.idprocesopartido}, estado_id=estado_id)
    
    try:
        if request.method == 'POST':
            formulario = CandidatosFormGU(request.POST)
            if formulario.is_valid():
                procesopartido = formulario.cleaned_data['idprocesopartido']
                estado = formulario.cleaned_data['idestado']
                estado_nacimiento = formulario.cleaned_data['idestado']
                num_elect= Procesoscargo.objects.get(idproceso=eleccion.idproceso, idtipo_cargo=3)

                # Crear instancia de Candidatos y guardarla
                candidato = formulario.save(commit=False)
                candidato.tipo = tipo
                candidato.fecha_de_captura = fecha_hora_actual_python
                candidato.anio = anio
                candidato.idpartido = partido
                candidato.registrado = "SI"
                candidato.verificado = "NO"
                candidato.aprobado = "NO"
                candidato.idproceso_id = eleccion.idproceso
                candidato.idprocesopartido_id = procesopartido.idprocesopartido
                candidato.idtipo_cargo_id = cargo.idtipo_cargo
                candidato.idestado_id = estado.idestado
                candidato.idestado_nacimiento_id = estado_nacimiento.idestado
                candidato.num_elec=num_elect
                candidato.save()

                # Obtener el id_cand máximo
                max_id_cand = Candidatos.objects.all().aggregate(Max('id_cand'))
                nuevo_id_cand = max_id_cand['id_cand__max']

                # Obtener los resultados de documentos
                resultados = DocCandidatos.objects.filter(idproceso=eleccion.idproceso).values_list('idtipo_doc', flat=True)

                # Obtener instancias de Tipodoc según los resultados
                tipos_documentos = Tipodoc.objects.filter(idtipo_doc__in=resultados)

                # Crear instancias de DocumentosCandidatos y asignar la instancia de Candidatos
                documentos = [
                         DocumentosCandidatos(id_cand=candidato, idproceso=eleccion, idtipo_doc=tipo_doc, estatus="Faltante", estatus_revicion="Pendiente")
                         for tipo_doc in tipos_documentos
                            ]

                DocumentosCandidatos.objects.bulk_create(documentos)


                return redirect('regicangu')
    except IntegrityError as e:
        print(f"Error de integridad al guardar el formulario: {e}")
    except ValidationError as e:
        print(f"Error de validación al guardar el formulario: {e}")
    except Exception as e:
        print(f"Error general al guardar el formulario: {e}")

    return render(request, 'Regsitro_de_Gubernatura/crear sin formela.html', {'formulario': formulario, 'anio': anio, 'nombreeleccion': nombreeleccion, 'nombrecargo': nombrecargo, 'nombre_partido': nombre_partido, 'tipo': tipo, **context})



def agregar_AY_Suplente(request , anio, nombreeleccion, nombrecargo, tipo, idpropietario, titulo):
    estado_id = request.session['ID_ESTADO']
    fecha_hora_actual_python = timezone.now()
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
    cargo = get_object_or_404(Tipocargo, descrip_tcargo=nombrecargo)
    eleccion = get_object_or_404(Procesos, descrip=nombreeleccion, idestado=estado_id)
    print ("HOla es procesos: "+str(eleccion.idproceso))
    print ("HOla es el estado: "+str(estado_id))

    idprocesopart = get_object_or_404(PartidosCoaliciones, idproceso=eleccion.idproceso, idpartido=idpartido, idestado=estado_id)

    print ("HOla es coaliciones: "+str(idprocesopart.idprocesopartido.idprocesopartido))


    if  idpropietario == 0:
       
        formulario = CandidatosFormSuplente(initial={'idestado': estado_id,'idprocesopartido': idprocesopart.idprocesopartido.idprocesopartido}, estado_id=estado_id)
        
    elif idpropietario != 0:
        Propietario = get_object_or_404(Candidatos, id_cand=idpropietario)
        formulario = CandidatosFormSuplente(initial={'idestado': estado_id, 'id_propietario': Propietario.id_cand, 'genero': Propietario.genero, 'idprocesopartido': Propietario.idprocesopartido, 'idmunicipio': Propietario.idmunicipio}, estado_id=estado_id)
 
    try:
       
            if request.method == 'POST':
                formulario = CandidatosFormSuplente(request.POST)
                if formulario.is_valid():
                    procesopartido = formulario.cleaned_data['idprocesopartido']
                    estado = formulario.cleaned_data['idestado']
                    munucipio = formulario.cleaned_data['idmunicipio']
                    estadonacimiento = formulario.cleaned_data['idestado']
                   


                    Candidato = formulario.save(commit=False)

                    Candidato.id_propietario_id = idpropietario
                    Candidato.tipo = tipo
                    Candidato.fecha_de_captura = fecha_hora_actual_python
                    Candidato.anio = anio
                    Candidato.idpartido = partido

                    Candidato.registrado = "SI"
                    Candidato.verificado = "NO"
                    Candidato.aprobado = "NO"

                    Candidato.idproceso_id = eleccion.idproceso
                    Candidato.idprocesopartido_id = procesopartido.idprocesopartido
                    Candidato.idtipo_cargo_id = cargo.idtipo_cargo
                    Candidato.idestado_id = estado.idestado
                    Candidato.idmunicipio_id = munucipio.idmunicipio
                    Candidato.idestado_nacimiento_id = estadonacimiento.idestado
                   
                    Candidato.save()

                                    # Obtener el id_cand máximo
                max_id_cand = Candidatos.objects.all().aggregate(Max('id_cand'))
                nuevo_id_cand = max_id_cand['id_cand__max']

                # Obtener los resultados de documentos
                resultados = DocCandidatos.objects.filter(idproceso=eleccion.idproceso).values_list('idtipo_doc', flat=True)

                # Obtener instancias de Tipodoc según los resultados
                tipos_documentos = Tipodoc.objects.filter(idtipo_doc__in=resultados)

                # Crear instancias de DocumentosCandidatos y asignar la instancia de Candidatos
                documentos = [
                         DocumentosCandidatos(id_cand=Candidato, idproceso=eleccion, idtipo_doc=tipo_doc, estatus="Faltante", estatus_revicion="Pendiente")
                         for tipo_doc in tipos_documentos
                            ]

                DocumentosCandidatos.objects.bulk_create(documentos)
                return redirect('regican')
                

    except IntegrityError as e:
        print(f"Error de integridad al guardar el formulario S: {e}")
    except ValidationError as e:
        print(f"Error de validación al guardar el formularioc S: {e}")
    except Exception as e:
        print(f"Error general al guardar el formulario S: {e}")

    return render(request, 'registro_de_candidatura/Crear_Suplente.html', {'formulario': formulario, 'anio': anio, 'nombreeleccion': nombreeleccion, 'nombrecargo': nombrecargo, 'nombre_partido': nombre_partido, 'tipo': tipo, 'titulo': titulo, **context})




def documentos_candidatos(request, id, nombreeleccion, nombrecargo):
    # Llamada al procedimiento almacenado
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion      
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

    with connection.cursor() as cursor:
        try:
            cursor.callproc('obtener_documentos_candidatos', [id])
            # Recuperar los resultados del procedimiento almacenado
            resultados = cursor.fetchall()
        except Exception as e:
            print(f"Error al llamar al procedimiento almacenado: {e}")
            resultados = []

    # Obtener el objeto Candidatos correspondiente al id
    candidato = get_object_or_404(Candidatos, id_cand=id)

    # Pasa el nombre completo del candidato a la plantilla
    nombre_completo = f"{candidato.nombres} {candidato.apaterno} {candidato.amaterno}"

    return render(request, 'registro_de_candidatura/Documentos.html', {'documentos_mostrar': resultados, 'nombreeleccion': nombreeleccion, 'nombrecargo': nombrecargo , 'nombre_completo': nombre_completo, 'id':id, **context})




def documentos_candidatosOple(request, id, nombreeleccion, nombrecargo, anio):
    # Llamada al procedimiento almacenado
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido


    with connection.cursor() as cursor:
        try:
            cursor.callproc('obtener_documentos_candidatos', [id])
            # Recuperar los resultados del procedimiento almacenado
            resultados = cursor.fetchall()
        except Exception as e:
            print(f"Error al llamar al procedimiento almacenado: {e}")
            resultados = []

    
    candidato = get_object_or_404(Candidatos, id_cand=id)
    if candidato.tipo == 'P':
     titulo = 'Candidato Propietario'
     titulopro = ''
    elif candidato.tipo == 'S':
        titulo = 'Candidato Suplente'
        # Obtener el nombre completo del propietario si existe
        if candidato.id_propietario:
         titulopro = f"Candidato Propietario: {candidato.id_propietario.nombres} {candidato.id_propietario.apaterno} {candidato.id_propietario.amaterno}"
        else:
         titulopro = ''  # No hay propietario
    else:
     titulo = ''    
     titulopro = ''

    # Pasa el nombre completo del candidato a la plantilla
    nombre_completo = f"{candidato.nombres} {candidato.apaterno} {candidato.amaterno}"

    return render(request, 'Revicion del Ople/Documentos.html', {'documentos_mostrar': resultados, 'nombreeleccion': nombreeleccion, 'nombrecargo': nombrecargo , 'nombre_completo': nombre_completo, 'id':id, 'anio':anio, 'nombre_partido':nombre_partido, 'titulo': titulo, 'titulopro':titulopro, **context})



def carga_documentos(request):
    if request.method == 'POST':  
        try:
            archivo = request.FILES['archivo']
            id_candidato = request.POST.get('idCandidato')
            nombre_documento = request.POST.get('nombreDocumento')

            # Busca el documento existente con los where proporcionados
            documento = get_object_or_404(DocumentosCandidatos, id_cand=id_candidato, idtipo_doc=nombre_documento)

            # Actualiza la información del documento en la base de datos
            documento.direccion = archivo
            documento.estatus = 'Capturado'  # Define el estatus según tus necesidades
            documento.estatus_revicion = 'Pendiente'  # Define el estatus de revisión según tus necesidades
            documento.save()

            return JsonResponse({'message': 'Archivo recibido y documento actualizado exitosamente'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return redirect('documentos_candidatos')



def visualizar_documento(request):
    id_candidato = request.GET.get('idCandidato')
    nombre_documento = request.GET.get('nombreDocumento')

    # Lógica para obtener la dirección del documento
    # Supongamos que la dirección de los documentos se guarda en el modelo DocumentosCandidatos

    # Importa el modelo
    from .models import DocumentosCandidatos

    # Obtiene el documento
    documento = DocumentosCandidatos.objects.get(id_cand=id_candidato, idtipo_doc=nombre_documento)

    # Obtén la dirección del documento
    documento_direccion = documento.direccion.path

    # Verifica que el archivo exista
    if os.path.exists(documento_direccion):
        # Abre y lee el archivo
        with open(documento_direccion, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/pdf')

            # Configura el encabezado para forzar la descarga
            response['Content-Disposition'] = f'inline; filename={os.path.basename(documento_direccion)}'
            return response
    else:
        # Devuelve una respuesta 404 si el archivo no existe
        return HttpResponse('Documento no encontrado', status=404)



def comentar_documento(request, id, iddoc, nombreeleccion,nombrecargo, anio):

    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
    doc = get_object_or_404(DocumentosCandidatos, id_cand =id, idtipo_doc=iddoc)
    formulario = ComentarDoc_Ople(request.POST or None, 
                             instance=doc)

    if formulario.is_valid() and request.POST:
      formulario.save()
        # Construir la URL basada en su nombre y parámetros
      url = reverse('documentos_candidatos_Ople', args=[id, nombreeleccion, nombrecargo, anio])
        # Redirigir a la URL construida
      return redirect(url)

    return render(request, 'Revicion del Ople/Comentar_doc.html', {'formulario': formulario, **context})




 
def regicadCo_consulta(request, iddistrito, nombreeleccion):
    idpartido = request.session['ID_PARTIDO']
    estado_id = request.session['ID_ESTADO']
    #idcargo = get_object_or_404(Tipocargo, descrip_tcargo=cargo)
    proceso = get_object_or_404(Procesos, descrip=nombreeleccion, idestado=estado_id)

    with connection.cursor() as cursor:
        # Llamada al procedimiento almacenado
        cursor.callproc('obtener_info_candidato_en_coalicion', [proceso.idproceso, idpartido, ])

        # Obtenemos los resultados
        candidatos = cursor.fetchall()

    if len(candidatos) > 0:
        data = {'message': "Success", 'candidatos': candidatos}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)







def prueba_consulta(request):
     
     Candidatoslist = list(Candidatos.objects.filter(idprocesopartido=1, idprinc='MY', idproceso=2, iddistrito=1).values())
     if len(Candidatoslist) > 0:
        data = {'message': "Success", 'distritos': Candidatoslist}
     else:
        data = {'message': "Not found"}

     return JsonResponse(data)



def regicadCongreso_consulta(request, iddistrito, nombreeleccion):
     
     Candidatoslist = list(Candidatos.objects.filter(idprocesopartido=1, idprinc='MY', idproceso=2, iddistrito=1).values())
     if len(Candidatoslist) > 0:
        data = {'message': "Success", 'Candidatoslist': Candidatoslist}
     else:
        data = {'message': "Not found"}

     return JsonResponse(data)



def get_elecciones_Congreso(request):
   # Obtener el estado actual desde settings
    id_estado = request.session['ID_ESTADO']

    # Obtener el año actual
    hoy = datetime.today().date()
    año_actual = hoy.year
    if id_estado ==0:
        elecciones = list(Procesos.objects.filter( anio=año_actual, idtipoc='CO').values())
    else:
        elecciones = list(Procesos.objects.filter(idestado=id_estado, anio=año_actual, idtipoc='CO').values())

    # Filtrar las elecciones por ID_ESTADO y por año
    
    if len(elecciones) > 0:
        data = {'message': "Success", 'elecciones': elecciones}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)




def get_elecciones_Ayuntamiento(request):
   # Obtener el estado actual desde settings
    id_estado = request.session['ID_ESTADO']

    # Obtener el año actual
    hoy = datetime.today().date()
    año_actual = hoy.year

    # Filtrar las elecciones por ID_ESTADO y por año
    elecciones = list(Procesos.objects.filter(idestado=id_estado, anio=año_actual, idtipoc='AY').values())

    if len(elecciones) > 0:
        data = {'message': "Success", 'elecciones': elecciones}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)



def Eliminar_AY(request, id):
    try:
        candidato_obj = Candidatos.objects.get(id_cand=id)
        candidato_obj.delete()
        data = {'message': 'Success'}
    except IntegrityError:
        data = {'message': 'No se puede eliminar esta Candidato, debido a que ya se le asignó un Suplente'}
    
    return JsonResponse(data)


def get_representantes_computos(request, anio, nombreeleccion, cargo):
    # Obtener el estado actual desde settings
    id_estado = request.session['ID_ESTADO']
    idpartido = request.session['ID_PARTIDO']
    proceso = get_object_or_404(Procesos, idestado=id_estado, anio=anio, descrip=nombreeleccion)
    cargoo = get_object_or_404(Tipocargo, descrip_tcargo=cargo)
    # Filtrar las elecciones por ID_ESTADO y por año
    representantes = list(Representantes.objects.filter(idproceso=proceso.idproceso, idpartido=idpartido, obs_repre='Re', idtipo_cargo=cargoo.idtipo_cargo).values())

    if representantes:
        data = {'message': "Success", 'representantes': representantes}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)



def get_representantes_Ople(request, anio, nombreeleccion, cargo, partido):
    # Obtener el estado actual desde settings
    id_estado = request.session['ID_ESTADO']
    proceso = get_object_or_404(Procesos, idestado=id_estado, anio=anio, descrip=nombreeleccion)
    cargoo = get_object_or_404(Tipocargo, descrip_tcargo=cargo)
    # Filtrar las elecciones por ID_ESTADO y por año
    representantes = list(Representantes.objects.filter(idproceso=proceso.idproceso, obs_repre='Re', idtipo_cargo=cargoo.idtipo_cargo, idpartido=partido).values())

    if representantes:
        data = {'message': "Success", 'representantes': representantes}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)


def get_elecciones_Gu(request):
   # Obtener el estado actual desde settings
    id_estado = request.session['ID_ESTADO']



    # Filtrar las elecciones por ID_ESTADO y por año
    elecciones = list(Procesos.objects.filter(idestado=id_estado,  descrip='Gubernatura').values())

    if len(elecciones) > 0:
        data = {'message': "Success", 'elecciones': elecciones}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)


def get_elecciones_Co(request):
   # Obtener el estado actual desde settings
    id_estado = request.session['ID_ESTADO']



    # Filtrar las elecciones por ID_ESTADO y por año
    elecciones = list(Procesos.objects.filter(idestado=id_estado,  descrip='Congreso').values())

    if len(elecciones) > 0:
        data = {'message': "Success", 'elecciones': elecciones}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)

def get_elecciones_Co_My(request):
   # Obtener el estado actual desde settings
    id_estado = request.session['ID_ESTADO']

    # Obtener el año actual
    hoy = datetime.today().date()
    año_actual = hoy.year

    # Filtrar las elecciones por ID_ESTADO y por año
    elecciones = list(Procesos.objects.filter(idestado=id_estado, anio=año_actual, descrip='Diputaciones de Mayoría Relativa').values())

    if len(elecciones) > 0:
        data = {'message': "Success", 'elecciones': elecciones}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)


def get_elecciones_Co_Rp(request):
   # Obtener el estado actual desde settings
    id_estado = request.session['ID_ESTADO']

    # Obtener el año actual
    hoy = datetime.today().date()
    año_actual = hoy.year

    # Filtrar las elecciones por ID_ESTADO y por año
    elecciones = list(Procesos.objects.filter(idestado=id_estado, anio=año_actual, descrip='Diputaciones de Representación Proporcional').values())

    if len(elecciones) > 0:
        data = {'message': "Success", 'elecciones': elecciones}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)


def get_elecciones_All(request):
   # Obtener el estado actual desde settings
    id_estado = request.session['ID_ESTADO']

    # Obtener el año actual
    hoy = datetime.today().date()
    año_actual = hoy.year

    # Filtrar las elecciones por ID_ESTADO y por año
    elecciones = list(Procesos.objects.filter(idestado=id_estado, anio=año_actual).values())

    if len(elecciones) > 0:
        data = {'message': "Success", 'elecciones': elecciones}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)


def get_eleccionefilter_congreso(request, anio):
    # Obtener el estado actual desde settings
    id_estado = request.session['ID_ESTADO']

    # Filtrar las elecciones por ID_ESTADO y por año
    elecciones = list(Procesos.objects.filter(idestado=id_estado, anio=anio, descrip='Congreso').values())

    if len(elecciones) > 0:
        data = {'message': "Success", 'elecciones': elecciones}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)





def get_eleccionefilter_ayuntamiento(request, anio):
    # Obtener el estado actual desde settings
    id_estado = request.session['ID_ESTADO']

    # Filtrar las elecciones por ID_ESTADO y por año
    elecciones = list(Procesos.objects.filter(idestado=id_estado, anio=anio, descrip='Ayuntamiento').values())

    if len(elecciones) > 0:
        data = {'message': "Success", 'elecciones': elecciones}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)




def get_elecciones(request):
    # Obtener el estado actual desde settings
    id_estado = request.session['ID_ESTADO']
    print(id_estado)
    # Obtener el año actual
    hoy = datetime.today().date()
    año_actual = hoy.year
    if id_estado ==0:
        elecciones = list(Procesos.objects.all())
    else:
        elecciones = list(Procesos.objects.filter(idestado=id_estado, anio=año_actual).values())
    # Filtrar las elecciones por ID_ESTADO y por año

    if len(elecciones) > 0:

        data = {'message': "Success", 'elecciones': elecciones}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)

def get_partidos(request):
    # Obtener el estado actual desde settings
    id_estado = request.session['ID_ESTADO']

    # Obtener el año actual
    hoy = datetime.today().date()
    año_actual = hoy.year

    # Filtrar las elecciones por ID_ESTADO y por año
    elecciones = list(Partidos.objects.values())

    if len(elecciones) > 0:
        data = {'message': "Success", 'elecciones': elecciones}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)

def get_estados(request):
    id_estado = request.session['ID_ESTADO']
    
    if id_estado is not None:
        estados = list(Estados.objects.filter(idestado=id_estado).values())
    else:
        estados = list(Estados.objects.values())

    if len(estados) > 0:
        data = {'message': "Success", 'estados': estados}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)



def get_consejos(request):
    # Obtener todos los objetos del modelo Consejos
    consejos = list(Consejos.objects.all().values())

    # Verificar si se encontraron objetos
    if consejos:
        data = {'message': "Success", 'consejos': consejos}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)


def get_cargos(request, idproceso):
    proceso = Procesos.objects.get(idproceso=idproceso) 
    print(proceso)
    # Inicializar el vector de cargos
    cargos = []
        
        # Verificar los campos booleanos y agregar los cargos correspondientes
    if proceso.ayuntamiento:
        cargos.append('AY')
    if proceso.gubernatura:
        cargos.append('GU')
    if proceso.congreso:
        cargos.append('CO')


    if cargos:
        query = Q(idtipoc=cargos[0])
        if len(cargos) > 1:
                query |= Q(idtipoc=cargos[1])
        if len(cargos) > 2:
                query |= Q(idtipoc=cargos[2])
            
        consulta_cargos = list(Tipocargo.objects.filter(query).values())
        data = {'message': "Success", 'cargos': consulta_cargos}
    else:
        data = {'message': "Not found", 'cargos': []}

    return JsonResponse(data)



def get_cargos_filter(request, idproceso,idtipocargo):
    proceso = Procesos.objects.get(idproceso=idproceso) 
    print(proceso)
    # Inicializar el vector de cargos
    cargos = []
        
        # Verificar los campos booleanos y agregar los cargos correspondientes
    if idtipocargo == 'AY':
        cargos.append('AY')
    if idtipocargo == 'GU':
        cargos.append('GU')
    if idtipocargo == 'CO':
        cargos.append('CO')


    if cargos:
        query = Q(idtipoc=cargos[0])
        if len(cargos) > 1:
                query |= Q(idtipoc=cargos[1])
        if len(cargos) > 2:
                query |= Q(idtipoc=cargos[2])
            
        consulta_cargos = list(Tipocargo.objects.filter(query).values())
        data = {'message': "Success", 'cargos': consulta_cargos}
    else:
        data = {'message': "Not found", 'cargos': []}

    return JsonResponse(data)




def get_casillas(request, idtipoc_id,eleccion, iddis):
    id_estado = request.session['ID_ESTADO']
    Proceso=get_object_or_404(Procesos, idestado=id_estado, descrip=eleccion)
    print(idtipoc_id)  
    print(Proceso.idproceso) 
    print(iddis)
    if iddis == 0:
     cargos=list(Casillas.objects.filter(idproceso=Proceso.idproceso).values())
     print("ES GUBERATUA TODAS LAS CASILLAS: ")
    else:
     cargos = list(Casillas.objects.filter(
    idproceso=Proceso.idproceso,
    idtipo_cargo=idtipoc_id
    ).filter(
    Q(iddistrito=iddis) | Q(idmunicipio=iddis)
    ).values())
     
    if len(cargos) > 0:
        data = {'message': "Success", 'cargos': cargos}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)

def get_eleccionefilter(request, anio):
    # Obtener el estado actual desde settings
    id_estado = request.session['ID_ESTADO']

    # Filtrar las elecciones por ID_ESTADO y por año
    elecciones = list(Procesos.objects.filter(idestado=id_estado, anio=anio).values())

    if len(elecciones) > 0:
        data = {'message': "Success", 'elecciones': elecciones}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)

def get_coaliciones_partidos(request):
    idestado= request.session['ID_ESTADO']
    coali = list(Procesopartidos.objects.filter(idestado=idestado).values())
    if len(coali) > 0:
        data = {'message': "Success", 'coali': coali}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)

def get_coaliciones(request,id):
    coali = list(Procesopartidos.objects.filter(idestado=id).values())
    if len(coali) > 0:
        data = {'message': "Success", 'coali': coali}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)


def get_municipios(request, id):

    if id == 0:
     idestados= request.session['ID_ESTADO']
     municipios = list(MunicipioModel.objects.filter(idestado=idestados).values())
    elif id != 0:
     municipios = list(MunicipioModel.objects.filter(idestado=id).values())

    if len(municipios) > 0:
        data = {'message': "Success", 'municipios': municipios}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)

def get_municipios_distrito(request,iddistrito):
    municipios = list(MunicipioModel.objects.filter(iddistrito=iddistrito).values())

    if len(municipios) > 0:
        data = {'message': "Success", 'municipios': municipios}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)

def get_distritos (request, idestado):

    if idestado == 0:
     idestados= request.session['ID_ESTADO']
     distritos = list(Distritos.objects.filter(idestado=idestados).values())
    elif idestado != 0:
     distritos = list(Distritos.objects.filter(idestado=idestado).values())

    if len(distritos) > 0:
        data = {'message': "Success", 'distritos': distritos}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)


def get_num_elec(request, idproceso, idtipocargo):
    try:
        with connection.cursor() as cursor:
            cursor.callproc('obtener_idtipoc', [idproceso, idtipocargo])
            results = cursor.fetchall()
            
            # Si deseas obtener los nombres de las columnas
            columns = [col[0] for col in cursor.description]
            
            # Convierte los resultados a una lista de diccionarios
            data = [
                dict(zip(columns, row))
                for row in results
            ]
        
        response_data = {
            'message': "Success",
            'results': data
        }
    except Exception as e:
        response_data = {
            'message': f"Error: {str(e)}"
        }
    
    return JsonResponse(response_data)
def generar_pdf(request, anio, nombreeleccion, nombrecargo, idcand):
    # Crear un nuevo documento PDF
    pdf = FPDF()

    # Establecer márgenes de página
    pdf.set_auto_page_break(auto=True, margin=2)  # Auto salto de página con un margen de 2mm
    pdf.set_margins(left=5, top=10, right=15)     # Márgenes izquierdo y derecho de 5mm, superior de 10mm

    # Agregar una página en blanco
    pdf.add_page()

    # Obtener datos del estado, partido y candidato
    id_estado = request.session['ID_ESTADO']
    id_partido = request.session['ID_PARTIDO']
    ople = get_object_or_404(Oples, idestado=id_estado)
    estado = get_object_or_404(Estados, idestado=id_estado)
    partido = get_object_or_404(Partidos, idpartido=id_partido)
    candidato = get_object_or_404(Candidatos, id_cand=idcand)

    # Establecer el tamaño y tipo de fuente
    pdf.set_font('Arial', '', 11)

    # Agregar el logo en la esquina superior izquierda
    pdf.image(ople.logo.path, x=10, y=8, w=30)

    # Agregar título
    pdf.cell(200, 5, ople.nombre_completo, 0, 1, 'C')
    pdf.cell(200, 5, nombreeleccion, 0, 1, 'C')
    if candidato.aprobado == 'NO':
        pdf.cell(200, 5, "Reporte de recepción del candidato", 0, 1, 'C')
        pdf.cell(200, 5, "(ESTO NO ES UNA CONSTANCIA DE APROBACIÓN)", 0, 1, 'C')
    else:
        pdf.cell(200, 5, "Constancia de Aprobación del Candidato", 0, 1, 'C')

    pdf.ln()

    # Obtener la fecha actual en español
    fecha_actual = format_date(datetime.now(), format='full', locale='es_ES')

    # Formatear la fecha de registro en español
    fecha_registro_str = format_datetime(candidato.fecha_de_captura, format='short', locale='es_ES')

    # Formatear la fecha de nacimiento en español
    fecha_nacimiento_str = format_date(candidato.fecha_nac, format='long', locale='es_ES')

    # Agregar fecha actual traducida alineada a la derecha
    pdf.cell(0, 5, estado.nombre_edo + " " + fecha_actual, ln=True, align='R')

    pdf.ln()

    Distrito = ""
    Municipio = ""

    if candidato is not None and candidato.iddistrito is not None:
        Distrito = ", del Distrito: " + str(candidato.iddistrito)
    if candidato is not None and candidato.idmunicipio is not None:
        Municipio = ", del Municipio: " + str(candidato.idmunicipio)

    # Agregar contenido con MultiCell para permitir división automática del texto
    texto = ("Por medio del presente se da por recibido el registro del Candidato para la elección: " + nombreeleccion + " "
         "para el cargo: " + nombrecargo + ", del Estado: " + estado.nombre_edo + Distrito + Municipio + ", por parte del partido: " + partido.desc_partido + "  (" + partido.partido + "). ")
    pdf.multi_cell(190, 6, texto, align='L')


    pdf.ln()
    pdf.cell(200, 5, "Los datos capturados en el sistema son: ", 0, 1)
    pdf.ln()

    # Agregar la fecha de registro formateada al PDF
    pdf.cell(200, 7, "Fecha de registro: " + fecha_registro_str, 0, 1)
    pdf.cell(200, 7, "Nombre: " + candidato.nombres + " " + candidato.apaterno + " " + candidato.amaterno, 0, 1)
    pdf.cell(200, 7, "Sobrenombre: " + candidato.apodo, 0, 1)


    if candidato.tipo == 'P':
        formule = 'Formula: Propietario'
        propietario=''
        pdf.cell(200, 7,formule, 0, 1)
    elif candidato.tipo == 'S':
        formule = 'Formula: Suplente'
        propietario='Candidato Propietario: '+str(candidato.id_propietario)
        pdf.cell(200, 7, formule, 0, 1)
        pdf.cell(200, 7, propietario, 0, 1)
    elif candidato.tipo == 'N':
        formule = ''  
        propietario=''      

    if candidato.genero == 'M':
        genero_texto = 'Hombre'
    elif candidato.genero == 'F':
        genero_texto = 'Mujer'
    elif candidato.genero == 'X':
        genero_texto = 'No binario'
    else:
        genero_texto = 'Desconocido'

    pdf.cell(200, 7, "Género: " + genero_texto, 0, 1)
    pdf.cell(200, 7, "Fecha de Nacimiento: " + fecha_nacimiento_str, 0, 1)
    pdf.cell(200, 7, "Número de Teléfono: " + candidato.tel, 0, 1)
    pdf.cell(200, 7, "Ocupación: " + candidato.ocupacion, 0, 1)
    pdf.cell(200, 7, "Domicilio: " + candidato.domicilio, 0, 1)
    pdf.cell(200, 7, "Tiempo de Residencia: " + candidato.tiempo_res, 0, 1)
    if candidato.grup_vul == 'S':
        pdf.cell(200, 7, "Pertenece a un Grupo Vulnerable: " + 'Si', 0, 1)
        pdf.cell(200, 7, "Grupo Vulnerable: " + candidato.grup_vulne, 0, 1)

    elif candidato.grup_vul == 'N':
        genero_texto = 'Mujer'
        pdf.cell(200, 7, "Pertenece a un Grupo Vulnerable: " + 'No', 0, 1)
    else:
        pdf.cell(200, 7, "No se identifico un Grupo Vulnerable: ")

    pdf.cell(200, 7, "Correo Electrónico: " + candidato.correo, 0, 1)
    pdf.ln(2)
    pdf.cell(200, 5, "Datos Electorales: ", 0, 1)
    pdf.ln()
    pdf.cell(200, 5, "Clave Electoral: " + candidato.clave_elect, 0, 1)
    pdf.cell(200, 5, "Clave Única de Registro de Población (CURP): " + candidato.curp, 0, 1)

    # Guardar la posición actual del cursor Y después de agregar la tabla
    pdf_y_table_end = pdf.get_y()

    # Agregar una tabla con los documentos del candidato
    pdf.ln(3)  # Espacio en blanco antes de la tabla
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(200, 10, "Documentos del Candidato", 0, 1, 'C')

    pdf.set_font('Arial', '', 11)
    pdf.set_fill_color(230, 230, 230)  # Color de fondo para las filas alternas

    # Encabezados de la tabla
    pdf.set_fill_color(255, 255, 255)  # Establecer el color
    pdf.cell(49, 10, "Nombre del Documento", 1, 0, 'C', fill=True)
    pdf.cell(38, 10, "Estatus de Entrega", 1, 0, 'C', fill=True)
    pdf.cell(45, 10, "Estatus de Revisión", 1, 0, 'C', fill=True)
    pdf.cell(65, 10, "Comentarios de la Revisión", 1, 1, 'C', fill=True)

    pdf.set_font('Arial', '', 8)
    # Obtener los resultados de la consulta
    try:
        with connection.cursor() as cursor:
            cursor.callproc('obtener_documentos_candidatos', [idcand])
            # Recuperar los resultados del procedimiento almacenado
            resultados = cursor.fetchall()
    except Exception as e:
        print(f"Error al llamar al procedimiento almacenado: {e}")
        resultados = []

    # Contenido de la tabla
    for row in resultados:
        nombre_documento = row[4]  # Acceder al nombre del documento
        estatus_entrega = row[6]   # Acceder al estatus de entrega
        estatus_revision = row[7]  # Acceder al estatus de revisión
        comentarios_revision = row[8]  # Acceder a los comentarios de la revisión

        pdf.cell(49, 10, nombre_documento if nombre_documento is not None else "", 1, 0, 'L')
        pdf.cell(38, 10, estatus_entrega if estatus_entrega is not None else "", 1, 0, 'C')
        pdf.cell(45, 10, estatus_revision if estatus_revision is not None else "", 1, 0, 'C')
        pdf.cell(65, 10, comentarios_revision if comentarios_revision is not None else "", 1, 1, 'L')

    # Calcular la cantidad de espacio en blanco necesaria entre la tabla y el código QR
    space_needed = 5  # Puedes ajustar este valor según sea necesario

    # Agregar espacio en blanco debajo de la tabla para separarla del código QR
    pdf.ln(space_needed)

    # Obtener la posición Y después de agregar el espacio en blanco
    pdf_y_qr_start = pdf.get_y()

 # Generar el código QR con datos estáticos para probar


    qr_data_dynamic = (
    ople.nombre_completo
    + "\n"
    + nombreeleccion
    + "\n"
    + fecha_actual
    + " "
    + "\n \n"
    + ("Reporte de recepción del candidato" if candidato.aprobado == 'NO' else "Constancia de Aprobación del Candidato")
    + ("\n(ESTO NO ES UNA CONSTANCIA DE APROBACIÓN)" if candidato.aprobado == 'NO' else "")
    + "\n \n"
    + "Por medio del presente se da por recibido el registro del Candidato para la elección: "
    + nombreeleccion
    + " "
    "para el cargo: "
    + nombrecargo
    + ", del Estado: "
    + estado.nombre_edo
    + Distrito 
    + Municipio 
    + ", por parte del partido: "
    + partido.desc_partido
    + "  ("
    + partido.partido
    + "). "
    + "\n \n"
    + "Los datos capturados en el sistema son:"
    + "\n \n"
    + "Fecha de registro: "
    + fecha_registro_str
    + "\nNombre Completo del Candidato: "
    + candidato.nombres
    + " "
    + candidato.apaterno
    + " "
    + candidato.amaterno
    + "\nSobrenombre: "
    + candidato.apodo
    +formule
    +propietario
    + "\nGénero: "
    + ("Hombre" if candidato.genero == 'M' else ("Mujer" if candidato.genero == 'F' else ("No binario" if candidato.genero == 'X' else "Desconocido")))
    + "\nFecha de Nacimiento: "
    + fecha_nacimiento_str
    + "\nOcupación: "
    + candidato.ocupacion
    + "\nDomicilio: "
    + candidato.domicilio
    + "\nTiempo de Residencia: "
    + candidato.tiempo_res
    + ("\nPertenece a un Grupo Vulnerable: Si\nGrupo Vulnerable: " + candidato.grup_vulne if candidato.grup_vul == 'S' else ("Pertenece a un Grupo Vulnerable: No" if candidato.grup_vul == 'N' else "No se identificó un Grupo Vulnerable"))
    + "\n \nDatos Electorales: \nClave Electoral: "
    + candidato.clave_elect
    + "\nClave Única de Registro de Población (CURP): "
    + candidato.curp
    + "\n \nDocumentos del Candidato:\n"
)

# Agregar los detalles de los documentos a qr_data_dynamic
    for row in resultados:
      nombre_documento = row[4] if row[4] is not None else ""
      estatus_entrega = row[6] if row[6] is not None else ""
      estatus_revision = row[7] if row[7] is not None else ""
      comentarios_revision = row[8] if row[8] is not None else ""
    
     # Concatenar los detalles del documento dentro del bucle
      qr_data_dynamic += (
         f"\nNombre del Documento: {nombre_documento}\n"
         f"Estatus de Entrega: {estatus_entrega}\n"
         f"Estatus de Revisión: {estatus_revision}\n"
         f"Comentarios de la Revisión: {comentarios_revision}\n"
      )

# Crear el código QR con los datos dinámicos
    qr_dynamic = qrcode.make(qr_data_dynamic)
    qr_stream_dynamic = BytesIO()
    qr_dynamic.save(qr_stream_dynamic, 'PNG')
# Establecer la posición para agregar el código QR en el PDF
    pdf_x = 143
    pdf_y = pdf_y_qr_start -140

# Crear un archivo temporal para almacenar el código QR
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmpfile:
    # Guardar el contenido de qr_stream_static en el archivo temporal
     tmpfile.write(qr_stream_dynamic.getvalue())
    # Obtener la ruta del archivo temporal
     tmp_filename = tmpfile.name

# Agregar el código QR al PDF desde el archivo temporal
    pdf.image(tmp_filename, x=pdf_x, y=pdf_y, w=50)

# Eliminar el archivo temporal después de usarlo
    os.unlink(tmp_filename)


    # Guardar el PDF en un objeto de bytes
    pdf_data = pdf.output(dest='S').encode('latin1')
    # Devolver el PDF como respuesta
    response = HttpResponse(pdf_data, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Reporte_del_Candidato.pdf"'
    return response




 # SISTEMA DE PAQUETES ELCTROALES

def get_paquetes_armados(request, eleccion, cargo, id, key):
    print(str(id))
    print(key)
    # Obtener el estado actual desde settings
    id_estado = request.session['ID_ESTADO']
    proceso = get_object_or_404(Procesos, descrip=eleccion, idestado=id_estado)

    with connection.cursor() as cursor:
        cursor.execute("CALL obtener_num_elec(%s, %s, %s, %s )", [proceso.idproceso, cargo, id, key])
        paquetes = cursor.fetchall()

    if len(paquetes) > 0:
        data = {'message': "Success", 'paquetes': paquetes}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)


def generar_pd_Representante(request, anio, nombreeleccion, idcand, cargo):
    # Crear un nuevo documento PDF
    pdf = FPDF()

    # Establecer márgenes de página
    pdf.set_auto_page_break(auto=True, margin=2)  # Auto salto de página con un margen de 2mm
    pdf.set_margins(left=15, top=10, right=15)     # Márgenes izquierdo y derecho de 15mm, superior de 10mm

    # Agregar una página en blanco
    pdf.add_page()

    # Obtener datos del estado, partido y candidato
    id_estado = request.session['ID_ESTADO']
    id_partido = request.session['ID_PARTIDO']
    ople = get_object_or_404(Oples, idestado=id_estado)
    estado = get_object_or_404(Estados, idestado=id_estado)
    partido = get_object_or_404(Partidos, idpartido=id_partido)
    Representante = get_object_or_404(Representantes, cdg_repre=idcand)

    # Establecer el tamaño y tipo de fuente
    pdf.set_font('Arial', '', 11)

    # Agregar el logo en la esquina superior izquierda
    
    pdf.image(ople.logo.path, x=10, y=8, w=34)


    # Agregar título
    pdf.cell(200, 5, ople.nombre_completo, 0, 1, 'C')
    pdf.cell(200, 5, nombreeleccion, 0, 1, 'C')
    pdf.cell(200, 5, cargo, 0, 1, 'C')
    pdf.cell(200, 5, partido.desc_partido, 0, 1, 'C')
    pdf.ln(3)

    # Obtener la fecha actual en español
    fecha_actual = format_date(datetime.now(), format='full', locale='es_ES')

    # Agregar fecha actual traducida alineada a la derecha
    pdf.cell(0, 5, estado.nombre_edo + " " + fecha_actual, ln=True, align='R')

    pdf.ln()

    Distrito = ""
    Municipio = ""

    # Agregar contenido con MultiCell para permitir división automática del texto

    estatus_obs = 'Observador' if Representante.obs_repre == 'Ob' else 'Representante'

    pdf.ln()
    pdf.cell(200, 5, "Datos del " +estatus_obs+ " ante Cómputos Electorales: ", 0, 1,)
    pdf.ln()


    # Guardar la posición actual del cursor Y después de agregar la tabla
    pdf_y_table_end = pdf.get_y()

    # Agregar una tabla con los documentos del candidato
    pdf.ln(3)  # Espacio en blanco antes de la tabla
    pdf.cell(200, 7, 'Nombre: ' + Representante.nombre, 0, 1,)
    pdf.cell(200, 7, 'Apellido Paterno: ' + Representante.ap_paterno, 0, 1,)
    pdf.cell(200, 7, 'Apellido Materno: ' + Representante.ap_materno, 0, 1,)
    genero_etiqueta = ''
    if Representante.genero == 'F':
            genero_etiqueta = 'Mujer'
    elif Representante.genero == 'M':
         genero_etiqueta = 'Hombre'
    elif Representante.genero == 'X':
             genero_etiqueta = 'No binario'
    else:
            genero_etiqueta = Representante.genero  # Si el género es otro, mantener el valor original

    pdf.cell(200, 7, 'Género: ' + genero_etiqueta, 0, 1,)

    ''''
    tipo_repre_etiqueta = ''
    if Representante.tipo_repre == 'T':
        tipo_repre_etiqueta = 'Titular'
    elif Representante.tipo_repre == 'S':
        tipo_repre_etiqueta = 'Suplente'
    else:
        tipo_repre_etiqueta = Representante.tipo_repre  # Si el tipo no es T ni S, mantener el valor original

    pdf.cell(200, 7, 'Tipo de Representante: ' + tipo_repre_etiqueta, 0, 1, 'C')
    '''

    pdf.cell(200, 7, 'Curp: ' + Representante.curp, 0, 1,)
    pdf.cell(200, 7, 'Clave Electoral: ' + Representante.clave_elec, 0, 1,)
    fecha_formateada = Representante.fecha_reg.strftime('%d-%m-%Y %H:%M:%S')

    pdf.cell(200, 7, 'Fecha de Registro: ' + fecha_formateada, 0, 1,)
    fecha_formateadaa = Representante.fecha_cita.strftime('%d-%m-%Y')

    pdf.cell(200, 7, 'Fecha de Cita: ' + fecha_formateadaa, 0, 1, )    
    pdf.cell(200, 7, 'Hora Inicio de la Cita: ' + Representante.hora_inicio.strftime('%H:%M'), 0, 1,)
    pdf.cell(200, 7, 'Hora Fin de la Cita: ' + Representante.hora_fin.strftime('%H:%M'), 0, 1,)      

   

    estatus_str = 'Activo' if Representante.status == 'Ac' else 'Inactivo'
    pdf.cell(200, 7, 'Estatus: ' + estatus_str, 0, 1, )
 
    pdf.cell(200, 7, 'Consejo: ' + str(Representante.cdg_consejo), 0, 1,) 

    # Obtener los resultados de la consulta

    # Calcular la cantidad de espacio en blanco necesaria entre la tabla y el código QR
    space_needed = 5  # Puedes ajustar este valor según sea necesario

    # Agregar espacio en blanco debajo de la tabla para separarla del código QR
    pdf.ln(space_needed)

    # Obtener la posición Y después de agregar el espacio en blanco
    pdf_y_qr_start = pdf.get_y()

 # Generar el código QR con datos estáticos para probar


    qr_data_dynamic = (
        ople.nombre_completo
        + "\n"
        +nombreeleccion
        + "\n"
        +partido.desc_partido
        + "\n"
        +"\n"
        + "\n"
        +"Datos del " +estatus_obs+ " ante Cómputos Electorales: "
        +"\n" 
        + "\n"
        +'Año: ' + anio
        + "\n"
        +'Elección en Disputa: ' + nombreeleccion
        + "\n"
        +'Cargo en Disputa: ' + cargo
        + "\n"
        +'Representante número: ' + idcand
        + "\n"
        +'Nombre: ' + Representante.nombre
        + "\n"
        +'Apellido Paterno: ' + Representante.ap_paterno
        + "\n"
        +'Apellido Materno: ' + Representante.ap_materno
        + "\n"
        +'Género: ' + genero_etiqueta
        + "\n"
        +'Curp: ' + Representante.curp
        + "\n"
        +'Clave Electoral: ' + Representante.clave_elec
        + "\n"
        +'Fecha de Registro: ' + fecha_formateada
        + "\n"
        +'Fecha de Cita: ' + fecha_formateadaa
        + "\n"
        +'Hora Inicio de la Cita: ' + Representante.hora_inicio.strftime('%H:%M')
        + "\n"
        +'Hora Fin de la Cita: ' + Representante.hora_fin.strftime('%H:%M')
        + "\n"
        + "\n"
        + "\n"
        +'Estatus: ' + estatus_str
        + "\n"
        +'Consejo: ' + str(Representante.cdg_consejo)
        )

# Crear el código QR con los datos dinámicos
    qr_dynamic = qrcode.make(qr_data_dynamic)
    qr_stream_dynamic = BytesIO()
    qr_dynamic.save(qr_stream_dynamic, 'PNG')
# Establecer la posición para agregar el código QR en el PDF
    pdf_x = 80
    pdf_y = pdf_y_qr_start +15

# Crear un archivo temporal para almacenar el código QR
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmpfile:
    # Guardar el contenido de qr_stream_static en el archivo temporal
     tmpfile.write(qr_stream_dynamic.getvalue())
    # Obtener la ruta del archivo temporal
     tmp_filename = tmpfile.name

# Agregar el código QR al PDF desde el archivo temporal
    pdf.image(tmp_filename, x=pdf_x, y=pdf_y, w=50)

# Eliminar el archivo temporal después de usarlo
    os.unlink(tmp_filename)


    # Guardar el PDF en un objeto de bytes
    pdf_data = pdf.output(dest='S').encode('latin1')
    # Devolver el PDF como respuesta
    response = HttpResponse(pdf_data, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Reporte_del_Candidato.pdf"'
    return response


def agregar_Representantes_Titulares_Computos(request, anio, nombreeleccion, cargo):
    estado_id = request.session['ID_ESTADO']
    fecha_hora_actual_python = timezone.now()
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  

    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido
    eleccion = get_object_or_404(Procesos, descrip=nombreeleccion, idestado=estado_id)
    cargo = get_object_or_404(Tipocargo, descrip_tcargo=cargo)
    formulario = Representantes_ante_computos_Titulares(request.POST or None, request.FILES or None)
    estado = get_object_or_404(Estados, idestado=estado_id)
    try:
            if request.method == 'POST':
                formulario = Representantes_ante_computos_Titulares(request.POST)
                if formulario.is_valid():
                    consejo = formulario.cleaned_data['cdg_consejo']
                    Representante = formulario.save(commit=False)

                    Representante.idproceso = eleccion
                    Representante.obs_repre = 'Re'
                    Representante.idpartido = partido
                    Representante.idtipo_cargo=cargo 
                    Representante.cdg_consejo = consejo
                    Representante.fecha_reg = fecha_hora_actual_python
                    Representante.save()
                 
               # Obtener el id_cand máximo
                max_cdg_repre = Representantes.objects.all().aggregate(Max('cdg_repre'))
                nuevo_id_cand = max_cdg_repre['cdg_repre__max']
                print(nuevo_id_cand)
                representante_max = Representantes.objects.get(cdg_repre=nuevo_id_cand)
                 #Obtener los resultados de documentos
                resultados = DocCandidatos.objects.filter(idproceso=eleccion.idproceso).values_list('idtipo_doc', flat=True)

                # Obtener instancias de Tipodoc según los resultados
                tipos_documentos = Tipodoc.objects.filter(idtipo_doc__in=resultados)

                # Crear instancias de DocumentosCandidatos y asignar la instancia de Candidatos
                documentos = [
                         DocRepresen(cdg_repre=representante_max, idproceso=eleccion, idtipo_doc=tipo_doc, status="Faltante")
                         for tipo_doc in tipos_documentos
                           ]

                DocRepresen.objects.bulk_create(documentos)

                return redirect('Comp_Agregar_Candidatos_Agregar')
        
    except IntegrityError as e:
        print(f"Error de integridad al guardar el formulario: {e}")
    except ValidationError as e:
        print(f"Error de validación al guardar el formulario: {e}")
    except Exception as e:
        print(f"Error general al guardar el formulario: {e}")

    return render(request, 'computos/agregar_candidatos/crear.html', {'formulario': formulario, 'anio': anio, 'nombreeleccion': nombreeleccion,  'nombre_partido': nombre_partido, 'cargo':cargo.descrip_tcargo, 'anio':anio, 'nombreedo':estado.nombre_edo, **context})

def agregar_Representantes_editar_titular(request,id, eleccion, cargo, anio):
    representante = get_object_or_404(Representantes, cdg_repre=id)
    cargoss = get_object_or_404(Tipocargo, descrip_tcargo=cargo)
    idpartido = request.session['ID_PARTIDO']
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
    estado_id = request.session['ID_ESTADO']
    estado = get_object_or_404(Estados, idestado=estado_id)
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido
    formulario = Representantes_ante_computos_Titulares(request.POST or None, request.FILES or None, instance=representante)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('Comp_Agregar_Candidatos_Agregar')
    return render(request, 'computos/agregar_candidatos/editar.html', {'formulario': formulario, 'representante': representante, 'nombreeleccion':eleccion, 'nombre_partido':nombre_partido,'nombreedo':estado.nombre_edo, 'cargo':cargoss.descrip_tcargo, 'anio':anio, **context})



def agregar_Representantes_editar_titular_Ople(request,id, eleccion, cargo, anio):
    representante = get_object_or_404(Representantes, cdg_repre=id)
    cargoss = get_object_or_404(Tipocargo, descrip_tcargo=cargo)
    idpartido = request.session['ID_PARTIDO']
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
    estado_id = request.session['ID_ESTADO']
    estado = get_object_or_404(Estados, idestado=estado_id)
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido
    formulario = Representantes_Ople(request.POST or None, request.FILES or None, instance=representante)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('representantes_Ople')
    return render(request, 'computos/representantes_ople/editar.html', {'formulario': formulario, 'representante': representante, 'nombreeleccion':eleccion, 'nombre_partido':nombre_partido,'nombreedo':estado.nombre_edo, 'cargo':cargoss.descrip_tcargo, 'anio':anio, **context})

def Candidatos_contienda_eliminar(request, id):
  try:
    repre_obj = ProcesopartidoCandidato.objects.get(id_cand=id)  
    repre_obj.delete()

  except IntegrityError:
    mensaje = "Error deleting"
    messages.error(request, mensaje)

  return redirect('candidatos_contienda')


def agregar_Representantes_eliminar(request, id):
  try:
    repre_obj = Representantes.objects.get(cdg_repre=id)  
    repre_obj.delete()

  except IntegrityError:
    mensaje = "No se puede eliminar Represenante, debido a que tiene asigando un Suplente"
    messages.error(request, mensaje)

  return redirect('Comp_Agregar_Candidatos_Agregar')


def documentos_representantes(request, id, nombreeleccion, anio, cargo):
    # Llamada al procedimiento almacenado
    estado_id = request.session['ID_ESTADO']
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos

    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
    estado = get_object_or_404(Estados, idestado=estado_id)
    with connection.cursor() as cursor:
        try:
            cursor.callproc('obtener_documentos_representantes', [id])
            # Recuperar los resultados del procedimiento almacenado
            resultados = cursor.fetchall()
        except Exception as e:
            print(f"Error al llamar al procedimiento almacenado: {e}")
            resultados = []

    # Obtener el objeto Candidatos correspondiente al id
    Representante = get_object_or_404(Representantes, cdg_repre=id)

    # Pasa el nombre completo del candidato a la plantilla

    nombre_completo = f"{Representante.nombre} {Representante.ap_paterno} {Representante.ap_materno}"

    return render(request, 'computos/agregar_candidatos/Documentos.html', {'nombreedo':estado.nombre_edo ,'anio':anio,'cargo':cargo,'documentos_mostrar': resultados, 'nombreeleccion': nombreeleccion,  'nombre_completo': nombre_completo, 'idcand': id, **context})



def carga_documentos_representantes(request):
    if request.method == 'POST':
        try:
            # Obtener el archivo del formulario y los datos relacionados
            archivo = request.FILES.get('archivo')
            id_candidato = request.POST.get('idCandidato')
            nombre_documento = request.POST.get('nombreDocumento')

            # Verificar si se proporcionaron todos los datos necesarios
            if not all([archivo, id_candidato, nombre_documento]):
                return JsonResponse({'error': 'Falta uno o más datos requeridos'}, status=400)

            # Buscar el documento existente con los criterios proporcionados
            documento = get_object_or_404(DocRepresen, cdg_repre=id_candidato, idtipo_doc=nombre_documento)

            # Actualizar la información del documento en la base de datos
            documento.archivo = archivo
            documento.status = 'Capturado'  # Define el estatus según tus necesidades
            documento.save()

            # Devolver una respuesta exitosa si todo funciona correctamente
            return JsonResponse({'message': 'Archivo recibido y documento actualizado exitosamente'})

        except FileNotFoundError:
            return JsonResponse({'error': 'El archivo no se encontró'}, status=404)

        except Exception as e:
            # Capturar cualquier otro error y devolverlo como una respuesta JSON
            return JsonResponse({'error': str(e)}, status=500)

    else:
        # Devolver la página de renderizado si la solicitud no es POST
        return redirect('documentos_representantes')
    



def visualizar_documento_representantes(request):
    id_candidato = request.GET.get('idCandidato')
    nombre_documento = request.GET.get('nombreDocumento')

    # Lógica para obtener la dirección del documento
    # Supongamos que la dirección de los documentos se guarda en el modelo DocumentosCandidatos

    # Obtiene el documento
    documento = DocRepresen.objects.get(cdg_repre=id_candidato, idtipo_doc=nombre_documento)

    # Obtén la dirección del documento
    documento_direccion = documento.archivo.path

    # Verifica que el archivo exista
    if os.path.exists(documento_direccion):
        # Abre y lee el archivo
        with open(documento_direccion, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/pdf')

            # Configura el encabezado para forzar la descarga
            response['Content-Disposition'] = f'inline; filename={os.path.basename(documento_direccion)}'
            return response
    else:
        # Devuelve una respuesta 404 si el archivo no existe
        return HttpResponse('Documento no encontrado', status=404)



def agregar_paquetes_armados(request , eleccion, cargo, anio, valor, ide):

    estado_id = request.session['ID_ESTADO']
    fecha_hora_actual_python = timezone.now()
    fecha_hora_actual_utc = timezone.now()
    
        # Convierte la fecha y hora actual a la zona horaria local
    fecha_hora_actual_local = timezone.localtime(fecha_hora_actual_utc)

    # Obtiene solo la hora actual en formato HH:MM:SS
    hora_actual = fecha_hora_actual_local.strftime("%H:%M:%S")
    print(request.session['ID_USUARIO'])
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion    
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
    # Puedes imprimir la hora actual en la consola si lo deseas
    print("Hora actual:", hora_actual)
    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido


    cargo = get_object_or_404(Tipocargo, descrip_tcargo=cargo)
    eleccion = get_object_or_404(Procesos, descrip=eleccion, idestado=estado_id)
    estado = get_object_or_404(Estados, idestado=estado_id)
    formulario = Armado_paquetes(request.POST or None, request.FILES or None, ide=ide)


    num_elect = Procesoscargo.objects.filter(
    Q(idproceso=eleccion.idproceso) & 
    Q(idtipo_cargo=cargo.idtipo_cargo) & 
    (Q(idMunicipio=ide) | Q(idDistrito=ide))
    ).first()
    print(num_elect)
    try:
            if request.method == 'POST':
                formulario = Armado_paquetes(request.POST)
                if formulario.is_valid():
                    cargoople_id = formulario.cleaned_data['idcargoople']
                    folioc = formulario.cleaned_data['folioc']
                    clave_ca= formulario.cleaned_data['clave_ca'] 

                    print(cargoople_id)
                    print(folioc.folioc)
                    print(clave_ca.Clave_ca)
                    cargoople = get_object_or_404(CatCargosOple,nombre_cargo=cargoople_id)
                    casilla = get_object_or_404(Casillas, folioc=folioc.folioc)
                    centro_acopio=get_object_or_404(CentrosDeAcopio, Clave_ca=clave_ca.Clave_ca)
                    Paquete = formulario.save(commit=False)

                    Paquete.num_elec=num_elect
                    Paquete.folioc =casilla
                    Paquete.idProceso=eleccion
                    Paquete.clave_ca =centro_acopio
                    Paquete.fecha_entrega = fecha_hora_actual_python
                    Paquete.hora_entrega = hora_actual
                    Paquete.idcargoople = cargoople
                    Paquete.estatus = "C"
                    Paquete.save()

                return redirect('Armado_Paquetes')
                

    except IntegrityError as e:
        print(f"Error de integridad al guardar el formulario S: {e}")
    except ValidationError as e:
        print(f"Error de validación al guardar el formularioc S: {e}")
    except Exception as e:
        print(f"Error general al guardar el formulario S: {e}")



    return render(request, 'paquetes/armado_paquetes/crear.html', {'formulario': formulario, 'anio': anio, 'nombreeleccion': eleccion, 'valor':valor,'nombrecargo': cargo,   'nombreedo':estado.nombre_edo,**context})





def agregar_paquetes_vizualizar(request, eleccion, cargo, num_paquete, anio,valor, folioc):
 
    estado_id = request.session['ID_ESTADO']
    fecha_hora_actual_python = timezone.now()
    fecha_hora_actual_utc = timezone.now()
        # Convierte la fecha y hora actual a la zona horaria local
    fecha_hora_actual_local = timezone.localtime(fecha_hora_actual_utc)
    # Obtiene solo la hora actual en formato HH:MM:SS
    hora_actual = fecha_hora_actual_local.strftime("%H:%M:%S")
    print(request.session['ID_USUARIO'])
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion    
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
    # Puedes imprimir la hora actual en la consola si lo deseas
    print("Hora actual:", hora_actual)
    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido

    cargo = get_object_or_404(Tipocargo, descrip_tcargo=cargo)
    eleccion = get_object_or_404(Procesos, descrip=eleccion, idestado=estado_id)
    Paquetes=get_object_or_404(PaquetesFase1, idPaquete=num_paquete)
    estado = get_object_or_404(Estados, idestado=estado_id)
    print(estado.nombre_edo)
    formulario = Armado_paquetes(request.POST or None, instance=Paquetes)
    

    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('Armado_Paquetes')

    return render(request, 'paquetes/armado_paquetes/editar.html', {'formulario': formulario, 'anio': anio, 'nombreeleccion': eleccion, 'nombrecargo': cargo,  'seccion': folioc, 'nombreedo':estado.nombre_edo,'valor':valor, 'paqueteno': num_paquete,**context})
def generar_pd_Armado_Paquetes(request, anio, nombreeleccion, nombrecargo, idcand):
    try:
        # Crear un nuevo documento PDF con tamaño de ticket de supermercado (80mm x 150mm)
        ancho_mm = 80
        alto_mm = 150

        # Convertir milímetros a pulgadas
        ancho_pulgadas = ancho_mm / 25.4
        alto_pulgadas = alto_mm / 25.4

        # Convertir pulgadas a puntos
        ancho_puntos = ancho_pulgadas * 72
        alto_puntos = alto_pulgadas * 72

        pdf = FPDF(format=(ancho_puntos, alto_puntos))

        # Establecer márgenes de página
        pdf.set_auto_page_break(auto=True, margin=2)  # Auto salto de página con un margen de 2mm
        pdf.set_margins(left=10, top=10, right=10)     # Márgenes izquierdo y derecho de 10mm, superior de 10mm

        # Agregar una página en blanco
        pdf.add_page()

        # Obtener datos del estado, partido y candidato
        id_estado = request.session['ID_ESTADO']
        id_partido = request.session['ID_PARTIDO']
        ople = get_object_or_404(Oples, idestado=id_estado)
        casilla = get_object_or_404(Casillas, folioc=idcand)
        estado = get_object_or_404(Estados, idestado=id_estado)
        partido = get_object_or_404(Partidos, idpartido=id_partido)
        proceso = get_object_or_404(Procesos, descrip=nombreeleccion, idestado=id_estado)
        cargo = get_object_or_404(Tipocargo, descrip_tcargo=nombrecargo)
        eleccion = get_object_or_404(
         Procesoscargo,
         Q(idDistrito=casilla.iddistrito.iddistrito) | Q(idMunicipio=casilla.idmunicipio.idmunicipio),
         idproceso=proceso.idproceso,
         idestado=id_estado,
         idtipo_cargo=cargo.idtipo_cargo
            )
        print(eleccion)
        PaquetesFaseuno = get_object_or_404(PaquetesFase1, folioc=idcand)

        folioc = PaquetesFase1.objects.filter(folioc=idcand).values_list('folioc', flat=True).first()
        paqueteno = get_object_or_404(PaquetesFase1.objects.filter(folioc=idcand).order_by('-idPaquete'))
        # Establecer el tamaño y tipo de fuente
        pdf.set_font('Arial', '', 9)
        
        # Obtener la fecha y hora actual en la zona horaria local
        # Obtener la fecha actual en español
        fecha_actual = datetime.now().strftime('%d/%m/%Y')
        fecha_entrega = PaquetesFaseuno.fecha_entrega.strftime('%d/%m/%Y')

        # Agregar el logo en la esquina superior izquierda
        pdf.image(ople.logo.path, x=92, y=8, w=45)
        pdf.ln(40)
        
        # Agregar título y detalles
        print(ople.nombre_completo)
        pdf.set_font('Arial', '', 14)
        pdf.cell(0, 10, ople.nombre_completo, 0, 1, 'C')
        pdf.cell(0, 7, "Reporte Armado del Paquete", 0, 1, 'C')  # Aumentar espacio entre líneas
        pdf.cell(0, 7, "Número de Paquete: "+ str(paqueteno.idPaquete), 0, 1, 'C')
        pdf.cell(0, 7, estado.nombre_edo, 0, 1, 'C')
        pdf.cell(0, 7, nombreeleccion, 0, 1, 'C')
        pdf.cell(0, 7, nombrecargo, 0, 1,'C' )
        pdf.cell(0, 7, "Distrito: "+str(casilla.iddistrito),0, 1,'C')
        pdf.cell(0, 7, "Municipio: "+str(casilla.idmunicipio),0, 1,'C')
        pdf.ln(5)
   
        
        pdf.ln(10)
        pdf.cell(0, 7, "Fecha de Impresión: " + fecha_actual, 0, 1, )
        pdf.ln(5)
        pdf.cell(0, 7, "Sección: " + folioc, 0, 1, )
        
        pdf.cell(0, 7, "Folio Inicio de Boletas: " + str(PaquetesFaseuno.folio_inicio), 0, 1, )
        pdf.cell(0, 7, "Folio Fin de Boletas: " + str(PaquetesFaseuno.folio_fin), 0, 1, )
        pdf.cell(0, 7, "Cantidad de Boletas: " + str(PaquetesFaseuno.cantidad_boletas), 0, 1, )
        actas_integradas = "Si" if PaquetesFaseuno.actas_entregadas == "S" else "No"
        listas_integradas = "Si" if PaquetesFaseuno.listasnominales_entrega == "S" else "No"

        pdf.cell(0, 7, "¿Se integraron las actas? " + actas_integradas, 0, 1, )
        pdf.cell(0, 7, "¿Se integraron las listas Nominales? " + listas_integradas, 0, 1, )

        pdf.cell(0, 7, "Fecha de entrega: " + fecha_entrega, 0, 1, )
        pdf.cell(0, 7, "Hora de entrega: " + str(PaquetesFaseuno.hora_entrega), 0, 1, )
        pdf.cell(0, 7, "Armó el paquete : " + str(PaquetesFaseuno.nombre_cargo), 0, 1, )
        pdf.cell(0, 7, "Cargo: " + str(PaquetesFaseuno.idcargoople), 0, 1, )

        # Calcular la cantidad de espacio en blanco necesaria entre la tabla y el título del código QR
        space_needed = 10  # Puedes ajustar este valor según sea necesario

        # Agregar espacio en blanco debajo de la tabla para separarla del título del código QR
        pdf.ln(space_needed)

        # Agregar título del código QR
        pdf.set_xy(2, 235)  # Ajustar según sea necesario
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, "                QR Reporte:", 0, 1, 'C')

        # Agregar espacio en blanco antes del código QR
        pdf.ln(5)

        # Obtener la posición Y después de agregar el título y el espacio en blanco
        pdf_y_qr_start = pdf.get_y()

        # Generar el primer código QR con datos estáticos para probar
        qr_data_dynamic = (
            str(anio)+"|"+ str(id_estado)+"|"+ str(proceso.idproceso)+"|"+str(cargo.idtipo_cargo)+"|"+str(cargo.idtipoc.idtipoc)+"|"+str(eleccion.num_elec)+"|"+str(casilla.folioc)+"|"+str(paqueteno.idPaquete)+"|"+str(casilla.id_casilla)
        )

        # Crear el primer código QR con los datos dinámicos
        qr_dynamic = qrcode.make(qr_data_dynamic)
        qr_stream_dynamic = BytesIO()
        qr_dynamic.save(qr_stream_dynamic, 'PNG')
        
        # Establecer la posición para agregar el primer código QR en el PDF
        pdf_x = 30
        pdf_y = pdf_y_qr_start + 5

        # Crear un archivo temporal para almacenar el primer código QR
        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmpfile:
            # Guardar el contenido de qr_stream_dynamic en el archivo temporal
            tmpfile.write(qr_stream_dynamic.getvalue())
            # Obtener la ruta del archivo temporal
            tmp_filename = tmpfile.name

        # Agregar el primer código QR al PDF desde el archivo temporal
       
       # pdf.image(tmp_filename, x=pdf_x, y=pdf_y, w=50)

        # Eliminar el archivo temporal después de usarlo
        os.unlink(tmp_filename)

        # Generar el segundo código QR con todos los detalles del reporte
        qr_data_full = (
    f"{ople.nombre_completo} | \n"
    f"Reporte Armado del Paquete | \n"
    f"Número de Paquete: {paqueteno.idPaquete} | \n"
    f"Año: {anio}\n"
    f"{estado.nombre_edo} | \n"
    f"Elección: {nombreeleccion}\n"
    f"Cargo: {nombrecargo}\n"
    f"Municipio: {casilla.idmunicipio}\n"
    f"Fecha de Impresión: {fecha_actual} | \n"
    f"Sección: {folioc}\n"
    f"Folio Inicio de Boletas: {PaquetesFaseuno.folio_inicio} | \n"
    f"Folio Fin de Boletas: {PaquetesFaseuno.folio_fin} | \n"
    f"Cantidad de Boletas: {PaquetesFaseuno.cantidad_boletas} | \n"
    f"¿Se integraron las actas? {actas_integradas} | \n"
    f"¿Se integraron las listas Nominales? {listas_integradas} | \n"
    f"Fecha de entrega: {fecha_entrega} | \n"
    f"Hora de entrega: {PaquetesFaseuno.hora_entrega} | \n"
    f"Armó el paquete: {PaquetesFaseuno.nombre_cargo} | \n"
    f"Cargo: {PaquetesFaseuno.idcargoople} | \n"
    f"QR Paquete: {qr_data_dynamic}"
)


        # Crear el segundo código QR con todos los detalles del reporte
        qr_full = qrcode.make(qr_data_full)
        qr_stream_full = BytesIO()
        qr_full.save(qr_stream_full, 'PNG')

        # Establecer la posición para agregar el segundo código QR en el PDF
        pdf_x_full = pdf_x + 65  # Ajustar la posición según sea necesario

        # Crear un archivo temporal para almacenar el segundo código QR
        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmpfile_full:
            # Guardar el contenido de qr_stream_full en el archivo temporal
            tmpfile_full.write(qr_stream_full.getvalue())
            # Obtener la ruta del archivo temporal
            tmp_filename_full = tmpfile_full.name

        # Agregar el segundo código QR al PDF desde el archivo temporal
        pdf.image(tmp_filename_full, x=pdf_x_full, y=pdf_y, w=50)

        # Eliminar el archivo temporal después de usarlo
        os.unlink(tmp_filename_full)

        response = HttpResponse(pdf.output(dest='S').encode('latin1'), content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="paquete_{PaquetesFaseuno.idPaquete}.pdf"'

        return response

    except Exception as e:
        # Capturar el traceback completo del error
        error_traceback = traceback.format_exc()

        # Mostrar el error y el traceback en la consola
        print(f"Ocurrió un error: {e}")
        print(f"Traceback completo:\n{error_traceback}")

        # Puedes regresar una respuesta de error o manejarlo según lo necesites
        return HttpResponse(f"Error al generar el PDF: {e}", status=500)
    
    
def Observadores_Agre_index (request):
  

     # Lógica para años
  hoy = datetime.today().date()
  año_actual = hoy.year

  idpartido = request.session['ID_PARTIDO']
  partido = Partidos.objects.get(idpartido=idpartido)
  nombre_partido = partido.desc_partido
  print(request.session['ID_USUARIO'])
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion   
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto


  años = []
  for i in range(año_actual, año_actual+11, +1):
    años.append(i)

  return render(request, 'observadores/resgistro_de_observadores/Index.html', {
    
      'años': años,
      'nombre_partido': nombre_partido,
      **context
  })


def get_Observadores(request, anio, nombreeleccion, cargo):
    # Obtener el estado actual desde settings
    id_estado = request.session['ID_ESTADO']
    idpartido = request.session['ID_PARTIDO']
    proceso = get_object_or_404(Procesos, idestado=id_estado, anio=anio, descrip=nombreeleccion)
    cargoss = get_object_or_404(Tipocargo, descrip_tcargo=cargo)
    # Filtrar las elecciones por ID_ESTADO y por año
    representantes = list(Representantes.objects.filter(idproceso=proceso.idproceso, idpartido=idpartido, obs_repre='Ob', idtipo_cargo=cargoss.idtipo_cargo ).values())

    if representantes:
        data = {'message': "Success", 'representantes': representantes}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)

def get_Candidatos_Contienda(request, anio, nombreeleccion, cargo):
    id_estado = request.session['ID_ESTADO']
    idpartido = request.session['ID_PARTIDO']
    proceso = get_object_or_404(Procesos, idestado=id_estado, anio=anio, descrip=nombreeleccion)
    cargo = get_object_or_404(Tipocargo, descrip_tcargo=cargo)
    print(cargo.idtipo_cargo)
    print(proceso.idproceso)
    representantes = ProcesopartidoCandidato.objects.filter(
        idproceso=proceso.idproceso,
        idtipo_cargo=cargo.idtipo_cargo
    ).select_related(
        'id_cand',
        'id_cand__idestado',
        'id_cand__idmunicipio',
        'id_cand__iddistrito',
        'id_cand__idpartido'
    ).values(
        'id_cand',
        'idprocesopartido',
        'idproceso',
        'idtipo_cargo',
        'anio',
        'nombres',
        'appaterno',
        'apmaterno',
        'sobrenombre',
        'status',
        'foto',
        'idprocesopartido__coliacion',
        'id_cand__idestado__nombre_edo',
        'id_cand__idmunicipio__nombre_mpo',
        'id_cand__iddistrito__nombredistrito',
        'id_cand__idpartido__partido'
    )

    if representantes:
        representantes_list = list(representantes)
        for rep in representantes_list:
            rep['coliacion'] = rep.pop('idprocesopartido__coliacion')
        data = {'message': "Success", 'representantes': representantes_list}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)


def agregar_Observadores(request, anio, nombreeleccion,cargo):
    estado_id = request.session['ID_ESTADO']
    fecha_hora_actual_python = timezone.now()
    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)

    nombre_partido = partido.desc_partido
    eleccion = get_object_or_404(Procesos, descrip=nombreeleccion, idestado=estado_id)
    estado=get_object_or_404(Estados, idestado=estado_id)
    cargoss = get_object_or_404(Tipocargo, descrip_tcargo=cargo)
    print(request.session['ID_USUARIO'])
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
    formulario = Observadoresform(request.POST or None, request.FILES or None)
 
    try:
            if request.method == 'POST':
                formulario = Observadoresform(request.POST)
                if formulario.is_valid():
                    consejo = formulario.cleaned_data['cdg_consejo']
                    Representante = formulario.save(commit=False)

                    Representante.idproceso = eleccion
                    Representante.idtipo_cargo = cargoss
                    Representante.obs_repre = 'Ob'
                    Representante.idpartido = partido
                    Representante.cdg_consejo = consejo
                    Representante.fecha_reg = fecha_hora_actual_python
                    Representante.save()
                 
               # Obtener el id_cand máximo
                max_cdg_repre = Representantes.objects.all().aggregate(Max('cdg_repre'))
                nuevo_id_cand = max_cdg_repre['cdg_repre__max']
                print(nuevo_id_cand)
                representante_max = Representantes.objects.get(cdg_repre=nuevo_id_cand)
                 #Obtener los resultados de documentos
                resultados = DocCandidatos.objects.filter(idproceso=eleccion.idproceso).values_list('idtipo_doc', flat=True)

                # Obtener instancias de Tipodoc según los resultados
                tipos_documentos = Tipodoc.objects.filter(idtipo_doc__in=resultados)

                # Crear instancias de DocumentosCandidatos y asignar la instancia de Candidatos
                documentos = [
                         DocRepresen(cdg_repre=representante_max, idproceso=eleccion, idtipo_doc=tipo_doc, status="Faltante")
                         for tipo_doc in tipos_documentos
                           ]

                DocRepresen.objects.bulk_create(documentos)

                return redirect('Observadores_index')
        
    except IntegrityError as e:
        print(f"Error de integridad al guardar el formulario: {e}")
    except ValidationError as e:
        print(f"Error de validación al guardar el formulario: {e}")
    except Exception as e:
        print(f"Error general al guardar el formulario: {e}")

    return render(request, 'observadores/resgistro_de_observadores/crear.html', {'formulario': formulario, 'anio': anio, 'nombreeleccion': nombreeleccion,  'nombre_partido': nombre_partido, 'nombreedo':estado.nombre_edo,'cargo':cargoss.descrip_tcargo, **context})

def agregar_Observadores_editar(request,id, eleccion, cargo,anio):
    observador = get_object_or_404(Representantes, cdg_repre=id)
    cargoss = get_object_or_404(Tipocargo, descrip_tcargo=cargo)
    estado_id = request.session['ID_ESTADO']
    estado=get_object_or_404(Estados, idestado=estado_id)
    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido
    print(request.session['ID_USUARIO'])
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion    
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto


    formulario = Observadoresform(request.POST or None, request.FILES or None, instance=observador)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('Observadores_index')
    return render(request, 'observadores/resgistro_de_observadores/editar.html', {'formulario': formulario, 'representante': observador, 'nombreeleccion':eleccion, 'nombre_partido':nombre_partido, 'nombreedo':estado.nombre_edo,'cargo':cargoss.descrip_tcargo, 'anio': anio, **context})

def Observadores_eliminar(request, id):
  try:
    repre_obj = Representantes.objects.get(cdg_repre=id)  
    repre_obj.delete()

  except IntegrityError:
    mensaje = "No se puede eliminar Represenante, por que ya esta registrado"
    messages.error(request, mensaje)

  return redirect('Observadores_index')

def documentos_Observadores(request, id, nombreeleccion, anio, cargo):
    # Llamada al procedimiento almacenado
    estado_id = request.session['ID_ESTADO']
    estado = get_object_or_404(Estados, idestado=estado_id)
    print(request.session['ID_USUARIO'])
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion        
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

    with connection.cursor() as cursor:
        try:
            cursor.callproc('obtener_documentos_representantes', [id])
            # Recuperar los resultados del procedimiento almacenado
            resultados = cursor.fetchall()
        except Exception as e:
            print(f"Error al llamar al procedimiento almacenado: {e}")
            resultados = []

    # Obtener el objeto Candidatos correspondiente al id
    Representante = get_object_or_404(Representantes, cdg_repre=id)

    # Pasa el nombre completo del candidato a la plantilla
    nombre_completo = f"{Representante.nombre} {Representante.ap_paterno} {Representante.ap_materno}"

    return render(request, 'observadores/resgistro_de_observadores/Documentos.html', {'nombreedo':estado.nombre_edo ,'anio':anio,'cargo':cargo,'documentos_mostrar': resultados, 'nombreeleccion': nombreeleccion,  'nombre_completo': nombre_completo,**context})

def Paquetes_entrega_Cae_index (request):
     # Lógica para años
  hoy = datetime.today().date()
  año_actual = hoy.year

  print(request.session['ID_USUARIO'])
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
    context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
    context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
    context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
     context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
     context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
     context['configuracion'] = Usuario.per_configuracion      
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
  años = []
  for i in range(año_actual, año_actual+11, +1):
    años.append(i)

  return render(request, 'paquetes/entrega_CAE/Index.html', {
    
      'años': años, **context
  })



def get_paquetes_entregados_cae(request, eleccion, cargo,  id, key):
    # Obtener el estado actual desde settings
    id_estado = request.session['ID_ESTADO']
    proceso = get_object_or_404(Procesos, descrip=eleccion, idestado=id_estado)

    with connection.cursor() as cursor:
        cursor.execute("CALL Paquetes_fase2_consulta(%s, %s, %s, %s )", [proceso.idproceso, cargo, id, key])
        paquetes = cursor.fetchall()

    if len(paquetes) > 0:
        data = {'message': "Success", 'paquetes': paquetes}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)





def verificar_estatus_paquete(request, id):
    # Obtener el estado actual desde settings
    paquetes = Paquetes.objects.filter(folioc=id)
    if len(paquetes) > 0:
        data = {'message': "Success"}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)



def agregar_paquetes_entregados_cae(request , eleccion, cargo, folioc, anio,valor, ide ):
    foliocs = int(folioc);
    estado_id = request.session['ID_ESTADO']
    fecha_hora_actual_python = timezone.now()
    fecha_hora_actual_utc = timezone.now()
    # Convierte la fecha y hora actual a la zona horaria local
    fecha_hora_actual_local = timezone.localtime(fecha_hora_actual_utc)
    casilla = get_object_or_404(Casillas, folioc=folioc)
    # Obtiene solo la hora actual en formato HH:MM:SS
    hora_actual = fecha_hora_actual_local.strftime("%H:%M:%S")
    print(request.session['ID_USUARIO'])
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
    # Puedes imprimir la hora actual en la consola si lo deseas
    print("Hora actual:", hora_actual)
    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido
    estado = get_object_or_404(Estados, idestado=estado_id)
    cargo = get_object_or_404(Tipocargo, descrip_tcargo=cargo)
    eleccion = get_object_or_404(Procesos, descrip=eleccion, idestado=estado_id)
    paquete1 = get_object_or_404(PaquetesFase1, idPaquete=ide)
    print(ide)

    formulario = paquetes_Entrega_Cae(request.POST or None, request.FILES or None, initial={'idcargo_recibe': 'CAE'}, id_estado=estado_id)
    try:
            if request.method == 'POST':
                formulario = paquetes_Entrega_Cae(request.POST)
                if formulario.is_valid():
                    cargoople_id1 = formulario.cleaned_data['idcargo_entrega']
                    print(cargoople_id1)
                    cargoople1 = get_object_or_404(CatCargosOple,nombre_cargo=cargoople_id1)
                    cargoople_id2 = formulario.cleaned_data['idcargo_recibe']
                    print(cargoople_id2)
                    cargoople2 = get_object_or_404(CatCargosOple,nombre_cargo=cargoople_id2)
                    cae = formulario.cleaned_data['id_usuario']
                    print(cae)
                    caeasignado = get_object_or_404(Inicio, id_usuario = cae.id_usuario)
               
                    Paquete = formulario.save(commit=False)

                    Paquete.num_elec=paquete1.num_elec
                    Paquete.idProceso=paquete1.idProceso
                    Paquete.clave_ca=paquete1.clave_ca
                    Paquete.id_usuario = caeasignado
                    Paquete.folioc = casilla
                    Paquete.idpaquete = ide
         
                    Paquete.fecha_entrega = fecha_hora_actual_python
                    Paquete.hora_entrga = hora_actual
                    Paquete.idcargo_entrega = cargoople1
                    Paquete.idcargo_recibe = cargoople2
                    Paquete.estatus = "C"
                    
                    Paquete.save()

                return redirect('Entrega_Paquetes_CAE')
                

    except IntegrityError as e:
        print(f"Error de integridad al guardar el formulario S: {e}")
    except ValidationError as e:
        print(f"Error de validación al guardar el formularioc S: {e}")
    except Exception as e:
        print(f"Error general al guardar el formulario S: {e}")

    return render(request, 'paquetes/entrega_CAE/crear.html', {'formulario': formulario, 'paqueteno': ide, 'valor':valor, 'anio': anio, 'nombreeleccion': eleccion, 'nombrecargo': cargo,  'seccion': folioc, 'nombreedo':estado.nombre_edo, **context})



def entrega_paquetes_cae_vizualizar(request, eleccion, cargo, folioc, anio, valor, ide):
 
    estado_id = request.session['ID_ESTADO']
    fecha_hora_actual_python = timezone.now()
    fecha_hora_actual_utc = timezone.now()
        # Convierte la fecha y hora actual a la zona horaria local
    fecha_hora_actual_local = timezone.localtime(fecha_hora_actual_utc)
    casilla = get_object_or_404(Casillas, folioc=folioc)
    # Obtiene solo la hora actual en formato HH:MM:SS
    hora_actual = fecha_hora_actual_local.strftime("%H:%M:%S")
    print(request.session['ID_USUARIO'])
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion    
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

    # Puedes imprimir la hora actual en la consola si lo deseas
    print("Hora actual:", hora_actual)
    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido

    cargo = get_object_or_404(Tipocargo, descrip_tcargo=cargo)
    eleccion = get_object_or_404(Procesos, descrip=eleccion, idestado=estado_id)
    estado = get_object_or_404(Estados, idestado=estado_id)
    Paquetes = get_object_or_404(PaquetesFase2, idpaquete=ide);
    formulario = paquetes_Entrega_Cae(request.POST or None, instance=Paquetes)

    #paqueteid = get_object_or_404(PaquetesFase1.objects.filter(folioc=folioc).order_by('-idPaquete'))



    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('Entrega_Paquetes_CAE')

    return render(request, 'paquetes/entrega_CAE/editar.html', {'formulario': formulario, 'paqueteno': ide, 'valor':valor,'anio': anio, 'nombreeleccion': eleccion, 'nombrecargo': cargo,  'seccion': folioc, 'nombreedo':estado.nombre_edo, **context})



def generar_pd_Entregado_Paquetes_cae(request, anio, nombreeleccion, nombrecargo, idcand, ide):
   try: 
    # Crear un nuevo documento PDF con tamaño de ticket de supermercado (80mm x 150mm)
    ancho_mm = 80
    alto_mm = 150

    # Convertir milímetros a pulgadas
    ancho_pulgadas = ancho_mm / 25.4
    alto_pulgadas = alto_mm / 25.4

    # Convertir pulgadas a puntos
    ancho_puntos = ancho_pulgadas * 72
    alto_puntos = alto_pulgadas * 72

    pdf = FPDF(format=(ancho_puntos, alto_puntos))


    # Establecer márgenes de página
    pdf.set_auto_page_break(auto=True, margin=2)  # Auto salto de página con un margen de 2mm
    pdf.set_margins(left=10, top=10, right=10)     # Márgenes izquierdo y derecho de 10mm, superior de 10mm

    # Agregar una página en blanco
    pdf.add_page()

    # Obtener datos del estado, partido y candidato
    id_estado = request.session['ID_ESTADO']
    id_partido = request.session['ID_PARTIDO']
    ople = get_object_or_404(Oples, idestado=id_estado)
    estado = get_object_or_404(Estados, idestado=id_estado)
    partido = get_object_or_404(Partidos, idpartido=id_partido)
    casilla = get_object_or_404(Casillas, folioc=idcand)
    proceso = get_object_or_404(Procesos, descrip=nombreeleccion, idestado=id_estado)
    cargo = get_object_or_404(Tipocargo, descrip_tcargo=nombrecargo)
    eleccion = get_object_or_404(
         Procesoscargo,
         Q(idDistrito=casilla.iddistrito.iddistrito) | Q(idMunicipio=casilla.idmunicipio.idmunicipio),
         idproceso=proceso.idproceso,
         idestado=id_estado,
         idtipo_cargo=cargo.idtipo_cargo
            )   
    print(idcand)
    PaquetesFaseuno = get_object_or_404(PaquetesFase2, idpaquete=ide)


    paqueteno = get_object_or_404(PaquetesFase1.objects.filter(idPaquete=ide).order_by('-idPaquete'))
    paquetedos =get_object_or_404(PaquetesFase2.objects.filter(idpaquete=ide))
    # Establecer el tamaño y tipo de fuente
    pdf.set_font('Arial', '', 14)
    
    # Obtener la fecha y hora actual en la zona horaria local
    # Obtener la fecha actual en español
    fecha_actual = datetime.now().strftime('%d/%m/%Y')
    fecha_entrega_formatted = PaquetesFaseuno.fecha_entrega.strftime('%d/%m/%Y')

    # Agregar el logo en la esquina superior izquierda
    pdf.image(ople.logo.path, x=92, y=8, w=45)
    pdf.ln(50)
    
    # Agregar título y detalles
    pdf.cell(0, 10, ople.nombre_completo, 0, 1, 'C')
    pdf.cell(0, 7, "Reporte de Entrega a los CAES", 0, 1, 'C')  # Aumentar espacio entre líneas
    pdf.cell(0, 7, "Número de Paquete: "+ str(paqueteno.idPaquete), 0, 1, 'C')
    pdf.cell(0, 7, estado.nombre_edo, 0, 1, 'C')
    pdf.cell(0, 7, nombreeleccion, 0, 1, 'C')
    pdf.cell(0, 7, nombrecargo, 0, 1,'C' )
    pdf.cell(0, 7, "Distrito: "+str(casilla.iddistrito),0, 1,'C')
    pdf.cell(0, 7, "Municipio: "+str(casilla.idmunicipio),0, 1,'C')
    pdf.ln(5)
    pdf.ln(10)
    pdf.cell(0, 7, "Fecha de Impresión: " + fecha_actual, 0, 1, )
    pdf.ln(5)
    pdf.cell(0, 7, "Sección: " + idcand, 0, 1, )

    pdf.cell(0, 7, "Fecha de entrega: " + fecha_entrega_formatted, 0, 1, )
    pdf.cell(0, 7, "Hora de entrega: " + str(PaquetesFaseuno.hora_entrga), 0, 1, )
    pdf.cell(0, 7, "Entregó el Paquete: " + str(PaquetesFaseuno.nombre_cargo_entrega), 0, 1, )
    pdf.cell(0, 7, "Cargo: " + str(PaquetesFaseuno.idcargo_entrega), 0, 1, )
    pdf.cell(0, 7, "Recibió el Paquete: " + str(PaquetesFaseuno.id_usuario), 0, 1, )
    pdf.cell(0, 7, "Cargo: " + str(PaquetesFaseuno.idcargo_recibe), 0, 1, )

        # Calcular la cantidad de espacio en blanco necesaria entre la tabla y el título del código QR
    space_needed = 10  # Puedes ajustar este valor según sea necesario

        # Agregar espacio en blanco debajo de la tabla para separarla del título del código QR
    pdf.ln(space_needed)

        # Agregar título del código QR
    pdf.set_xy(2, 235)  # Ajustar según sea necesario
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, "QR Paquete:                                                                           QR Reporte:", 0, 1, 'C')

        # Agregar espacio en blanco antes del código QR
    pdf.ln(5)

        # Obtener la posición Y después de agregar el título y el espacio en blanco
    pdf_y_qr_start = pdf.get_y()

        # Generar el primer código QR con datos estáticos para probar
    qr_data_dynamic = (
            str(anio)+"|"+ str(id_estado)+"|"+ str(proceso.idproceso)+"|"+str(cargo.idtipo_cargo)+"|"+str(cargo.idtipoc.idtipoc)+"|"+str(eleccion.num_elec)+"|"+str(casilla.folioc)+"|"+str(paquetedos.id_usuario.id_usuario)+"|"+str(paqueteno.idPaquete)
        )

        # Crear el primer código QR con los datos dinámicos
    qr_dynamic = qrcode.make(qr_data_dynamic)
    qr_stream_dynamic = BytesIO()
    qr_dynamic.save(qr_stream_dynamic, 'PNG')
        
        # Establecer la posición para agregar el primer código QR en el PDF
    pdf_x = 30
    pdf_y = pdf_y_qr_start + 5

        # Crear un archivo temporal para almacenar el primer código QR
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmpfile:
            # Guardar el contenido de qr_stream_dynamic en el archivo temporal
            tmpfile.write(qr_stream_dynamic.getvalue())
            # Obtener la ruta del archivo temporal
            tmp_filename = tmpfile.name

        # Agregar el primer código QR al PDF desde el archivo temporal
    pdf.image(tmp_filename, x=pdf_x, y=pdf_y, w=50)

        # Eliminar el archivo temporal después de usarlo
    os.unlink(tmp_filename)

    # Calcular la cantidad de espacio en blanco necesaria entre la tabla y el código QR
    space_needed = 5  # Puedes ajustar este valor según sea necesario

    # Agregar espacio en blanco debajo de la tabla para separarla del código QR
    pdf.ln(space_needed)

    # Obtener la posición Y después de agregar el espacio en blanco
    pdf_y_qr_start = pdf.get_y()

    # Generar el código QR con datos estáticos para probar
    qr_data_dynamic = (ople.nombre_completo
                   + "\n"
                   +"Reporte de Entrega a los CAES"
                   + "\n"
                   +"Año: " + str(anio)
                   + "\n"
                   + estado.nombre_edo
                   + "\n"
                   +"Elección: "+ nombreeleccion
                   + "\n"
                   + "Cargo: "+nombrecargo
                   + "\n"
                   + "Municipio: "+str(casilla.idmunicipio)
                   + "\n"
                   + "\n"
                   + "\n"
                   + "Sección: " + idcand
                   + "\n"
                   + "Fecha Actual: " + fecha_actual
                   + "\n"
                   + "\n"
                   + "Fecha de entrega: " + fecha_entrega_formatted
                   + "\n"
                   + "Hora de entrega: " + str(PaquetesFaseuno.hora_entrga)
                   + "\n"
                   + "Entregó el Paquete: " + str(PaquetesFaseuno.nombre_cargo_entrega)
                   + "\n"
                   + "Cargo: " + str(PaquetesFaseuno.idcargo_entrega)
                   + "\n"
                   + "Recibió el Paquete: " + str(PaquetesFaseuno.id_usuario)
                   + "\n"
                   + "Cargo: " + str(PaquetesFaseuno.idcargo_recibe)
                   )


    # Crear el código QR con los datos dinámicos
    qr_dynamic = qrcode.make(qr_data_dynamic)
    qr_stream_dynamic = BytesIO()
    qr_dynamic.save(qr_stream_dynamic, 'PNG')
    
    # Establecer la posición para agregar el código QR en el PDF

    pdf_y_qr_full_start = pdf.get_y() 

    # Crear un archivo temporal para almacenar el código QR
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmpfile:
        # Guardar el contenido de qr_stream_static en el archivo temporal
        tmpfile.write(qr_stream_dynamic.getvalue())
        # Obtener la ruta del archivo temporal
        tmp_filename = tmpfile.name

    # Agregar el código QR al PDF desde el archivo temporal
    pdf.image(tmp_filename, x=141, y=pdf_y_qr_full_start, w=50)

    # Eliminar el archivo temporal después de usarlo
    os.unlink(tmp_filename)

    # Guardar el PDF en un objeto de bytes
    pdf_data = pdf.output(dest='S').encode('latin1')
    # Devolver el PDF como respuesta
    response = HttpResponse(pdf_data, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Reporte_Entrega_Paquete_al_cae.pdf"'
    return response
   except Exception as e:
 # Capturar el traceback completo del error
        error_traceback = traceback.format_exc()

        # Mostrar el error y el traceback en la consola
        print(f"Ocurrió un error: {e}")
        print(f"Traceback completo:\n{error_traceback}")

        # Puedes regresar una respuesta de error o manejarlo según lo necesites
        return HttpResponse(f"Error al generar el PDF: {e}", status=500)



def Paquetes_entrega_Casilla (request):
     # Lógica para años
  hoy = datetime.today().date()
  año_actual = hoy.year
  print(request.session['ID_USUARIO'])
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])
  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion      
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
  años = []
  for i in range(año_actual, año_actual+11, +1):
    años.append(i)

  return render(request, 'paquetes/entrega_paquetes/Index.html', {
    
      'años': años,
      **context
  })

def get_paquetes_entregados_casilla(request, eleccion, cargo, id, key):
    # Obtener el estado actual desde settings
    id_estado = request.session['ID_ESTADO']
    proceso = get_object_or_404(Procesos, descrip=eleccion, idestado=id_estado)

    with connection.cursor() as cursor:
        cursor.execute("CALL Paquetes_fase3_consulta(%s, %s,%s, %s)", [proceso.idproceso, cargo, id, key])
        paquetes = cursor.fetchall()

    if len(paquetes) > 0:
        data = {'message': "Success", 'paquetes': paquetes}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)


def agregar_paquetes_entregados_casillas(request, eleccion, cargo, folioc, anio, valor, ide):
    estado_id = request.session['ID_ESTADO']
    #foliocs = int(folioc);
    fecha_hora_actual_python = timezone.now()
    fecha_hora_actual_utc = timezone.now()
    # Convierte la fecha y hora actual a la zona horaria local
    fecha_hora_actual_local = timezone.localtime(fecha_hora_actual_utc)
    # casilla = get_object_or_404(Casillas, folioc=folioc)
    # Obtiene solo la hora actual en formato HH:MM:SS
    hora_actual = fecha_hora_actual_local.strftime("%H:%M:%S")

    print(request.session['ID_USUARIO'])
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion    
    # Puedes imprimir la hora actual en la consola si lo deseas
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto    
    print("Hora actual:", hora_actual)
    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido
    estado = get_object_or_404(Estados, idestado=estado_id)
    cargo = get_object_or_404(Tipocargo, descrip_tcargo=cargo)
    eleccion = get_object_or_404(Procesos, descrip=eleccion, idestado=estado_id)
    paquete2 = get_object_or_404(PaquetesFase2, idpaquete=ide)
    print('es la centro : '+str(paquete2.clave_ca))
    num_eleeccion = get_object_or_404(Procesoscargo, num_elec=paquete2.num_elec.num_elec)
    print("el valor que etsa sbuscando es: "+ str(num_eleeccion.idtipo_cargo.idtipo_cargo))

    if int(num_eleeccion.idtipo_cargo.idtipo_cargo) == 1:
        descricionproceso ='Presidencias Municipales'
        descripcioncargo= 'Presidencia Municipal '+valor
        
    else:
         descricionproceso ='Pendiente'
         descripcioncargo = 'Pendiente'
   

    if request.method == 'POST':
        formulario = CAESEntregaalosPresidentes(request.POST)

        if formulario.is_valid():
           
            id_entrega = formulario.cleaned_data['id_cargo_entrega'].idcargoople
            id_recipe = formulario.cleaned_data['id_cargo_recive'].id_cargo_entrega
            print(id_entrega)
            print(id_recipe)
            cargo_entrega = CatCargosOple.objects.get(idcargoople=id_entrega)
            cargo_recive = CargosEntrega.objects.get(id_cargo_entrega=id_recipe)
            #print('HOLAAAAAAA')


            fecha_actual = datetime.now().strftime("%Y-%m-%d") 
            paquete_cae = formulario.save(commit=False)
            Casilla= Casillas.objects.get(folioc=folioc)

                   
            paquete_cae.clave_ca=paquete2.clave_ca
            paquete_cae.idProceso=paquete2.idProceso
            paquete_cae.num_elec=paquete2.num_elec
            paquete_cae.idPaquete=paquete2.idpaquete
            paquete_cae.folioc = Casilla
            paquete_cae.id_cargo_entrega = cargo_entrega
            paquete_cae.id_cargo_recive = cargo_recive
            paquete_cae.hora = hora_actual
            paquete_cae.fecha = fecha_actual

            paquete_cae.save()
        try:
            # Obtener la instancia a actualizar
            nuevo_bi = CadenaCustodiaBi(
            descrip_proceso=descricionproceso,
            cargo=descripcioncargo,
            anio=anio,
            country='MEXICO',
            city=estado.nombre_edo,
            nombre_mpo=valor,
            casilla=Casilla.folioc,
            id_distrito=Casilla.iddistrito.iddistrito,
            id_cae=paquete2.id_usuario.id_usuario,
            id_paquete=paquete2.idpaquete,
            clave_ca=paquete2.clave_ca.Clave_ca,
            )
        
            # Guardar la nueva instancia en la base de datos
            nuevo_bi.save()


            # Supongamos que ya has importado el modelo Paquetes y los modelos relacionados necesarios.

            paquetebeta = Paquetes(
            idpaquete=paquete2.idpaquete,  # Llave primaria, campo obligatorio
            folioc=Casilla,
            num_elec=paquete2.num_elec,
            idproceso=paquete2.idProceso
            )
            paquetebeta.save()



            return redirect('Entrega_Paquetes_Casilla_index')
        except Exception as e:
            # Imprimir el error en consola, pero no detener el proceso
            print(f"Error al actualizar o guardar CadenaCustodiaBi: {e}")

            return redirect('Entrega_Paquetes_Casilla_index')

    else:
        formulario = CAESEntregaalosPresidentes(request.POST or None, request.FILES or None, initial={'id_cargo_entrega': 'CAE', 'id_usuario': paquete2.id_usuario})

    return render(request, 'paquetes/entrega_paquetes/crear.html', {'formulario': formulario, 'paqueteno': ide,'anio': anio, 'nombreeleccion': eleccion, 'nombrecargo': cargo, 'seccion': folioc, 'nombreedo':estado.nombre_edo, 'valor':valor, **context})





def Vizualizar_paquetes_entregados_casillas(request, eleccion, cargo, folioc, anio, valor, ide):

  estado_id = request.session['ID_ESTADO']
  
  fecha_hora_actual_python = timezone.now()

  fecha_hora_actual_utc = timezone.now()
  
  # Convierte la fecha y hora actual a la zona horaria local
  fecha_hora_actual_local = timezone.localtime(fecha_hora_actual_utc)

  #casilla = get_object_or_404(Casillas, folioc=folioc)

  #paquetef2 = get_object_or_404(PaquetesFase2, folioc=folioc)

  paquetef3 = PackElecFase3.objects.get(idPaquete=ide)
  formulario = CAESEntregaalosPresidentes(request.POST or None, request.FILES or None, instance= paquetef3)

   
  # Obtiene solo la hora actual en formato HH:MM:SS
  hora_actual = fecha_hora_actual_local.strftime("%H:%M:%S")
  print(request.session['ID_USUARIO'])
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion    
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
 

  # Puedes imprimir la hora actual en la consola si lo deseas
  print("Hora actual:", hora_actual)
  
  idpartido = request.session['ID_PARTIDO']
  
  partido = Partidos.objects.get(idpartido=idpartido)
 
  nombre_partido = partido.desc_partido

  #cargo = get_object_or_404(Tipocargo, descrip_tcargo=cargo)
  estado = get_object_or_404(Estados, idestado=estado_id)
  eleccion = get_object_or_404(Procesos, descrip=eleccion, idestado=estado_id)

  if formulario.is_valid() and request.POST:
    formulario.save()
    
    return redirect('Entrega_Paquetes_Casilla_index')
  
  return render(request, 'paquetes/entrega_paquetes/editar.html', {'formulario': formulario, 'anio': anio, 'nombreeleccion': eleccion, 'nombrecargo': cargo, 'seccion': folioc, 'nombreedo':estado.nombre_edo,'valor':valor, 'paqueteno': ide, **context})




def generar_pd_Entregado_Paquetes_casilla(request, anio, nombreeleccion, nombrecargo, idcand, ide):
   try:
    # Crear un nuevo documento PDF con tamaño de ticket de supermercado (80mm x 150mm)
    ancho_mm = 80
    alto_mm = 150

    # Convertir milímetros a pulgadas
    ancho_pulgadas = ancho_mm / 25.4
    alto_pulgadas = alto_mm / 25.4

    # Convertir pulgadas a puntos
    ancho_puntos = ancho_pulgadas * 72
    alto_puntos = alto_pulgadas * 72

    pdf = FPDF(format=(ancho_puntos, alto_puntos))


    # Establecer márgenes de página
    pdf.set_auto_page_break(auto=True, margin=2)  # Auto salto de página con un margen de 2mm
    pdf.set_margins(left=10, top=10, right=10)     # Márgenes izquierdo y derecho de 10mm, superior de 10mm

    # Agregar una página en blanco
    pdf.add_page()

    # Obtener datos del estado, partido y candidato
    id_estado = request.session['ID_ESTADO']
    id_partido = request.session['ID_PARTIDO']
    ople = get_object_or_404(Oples, idestado=id_estado)
    estado = get_object_or_404(Estados, idestado=id_estado)
    partido = get_object_or_404(Partidos, idpartido=id_partido)
    print(idcand)
    PaquetesFasedos = get_object_or_404(PaquetesFase2, idpaquete=ide)
    PaquetesFasetres = get_object_or_404(PackElecFase3, idPaquete=ide)
    proceso = get_object_or_404(Procesos, descrip=nombreeleccion, idestado=id_estado)
    cargo = get_object_or_404(Tipocargo, descrip_tcargo=nombrecargo)
    casilla = get_object_or_404(Casillas, folioc=idcand)
    eleccion = get_object_or_404(
         Procesoscargo,
         Q(idDistrito=casilla.iddistrito.iddistrito) | Q(idMunicipio=casilla.idmunicipio.idmunicipio),
         idproceso=proceso.idproceso,
         idestado=id_estado,
         idtipo_cargo=cargo.idtipo_cargo
            )
    folioc = PaquetesFase2.objects.filter(folioc=idcand).values_list('folioc', flat=True).first()
    
    # Establecer el tamaño y tipo de fuente
    pdf.set_font('Arial', '', 14)
    
    # Obtener la fecha y hora actual en la zona horaria local
    # Obtener la fecha actual en español
    fecha_actual = datetime.now().strftime('%d/%m/%Y')
    fecha_entrega_formatted = PaquetesFasetres.fecha.strftime('%d/%m/%Y')

    # Agregar el logo en la esquina superior izquierda
    pdf.image(ople.logo.path, x=92, y=8, w=45)
    pdf.ln(50)
    
    # Agregar título y detalles
    pdf.cell(0, 10, ople.nombre_completo, 0, 1, 'C')
    pdf.cell(0, 7, "Paquete Entregado al Presidente de Casilla", 0, 1, 'C')  # Aumentar espacio entre líneas
    pdf.cell(0, 7, "Número de Paquete: "+ str(PaquetesFasetres.idPaquete), 0, 1, 'C')
    pdf.cell(0, 7, estado.nombre_edo, 0, 1, 'C')
    pdf.cell(0, 7, nombreeleccion, 0, 1, 'C')
    pdf.cell(0, 7, nombrecargo, 0, 1,'C' )
    pdf.cell(0, 7, "Distrito: "+str(casilla.iddistrito),0, 1,'C')
    pdf.cell(0, 7, "Municipio: "+str(casilla.idmunicipio),0, 1,'C')
    pdf.ln(5)
    
    pdf.ln(10)
    pdf.cell(0, 7, "Fecha de Impresión: " + fecha_actual, 0, 1, )
    pdf.ln(5)
    pdf.cell(0, 7, "Sección: " + folioc, 0, 1, )

    pdf.cell(0, 7, "Fecha de entrega: " + fecha_entrega_formatted, 0, 1, )
    pdf.cell(0, 7, "Hora de entrega: " + str(PaquetesFasetres.hora), 0, 1, )
    pdf.cell(0, 7, "Entregó el Paquete: " + str(PaquetesFasetres.nombre_entrega), 0, 1, )
    pdf.cell(0, 7, "Cargo: " + str(PaquetesFasetres.id_cargo_entrega), 0, 1, )
    pdf.cell(0, 7, "Recibió el Paquete: " + str(PaquetesFasetres.nombre_recibe), 0, 1, )
    pdf.cell(0, 7, "Cargo: " + str(PaquetesFasetres.id_cargo_recive), 0, 1, )
    
    if PaquetesFasetres.estatus == 'S':
        texto = "Si"
    elif PaquetesFasetres.estatus == 'N':
         texto = "No"
    else:
         texto = ""

    pdf.cell(0, 7, "Se entregó el Paquete: " + texto, 0, 1)

    # Calcular la cantidad de espacio en blanco necesaria entre la tabla y el código QR
    space_needed = 5  # Puedes ajustar este valor según sea necesario

    # Agregar espacio en blanco debajo de la tabla para separarla del código QR
    pdf.ln(space_needed)

       # Agregar título del código QR
    pdf.set_xy(2, 235)  # Ajustar según sea necesario
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, "QR Paquete:                                                                           QR Reporte:", 0, 1, 'C')

        # Agregar espacio en blanco antes del código QR
    pdf.ln(5)

        # Obtener la posición Y después de agregar el título y el espacio en blanco
    pdf_y_qr_start = pdf.get_y()

        # Generar el primer código QR con datos estáticos para probar
    qr_data_dynamic = (
            str(anio)+"|"+ str(id_estado)+"|"+ str(proceso.idproceso)+"|"+str(cargo.idtipo_cargo)+"|"+str(cargo.idtipoc.idtipoc)+"|"+str(eleccion.num_elec)+"|"+str(casilla.folioc)+"|"+str(PaquetesFasedos.id_usuario.id_usuario)+"|"+str(PaquetesFasetres.idPaquete)
        )
      
        # Crear el primer código QR con los datos dinámicos
    qr_dynamic = qrcode.make(qr_data_dynamic)
    qr_stream_dynamic = BytesIO()
    qr_dynamic.save(qr_stream_dynamic, 'PNG')
        
        # Establecer la posición para agregar el primer código QR en el PDF
    pdf_x = 30
    pdf_y = pdf_y_qr_start + 5

        # Crear un archivo temporal para almacenar el primer código QR
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmpfile:
            # Guardar el contenido de qr_stream_dynamic en el archivo temporal
            tmpfile.write(qr_stream_dynamic.getvalue())
            # Obtener la ruta del archivo temporal
            tmp_filename = tmpfile.name

        # Agregar el primer código QR al PDF desde el archivo temporal
    pdf.image(tmp_filename, x=pdf_x, y=pdf_y, w=50)

        # Eliminar el archivo temporal después de usarlo
    os.unlink(tmp_filename)



    # Obtener la posición Y después de agregar el espacio en blanco
    pdf_y_qr_start = pdf.get_y()

    # Generar el código QR con datos estáticos para probar
    qr_data_dynamic = (ople.nombre_completo
                   + "\n"
                   +"Ticket CAES Entrega a los Presidentes de casilla"
                   + "\n"
                   +"Año: " + str(anio)
                   + "\n"
                   + estado.nombre_edo
                   + "\n"
                   + "Elección: "+nombreeleccion
                   + "\n"
                   + "Cargo: "+ nombrecargo
                   + "\n"
                   + "Municipio: "+str(casilla.idmunicipio)
                   + "\n"
                   + "\n"
                   + "\n"
                   + "Sección: " + folioc
                     + "\n"
                   +"Cargo en Disputa: " + nombrecargo
                     + "\n"
                   +"Eleccion en Disputa: " + nombreeleccion

                   + "\n"
                   + "Fecha Actual: " + fecha_actual
                   + "\n"
                   + "\n"
                   + "Fecha de entrega: " + fecha_entrega_formatted
                   + "\n"
                   + "Hora de entrega: " + str(PaquetesFasetres.hora)
                   + "\n"
                   + "Entregó el Paquete: " + str(PaquetesFasetres.nombre_entrega)
                   + "\n"
                   + "Cargo: " + str(PaquetesFasetres.id_cargo_entrega)
                   + "\n"
                   + "Recibió el Paquete: " +str(PaquetesFasetres.nombre_recibe)
                   + "\n"
                   + "Cargo: " + str(PaquetesFasetres.id_cargo_recive)
                   + "\n"
                   +"Se entregó el Paquete: " + texto
                   )


    # Crear el código QR con los datos dinámicos
    qr_dynamic = qrcode.make(qr_data_dynamic)
    qr_stream_dynamic = BytesIO()
    qr_dynamic.save(qr_stream_dynamic, 'PNG')
    
    # Establecer la posición para agregar el código QR en el PDF
    pdf_x = 80
    pdf_y_qr_full_start = pdf.get_y() + 5

    # Crear un archivo temporal para almacenar el código QR
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmpfile:
        # Guardar el contenido de qr_stream_static en el archivo temporal
        tmpfile.write(qr_stream_dynamic.getvalue())
        # Obtener la ruta del archivo temporal
        tmp_filename = tmpfile.name

    # Agregar el código QR al PDF desde el archivo temporal
    pdf.image(tmp_filename, x=141, y=pdf_y_qr_full_start, w=50)


    # Eliminar el archivo temporal después de usarlo
    os.unlink(tmp_filename)

    # Guardar el PDF en un objeto de bytes
    pdf_data = pdf.output(dest='S').encode('latin1')
    # Devolver el PDF como respuesta
    response = HttpResponse(pdf_data, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Reporte_Entrega_Casilla_Paquete.pdf"'
    return response
   except Exception as e:
        # Manejo de excepciones
        return HttpResponse(f"Error al generar el PDF: {e}", status=500)




def Paquetes_recoleccion_Casilla (request):
     # Lógica para años
  hoy = datetime.today().date()
  año_actual = hoy.year
  print(request.session['ID_USUARIO'])
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion    
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

  años = []
  for i in range(año_actual, año_actual+11, +1):
    años.append(i)

  return render(request, 'paquetes/paquetes_electorales/Index.html', {
    
      'años': años,
      **context
  })


def get_paquetes_recolectados_casilla(request, eleccion, cargo, id, key):
    # Obtener el estado actual desde settings
    id_estado = request.session['ID_ESTADO']
    proceso = get_object_or_404(Procesos, descrip=eleccion, idestado=id_estado)

    with connection.cursor() as cursor:
        cursor.execute("CALL Paquetes_fase4_consulta(%s, %s, %s, %s)", [proceso.idproceso, cargo, id, key])
        paquetes = cursor.fetchall()

    if len(paquetes) > 0:
        data = {'message': "Success", 'paquetes': paquetes}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)



def agregar_paquetes_recolectados_casillasbeta(request, eleccion, cargo, folioc, anio, valor, ide):
    estado_id = request.session['ID_ESTADO']

    fecha_hora_actual_python = timezone.now()
    fecha_hora_actual_utc = timezone.now()
    # Convierte la fecha y hora actual a la zona horaria local
    fecha_hora_actual_local = timezone.localtime(fecha_hora_actual_utc)
    casilla = get_object_or_404(Casillas, folioc=folioc)
    foliocs = int(folioc);
    # Convertir a la zona horaria local
    fecha_hora_actual_local = timezone.localtime(fecha_hora_actual_utc)
    print(request.session['ID_USUARIO'])
    paquete3 = get_object_or_404(PackElecFase3, idPaquete=ide)

    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])
    formulario = paquetesfasee4(request.POST or None, request.FILES or None, initial={'id_cargo_entrega': 'CAE', 'id_usuario':paquete3.id_usuario})

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion   
    # Obtener solo la fecha en formato día, mes y año
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto    
    fecha_solo = fecha_hora_actual_local.strftime('%d/%m/%Y')

    # Obtiene solo la hora actual en formato HH:MM:SS
    hora_actual = fecha_hora_actual_local.strftime("%H:%M:%S")


    # Puedes imprimir la hora actual en la consola si lo deseas
    print("Hora actual:", hora_actual)

    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido

    cargo = get_object_or_404(Tipocargo, descrip_tcargo=cargo)
    eleccion = get_object_or_404(Procesos, descrip=eleccion, idestado=estado_id)
    estado = get_object_or_404(Estados, idestado=estado_id)
  

    if request.method == 'POST':
        formulario = paquetesfasee4(request.POST, request.FILES)
        if formulario.is_valid():

            paquete = formulario.save(commit=False)

            paquetebeta = Paquetes.objects.get(idpaquete=paquete3.idPaquete)
            paquetebeta.delete()

            con_firma = formulario.cleaned_data.get('con_firma')
            sin_muestras_alteracion = formulario.cleaned_data.get('sin_muestras_alteracion')
            cinta_etiqueta_seguridad = formulario.cleaned_data.get('cinta_etiqueta_seguridad')
            sobre_prep = formulario.cleaned_data.get('sobre_prep')
            bolsa_por_fuera = formulario.cleaned_data.get('bolsa_por_fuera')
            id_entrega = formulario.cleaned_data.get('id_cargo_entrega')
            id_resepcion = formulario.cleaned_data.get('id_cargo_recepcion')

            # Aquí se ajustan los valores
            paquete.clave_ca = paquete3.clave_ca
            paquete.idProceso = paquete3.idProceso
            paquete.num_elec = paquete3.num_elec
            paquete.idpaquete = paquete3.idPaquete  # Usar idPaquete en lugar de iPpaquete
            paquete.folioc = casilla
            paquete.id_cargo_entrega = id_entrega
            paquete.id_cargo_recepcion = id_resepcion
            paquete.idtipo_cargo = cargo
            paquete.anio = anio
            paquete.idproceso = eleccion
            paquete.idestado = estado
            paquete.fecha_hora_entrega = fecha_hora_actual_python
            paquete.foto_entrega = request.FILES.get('foto_entrega')
            paquete.foto_acta = request.FILES.get('foto_acta')

            try:
                paquete.save()
            except Exception as e:
                print(f"Error al guardar el paquete: {e}")

            # Ajustar valores según los casos
            con_firma = 'SI' if con_firma == 'S' else 'NO'
            sin_muestras_alteracion = 'SI' if sin_muestras_alteracion == 'S' else 'NO'
            cinta_etiqueta_seguridad = 'SI' if cinta_etiqueta_seguridad == 'S' else 'NO'
            sobre_prep = 'SI' if sobre_prep == 'S' else 'NO'
            bolsa_por_fuera = 'SI' if bolsa_por_fuera == 'S' else 'NO'

            try:
                Bi = get_object_or_404(CadenaCustodiaBi, id_paquete=paquete3.idPaquete)  # Cambiar a idPaquete

                Bi.con_firma = con_firma
                Bi.sin_muestras_alteracion = sin_muestras_alteracion
                Bi.cinta_etiqueta_seguridad = cinta_etiqueta_seguridad
                Bi.sobre_prep = sobre_prep
                Bi.bolsa_por_fuera = bolsa_por_fuera

                Bi.save()
            except Exception as e:
                print(f"Error al actualizar o guardar CadenaCustodiaBi: {e}")

            return redirect('Entrega_Paquetes_Casilla_Recoleccion')
    else:
        print(f"Errores en el formulario: {formulario.errors}")


    return render(request, 'paquetes/paquetes_electorales/crear.html', {
        'formulario': formulario,
        'valor': valor,
        'anio': anio,
        'nombreeleccion': eleccion,
        'nombrecargo': cargo,
        'seccion': folioc,
        'paqueteno': ide,
        'nombreedo': estado.nombre_edo,
        **context
    })


def agregar_paquetes_recolectados_casillasbeta_viwes(request, eleccion, cargo, folioc, anio, valor, ide):
    estado_id = request.session['ID_ESTADO']
    fecha_hora_actual_python = timezone.now()
    fecha_hora_actual_utc = timezone.now()
    # Convierte la fecha y hora actual a la zona horaria local
    fecha_hora_actual_local = timezone.localtime(fecha_hora_actual_utc)
    casilla = get_object_or_404(Casillas, folioc=folioc)
    print(request.session['ID_USUARIO'])
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])
    

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion        
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto    
    
    cargos_entrega_casilla = get_object_or_404(CargosEntregaCasilla, folioc=folioc, id_cargo_entrega='PR' )
    cargos_entrega_casilla2 = get_object_or_404(CargosEntregaCasilla, folioc=folioc, id_cargo_entrega='RC' )
    Paquetesfase4 = get_object_or_404(Paquetes, idpaquete=ide)
    formulario = paquetesfasee4(instance=Paquetesfase4)
    # Obtiene solo la hora actual en formato HH:MM:SS
    hora_actual = fecha_hora_actual_local.strftime("%H:%M:%S")



    # Puedes imprimir la hora actual en la consola si lo deseas
    print("Hora actual:", hora_actual)
    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido

    cargo = get_object_or_404(Tipocargo, descrip_tcargo=cargo)
    eleccion = get_object_or_404(Procesos, descrip=eleccion, idestado=estado_id)
    estado = get_object_or_404(Estados, idestado=estado_id)

    if request.method == 'POST':
                formulario = paquetesfasee4(request.POST)
                if formulario.is_valid():
                    Paquete = formulario.save(commit=False)

                    Paquete.folioc = casilla
                    Paquete.idtipo_cargo= cargo
                    Paquete.idproceso=eleccion
                    Paquete.idestado=estado
                    Paquete.fecha_hora_entrega = fecha_hora_actual_python
                    Paquete.foto_entrega = request.FILES.get('foto_entrega')
                    Paquete.foto_acta = request.FILES.get('foto_acta')
                    Paquete.save()

                return redirect('Entrega_Paquetes_Casilla_Recoleccion')

    else:
    
        print(f"Errores en el formulario: {formulario.errors}")



    return render(request, 'paquetes/paquetes_electorales/editar.html', {'formulario': formulario,'valor':valor, 'anio': anio, 'nombreeleccion': eleccion, 'nombrecargo': cargo, 'seccion': folioc,'nombreedo':estado.nombre_edo,'paqueteno': ide, **context})




def Resumen_de_paquetes (request):
     # Lógica para años
  hoy = datetime.today().date()
  año_actual = hoy.year
  print(request.session['ID_USUARIO'])
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion   
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

  años = []
  for i in range(año_actual, año_actual+11, +1):
    años.append(i)

  return render(request, 'paquetes/resumen_de_paquetes/Index.html', {
    
      'años': años,
      **context

  })




def Recorrido_de_paquetes (request):
     # Lógica para años
  hoy = datetime.today().date()
  año_actual = hoy.year
  print(request.session['ID_USUARIO'])
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion   
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

  años = []
  for i in range(año_actual, año_actual+11, +1):
    años.append(i)

  return render(request, 'paquetes/recorrido_paquetes/Index.html', {
    
      'años': años,
      **context

  })

def Recorrido_de_paquetes_editar(request, id_paquetetranslado, estado, anio, eleccion, cargo, paqueteid):
    print(id_paquetetranslado)
    print(estado)
    print(anio)
    print(eleccion)
    print(cargo)

    # Realiza la consulta SQL cruda
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT Nombre, Apaterno, Amaterno 
            FROM dbsite.inicio 
            WHERE id_usuario = (
                SELECT id_usuario 
                FROM transladado_paquetes 
                WHERE id_paquetetranslado = %s
            )
        """, [id_paquetetranslado])
        row = cursor.fetchone()

    if row:
        nombre, apaterno, amaterno = row
        nombre_completo = f"{nombre} {apaterno} {amaterno}"
    else:
        print('erorr: 201')

    # Obtén el objeto Usuario basado en la sesión (mantén esta lógica)
    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {
        'nombrecae': nombre_completo,
    }

    if Usuario.per_regiscandidatura is not None:
        context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion

    doc = Tipodoc.objects.all()
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)

    try:
     inicioRecorrido = TransladadoPaquete.objects.get(idPaquete=paqueteid, estatus='Inicio')
     context['inicioR']=[inicioRecorrido]
    except TransladadoPaquete.DoesNotExist:
     print('No se ecotraron de inicio')   
    try:
     rutaRecorrido = TransladadoPaquete.objects.filter(idPaquete=paqueteid, estatus='Ruta')
     context['rutaR']=rutaRecorrido
    except TransladadoPaquete.DoesNotExist:
     print('No se ecotraron de ruta')   
    try:
     rutaEntrega = TransladadoPaquete.objects.filter(idPaquete=paqueteid, estatus='Llego')
     context['llegoR']=rutaEntrega
    except TransladadoPaquete.DoesNotExist:
     print('No se ecotraron de ruta')    
    try:
     rutaIncidencia = TransladadoPaquete.objects.filter(idPaquete=paqueteid, estatus='Incidencia')
     context['incidenciaR']=rutaIncidencia
    except TransladadoPaquete.DoesNotExist:
     print('No se ecotraron Incidencias de ruta') 
      
    try:
     rutaEmergencia = TransladadoPaquete.objects.get(idPaquete=paqueteid, estatus='Emergencia')
     context['emergenciaR']=[rutaEmergencia ]
    except TransladadoPaquete.DoesNotExist:
     print('No se ecotraron Emergencias  de ruta') 
    try:
     rutaEntrega = TransladadoPaquete.objects.filter(idPaquete=paqueteid, estatus='Llego')
     context['llegoR']=rutaEntrega
    except TransladadoPaquete.DoesNotExist:
     print('No se ecotraron de ruta') 
    try:
     rutaEntrego = TransladadoPaquete.objects.get(idPaquete=paqueteid, estatus='Entregado')
     context['entregaR']=[rutaEntrego]
    except TransladadoPaquete.DoesNotExist:
     print('No se ecotraron Entregas')      


    context['logo'] = logos.logo
    context['idpaquete'] = paqueteid
    context['años'] = [anio]
    context['entidad_federativa']=[estado]
    context['eleccion']=[eleccion]
    context['cargo']=[cargo]
    
    
    

    return render(request, 'paquetes/recorrido_paquetes/Vizualizar.html', context)

def Ubicar_paquete(request, latitud, longitud):

    try:
        latitud = float(latitud)
        longitud = float(longitud)
        url = f"https://www.google.com/maps/?q={latitud},{longitud}"
        return HttpResponseRedirect(url)
    except ValueError:
        return HttpResponseRedirect('/')  # Redirigir a una página de error o a la página principal

def agregar_paquetes_recolectados_casillas(request , eleccion, cargo, folioc, anio):
    estado_id = request.session['ID_ESTADO']
    fecha_hora_actual_python = timezone.now()
    fecha_hora_actual_utc = timezone.now()
    # Convierte la fecha y hora actual a la zona horaria local
    fecha_hora_actual_local = timezone.localtime(fecha_hora_actual_utc)
    casilla = get_object_or_404(Casillas, folioc=folioc)
    # Obtiene solo la hora actual en formato HH:MM:SS
    hora_actual = fecha_hora_actual_local.strftime("%H:%M:%S")

    # Puedes imprimir la hora actual en la consola si lo deseas
    print("Hora actual:", hora_actual)
    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido
    estado = get_object_or_404(Estados, idestado=estado_id)
    cargo = get_object_or_404(Tipocargo, descrip_tcargo=cargo)
    eleccion = get_object_or_404(Procesos, descrip=eleccion, idestado=estado_id)

    formulario = paquetesfasee4(request.POST or None, request.FILES or None, initial={'idcargo_recibe': 'CAE'})
    try:
            if request.method == 'POST':
                formulario = paquetesfasee4(request.POST)
                if formulario.is_valid():
                    Paquete = formulario.save(commit=False)

                    Paquete.folioc = casilla
                    Paquete.idtipo_cargo= cargo
                    Paquete.idproceso=eleccion
                    Paquete.idestado=estado
                    Paquete.fecha_hora_entrega = fecha_hora_actual_python
                    Paquete.save()

                return redirect('Entrega_Paquetes_Casilla_Recoleccion')
                

    except IntegrityError as e:
        print(f"Error de integridad al guardar el formulario S: {e}")
    except ValidationError as e:
        print(f"Error de validación al guardar el formularioc S: {e}")
    except Exception as e:
        print(f"Error general al guardar el formulario S: {e}")

    return render(request, 'paquetes/paquetes_electorales/crear.html', {'formulario': formulario, 'anio': anio, 'nombreeleccion': eleccion, 'nombrecargo': cargo,  'seccion': folioc, 'nombreedo':estado.nombre_edo})



def agregar_paquetes_vizualizar_recolectados_casillas(request, eleccion, cargo, folioc, anio):
 
    estado_id = request.session['ID_ESTADO']
    fecha_hora_actual_python = timezone.now()
    fecha_hora_actual_utc = timezone.now()
        # Convierte la fecha y hora actual a la zona horaria local
    fecha_hora_actual_local = timezone.localtime(fecha_hora_actual_utc)
    casilla = get_object_or_404(Casillas, folioc=folioc)
    # Obtiene solo la hora actual en formato HH:MM:SS
    hora_actual = fecha_hora_actual_local.strftime("%H:%M:%S")

    # Puedes imprimir la hora actual en la consola si lo deseas
    print("Hora actual:", hora_actual)
    idpartido = request.session['ID_PARTIDO']
    partido = Partidos.objects.get(idpartido=idpartido)
    nombre_partido = partido.desc_partido

    cargo = get_object_or_404(Tipocargo, descrip_tcargo=cargo)
    eleccion = get_object_or_404(Procesos, descrip=eleccion, idestado=estado_id)
    
    Paquete = get_object_or_404(Paquetes, folioc=folioc);
    estado = get_object_or_404(Estados, idestado=estado_id)
    print(estado.nombre_edo)
    formulario = paquetesfasee4(request.POST or None, instance=Paquete)
    

    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('Armado_Paquetes')

    return render(request, 'paquetes/paquetes_electorales/editar.html', {'formulario': formulario, 'anio': anio, 'nombreeleccion': eleccion, 'nombrecargo': cargo,  'seccion': folioc, 'nombreedo':estado.nombre_edo})



 
def generar_pd_Entregado_Paquetes_recoleccion(request, anio, nombreeleccion, nombrecargo, idcand, ide):
   try:  
    # Crear un nuevo documento PDF con tamaño de ticket de supermercado (80mm x 150mm)
    ancho_mm = 80
    alto_mm = 150

    # Convertir milímetros a pulgadas
    ancho_pulgadas = ancho_mm / 25.4
    alto_pulgadas = alto_mm / 25.4

    # Convertir pulgadas a puntos
    ancho_puntos = ancho_pulgadas * 72
    alto_puntos = alto_pulgadas * 72

    pdf = FPDF(format=(ancho_puntos, alto_puntos))


    # Establecer márgenes de página
    pdf.set_auto_page_break(auto=True, margin=2)  # Auto salto de página con un margen de 2mm
    pdf.set_margins(left=10, top=10, right=10)     # Márgenes izquierdo y derecho de 10mm, superior de 10mm

    # Agregar una página en blanco
    pdf.add_page()

    # Obtener datos del estado, partido y candidato
    id_estado = request.session['ID_ESTADO']
    id_partido = request.session['ID_PARTIDO']
    ople = get_object_or_404(Oples, idestado=id_estado)
    estado = get_object_or_404(Estados, idestado=id_estado)
    partido = get_object_or_404(Partidos, idpartido=id_partido)
    print(idcand)
    PaquetesFaseuno = get_object_or_404(PaquetesFase2, folioc=idcand)
    paqeutesfasecuatro = get_object_or_404(Paquetes, folioc=idcand)
    casilla = get_object_or_404(Casillas, folioc=idcand)




    # Establecer el tamaño y tipo de fuente
    pdf.set_font('Arial', '', 14)
    
    # Obtener la fecha y hora actual en la zona horaria local
    # Obtener la fecha actual en español
    fecha_actual = datetime.now().strftime('%d/%m/%Y')
    fecha_entrega_formatted = PaquetesFaseuno.fecha_entrega.strftime('%d/%m/%Y')

    # Agregar el logo en la esquina superior izquierda
    pdf.image(ople.logo.path, x=92, y=8, w=45)
    pdf.ln(50)
    
    # Agregar título y detalles
    pdf.cell(0, 10, ople.nombre_completo, 0, 1, 'C')
    pdf.cell(0, 7, "Entrega de Paquetes en Centros de Acopio", 0, 1, 'C')  # Aumentar espacio entre líneas
    pdf.cell(0, 7, "Número de Paquete: "+ str(paqeutesfasecuatro.idpaquete), 0, 1, 'C')


    pdf.cell(0, 7, estado.nombre_edo, 0, 1, 'C')
    pdf.cell(0, 7, nombreeleccion, 0, 1, 'C')
    pdf.cell(0, 7, nombrecargo, 0, 1,'C' )
    pdf.cell(0, 7, "Distrito: "+str(casilla.iddistrito),0, 1,'C')
    pdf.cell(0, 7, "Municipio: "+str(casilla.idmunicipio),0, 1,'C')
    pdf.ln(5)
    
    pdf.ln(10)
    pdf.cell(0, 7, "Fecha de Impresión: " + fecha_actual, 0, 1, )
    pdf.ln(5)
    pdf.cell(0, 7, "Sección: " + idcand, 0, 1, )

    pdf.cell(0, 7, "Fecha y Hora de entrega: " + str(paqeutesfasecuatro.fecha_hora_entrega), 0, 1, )
    pdf.cell(0, 7, "Entregó el Paquete: " + str(paqeutesfasecuatro.nombre_entrega), 0, 1, )
    pdf.cell(0, 7, "Cargo: " + str(paqeutesfasecuatro.id_cargo_entrega), 0, 1, )
    pdf.cell(0, 7, "Recibió el Paquete: " + str(paqeutesfasecuatro.nombre_recepcion), 0, 1, )
    pdf.cell(0, 7, "Cargo: " + str(paqeutesfasecuatro.id_cargo_recepcion), 0, 1, )
    pdf.ln(10)
    pdf.cell(0, 7, "Condiciones en las que se Entregó el Paquete Electoral: ")
    pdf.ln(10)
    pdf.cell(1, 7, "Lugar de Entrega: " + paqeutesfasecuatro.lugar_entrega)
    if paqeutesfasecuatro.con_firma == 'S':
     texto = "Si"
    elif paqeutesfasecuatro.con_firma == 'N':
     texto = "No"
    else:
     texto = ""
    pdf.ln(7)
    pdf.cell(1, 7, "¿Con firma? " + texto)
    if paqeutesfasecuatro.sin_muestras_alteracion == 'S':
     texto2 = "Si"
    elif paqeutesfasecuatro.sin_muestras_alteracion == 'N':
     texto2 = "No"
    else:
     texto2 = ""
    pdf.ln(7)
    pdf.cell(1, 7, "¿Con Muestras de Alteración? " + texto2)
    if paqeutesfasecuatro.cinta_etiqueta_seguridad == 'S':
     texto3 = "Si"
    elif paqeutesfasecuatro.cinta_etiqueta_seguridad == 'N':
     texto3 = "No"
    else:
     texto3 = ""
    pdf.ln(7)
    pdf.cell(1, 7, "¿Con Cinta de Seguridad? " + texto3)
    if paqeutesfasecuatro.sobre_prep == 'S':
        texto4 = "Si"
    elif paqeutesfasecuatro.sobre_prep == 'N':
     texto4 = "No"
    else:
     texto4 = ""
    pdf.ln(7)
    pdf.cell(1, 7, "¿Sobre para el PREP? " + texto4)
    if paqeutesfasecuatro.bolsa_por_fuera == 'S':
        texto5 = "Si"
    elif paqeutesfasecuatro.bolsa_por_fuera == 'N':
     texto5 = "No"
    else:
     texto = ""
    pdf.ln(7)
    pdf.cell(1, 7, "¿Una bolsa que va por fuera del paquete? " + texto5)
    # Calcular la cantidad de espacio en blanco necesaria entre la tabla y el código QR
    space_needed = 5  # Puedes ajustar este valor según sea necesario

    # Agregar espacio en blanco debajo de la tabla para separarla del código QR
    pdf.ln(space_needed)

    # Obtener la posición Y después de agregar el espacio en blanco
    pdf_y_qr_start = pdf.get_y()

    # Generar el código QR con datos estáticos para probar
    qr_data_dynamic = (ople.nombre_completo
                   + "\n"
                   +"Ticket Entrega de Paquetes en Centros de Acopio"
                   + "\n"
                   + estado.nombre_edo
                   + "\n"
                   + nombreeleccion
                   + "\n"
                   + nombrecargo
                   + "\n"
                   + "\n"
                   + "\n"
                   + "Sección: " + idcand
                   + "\n"
                   + "Fecha Actual: " + fecha_actual
                   + "\n"
                   + "\n"
                   + "Fecha y Hora de entrega: " + str(paqeutesfasecuatro.fecha_hora_entrega)
                   + "\n"
                   + "\n"
                   + "Entregó el Paquete: " + str(paqeutesfasecuatro.nombre_entrega)
                   + "\n"
                   + "Cargo: " + str(paqeutesfasecuatro.id_cargo_entrega)
                   + "\n"
                   + "Recibió el Paquete: " + str(paqeutesfasecuatro.nombre_recepcion)
                   + "\n"
                   + "Cargo: " + str(paqeutesfasecuatro.id_cargo_recepcion)
                   + "\n"
                   +"Condiciones en las que se Entrego el Paquete Electoral: "
                     + "\n"
                        + "Lugar de Entrega: " + paqeutesfasecuatro.lugar_entrega
                        + "\n"
                        + "¿Con firma? " + texto
                        + "\n"
                        + "¿Con Muestras de Alteración? " + texto2
                        + "\n"
                        + "¿Con Cinta de Seguridad? " + texto3
                        + "\n"
                        + "¿Sobre para el PREP? " + texto4
                        + "\n"
                        + "¿Una bolsa que va por fuera del paquete? " + texto5


                   )


    # Crear el código QR con los datos dinámicos
    qr_dynamic = qrcode.make(qr_data_dynamic)
    qr_stream_dynamic = BytesIO()
    qr_dynamic.save(qr_stream_dynamic, 'PNG')
    
    # Establecer la posición para agregar el código QR en el PDF
    pdf_x = 80
    pdf_y = pdf_y_qr_start + 9

    # Crear un archivo temporal para almacenar el código QR
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmpfile:
        # Guardar el contenido de qr_stream_static en el archivo temporal
        tmpfile.write(qr_stream_dynamic.getvalue())
        # Obtener la ruta del archivo temporal
        tmp_filename = tmpfile.name

    # Agregar el código QR al PDF desde el archivo temporal
    pdf.image(tmp_filename, x=pdf_x, y=pdf_y, w=50)

    # Eliminar el archivo temporal después de usarlo
    os.unlink(tmp_filename)

    # Guardar el PDF en un objeto de bytes
    pdf_data = pdf.output(dest='S').encode('latin1')
    # Devolver el PDF como respuesta
    response = HttpResponse(pdf_data, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Reporte_Entrega_CA_Paquete.pdf"'
    return response
   except Exception as e:
        # Manejo de excepcione
        mensaje = f"Aun no se Entrega el Paquete: {e}"
        messages.error(request, mensaje)
        return redirect('Entrega_Paquetes_Casilla_Recoleccion')





def get_paquetes_recolectados_casilla_all(request, eleccion, cargo,  id, key):
    # Obtener el estado actual desde settings
    id_estado = request.session['ID_ESTADO']
    proceso = get_object_or_404(Procesos, descrip=eleccion, idestado=id_estado)

    with connection.cursor() as cursor:
        cursor.execute("CALL paquetes_resumen(%s, %s, %s, %s)", [proceso.idproceso, cargo, id, key])
        paquetes = cursor.fetchall()

    if len(paquetes) > 0:
        data = {'message': "Success", 'paquetes': paquetes}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)


def get_paquetes_recorrido_casilla(request, eleccion, cargo, id, key):

    proceso = get_object_or_404(Procesos, descrip=eleccion,idestado=request.session['ID_ESTADO'])
    
    #print(proceso.idproceso.idproceso)
    print(proceso.idproceso)
    with connection.cursor() as cursor:
        cursor.execute("CALL GetTransladadoPaquetes(%s, %s, %s, %s)", [proceso.idproceso, cargo, id, key])
        paquetes = cursor.fetchall()
        
        # Obtenemos los nombres de las columnas
        column_names = [desc[0] for desc in cursor.description]

    if len(paquetes) > 0:
        # Convertimos los resultados en una lista de diccionarios
        paquetes_dict = [
            {column_names[i]: (base64.b64encode(field).decode('utf-8') if isinstance(field, bytes) else field)
             for i, field in enumerate(row)}
            for row in paquetes
        ]
        data = {'message': "Success", 'paquetes': paquetes_dict}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)

def candidatos_contienda (request):
     # Lógica para años
  hoy = datetime.today().date()
  idpartido = request.session['ID_PARTIDO']
  id_estado = request.session['ID_ESTADO']
  #partido = Partidos.objects.get(idpartido=idpartido)
  #idcoalicion = PartidosCoaliciones.objects.get(idpartido=idpartido, idestado=id_estado)
 #coalicion = Procesopartidos.objects.get(idprocesopartido=idcoalicion.idprocesopartido)
  
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
  año_actual = hoy.year
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
  años = []
  for i in range(año_actual, año_actual+11, +1):
    años.append(i)

  return render(request, 'computos_eletorales/agregar_candidato/Index.html', {
    
      'años': años,
        **context
       #'nombre_partido': coalicion.coliacion

  })



def computo_votos (request):
     # Lógica para años
  hoy = datetime.today().date()
  año_actual = hoy.year
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
  años = []
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto  
  for i in range(año_actual, año_actual+11, +1):
    años.append(i)

  return render(request, 'computos_eletorales/computo_votos/Index.html', {
    
      'años': años,
      'captura': 'Uno',
        **context
  })



def Rerepre_Ople_index (request):
  

     # Lógica para años
  hoy = datetime.today().date()
  año_actual = hoy.year
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
  idpartido = request.session['ID_PARTIDO']
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto  
  partido = Partidos.objects.get(idpartido=idpartido)
  nombre_partido = partido.desc_partido

  años = []
  for i in range(año_actual, año_actual+11, +1):
    años.append(i)

  return render(request, 'computos/representantes_ople/Index.html', {
    
      'años': años,
      'nombre_partido': nombre_partido,
      **context
  })

def Integrar_Candidatos(request, anio, nombreeleccion, cargo):
    id_estado = request.session['ID_ESTADO']
    idpartido = request.session['ID_PARTIDO']
    # Obtener todos los objetos Paridad
    partido=Partidos.objects.all()
    proceso = get_object_or_404(Procesos, descrip=nombreeleccion, idestado=id_estado)
    cargo = get_object_or_404(Tipocargo, descrip_tcargo=cargo)
    estado = get_object_or_404(Estados, idestado=id_estado)
    cargoss = get_object_or_404(Tipocargo, descrip_tcargo=cargo)
    idprocesopart = PartidosCoaliciones.objects.filter(idpartido=idpartido, idestado=id_estado, anio=anio).first()

    Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
    Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

    context = {}
    if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
    if Pantallas.revision_ople is not None:
        context['revision_ople'] = Pantallas.revision_ople
    if Pantallas.registro_de_gubernatura is not None:
        context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
    if Pantallas.registro_de_ayuntamiento is not None:
        context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
    if Pantallas.diputaciones_de_mayoria is not None:
        context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
    if Pantallas.diputaciones_de_rp is not None:
        context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
    if Pantallas.armado_de_documentacion is not None:
        context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
    if Pantallas.entrega_a_los_caes is not None:
        context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
    if Pantallas.caes_entrega_a_los_presidentes is not None:
        context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
    if Pantallas.entrega_de_paquetes_en_ca is not None:
        context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
    if Pantallas.resumen_de_paquetes is not None:
        context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
    if Pantallas.traslado_de_paquetes is not None:
        context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
    if Pantallas.registro_de_representantes is not None:
        context['registro_de_representantes'] = Pantallas.registro_de_representantes
    if Pantallas.representantes_ople is not None:
        context['representantes_ople'] = Pantallas.representantes_ople
    if Pantallas.registro_de_observadores is not None:
        context['registro_de_observadores'] = Pantallas.registro_de_observadores
    if Pantallas.agregar_candidatos is not None:
        context['agregar_candidatos'] = Pantallas.agregar_candidatos
    if Pantallas.computo_de_votos is not None:
        context['computo_de_votos'] = Pantallas.computo_de_votos
    if Pantallas.porcentajes_de_avances is not None:
        context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
    if Pantallas.resumen_de_actas is not None:
        context['resumen_de_actas'] = Pantallas.resumen_de_actas
    if Pantallas.votos_por_partido is not None:
        context['votos_por_partido'] = Pantallas.votos_por_partido
    if Pantallas.principios is not None:
        context['principios'] = Pantallas.principios
    if Pantallas.acciones_afirmativas is not None:
        context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
    if Pantallas.documentos is not None:
        context['documentos'] = Pantallas.documentos
    if Pantallas.entidades_federativas is not None:
        context['entidades_federativas'] = Pantallas.entidades_federativas
    if Pantallas.distritos is not None:
        context['distritos'] = Pantallas.distritos
    if Pantallas.municipios is not None:
        context['municipios'] = Pantallas.municipios
    if Pantallas.cargos_entrega is not None:
        context['cargos_entrega'] = Pantallas.cargos_entrega
    if Pantallas.partidos is not None:
        context['partidos'] = Pantallas.partidos
    if Pantallas.casillas is not None:
        context['casillas'] = Pantallas.casillas
    if Pantallas.centros_de_acopio is not None:
        context['centros_de_acopio'] = Pantallas.centros_de_acopio
    if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
    if Pantallas.tipo_eleccion is not None:
        context['tipo_eleccion'] = Pantallas.tipo_eleccion
    if Pantallas.partidos_coaliciones is not None:
        context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
    if Pantallas.eleccion_documentos is not None:
        context['eleccion_documentos'] = Pantallas.eleccion_documentos
    if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
    if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
    if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
    if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
    if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
    logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
    context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

    with connection.cursor() as cursor:
        cursor.execute("CALL candidatos_por_Integrar(%s, %s, %s)", [proceso.idproceso, cargo.idtipo_cargo, idprocesopart.idprocesopartido.idprocesopartido])
        paquetes = cursor.fetchall()

    if len(paquetes) > 0:
        data = {'message': "Success", 'paquetes': paquetes}
    else:
        data = {'message': "Not found"}


    return render(request, 'computos_eletorales/agregar_candidato/Integrar Cand.html', {'nombreedo':estado.nombre_edo ,'anio':anio,'cargo':cargo, 'nombreeleccion': nombreeleccion, 'candidatos_mostrar': data, **context})


def carga_foto_candidato(request):
    if request.method == 'POST':
        try:
            archivo = request.FILES['archivo']
            id_candidato = request.POST.get('idCandidato')
            

            # Busca el documento existente con los where proporcionados
            Candidato = get_object_or_404(ProcesopartidoCandidato, id_cand=id_candidato)

            # Actualiza la información del documento en la base de datos
            Candidato.foto = archivo
            Candidato.save()

            return JsonResponse({'message': 'Foto recibida y actualizado exitosamente'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return redirect('Integrar_Candidatos')

def Integrar_candidato_Eleccion(request, idcand):
    if request.method == 'POST':
        # Obtener el objeto Candidato
        candidato = get_object_or_404(Candidatos, id_cand=idcand)

        # Obtener los valores necesarios del objeto Candidato
        idProcesoPartido = candidato.idprocesopartido
        idProceso = candidato.idproceso
        idtipo_cargo = candidato.idtipo_cargo
        anio = candidato.anio
        Nombres = candidato.nombres
        ApPaterno = candidato.apaterno
        ApMaterno = candidato.apaterno
        Sobrenombre = candidato.apodo
        # Añade más campos si es necesario

        # Crear una nueva instancia de ProcesopartidoCandidato con los valores obtenidos
        nuevo_candidato = ProcesopartidoCandidato(
            id_cand=candidato,
            idprocesopartido=idProcesoPartido,
            idproceso=idProceso,
            idtipo_cargo=idtipo_cargo,
            anio=anio,
            nombres=Nombres,
            appaterno=ApPaterno,
            apmaterno=ApMaterno,
            sobrenombre=Sobrenombre,
            # Excluimos los campos estatus y foto
        )

        # Guardar la nueva instancia en la base de datos
        nuevo_candidato.save()

        return JsonResponse({'message': 'Candidato integrado exitosamente'})
    else:
        # Si la solicitud no es de tipo POST, devolver un mensaje de error
        return JsonResponse({'error': 'La solicitud debe ser de tipo POST'}, status=400)
    
def Paquete_numero_cero(request, anio, nombreeleccion, cargo, folioc):
    idpartido = request.session['ID_PARTIDO']
    estado_id = request.session['ID_ESTADO']
    proceso = get_object_or_404(Procesos, descrip=nombreeleccion, idestado=estado_id)

    # Intenta obtener el objeto Actasmodif
    idacta = Actasmodif.objects.filter(folioc=folioc).first()

    # Verifica si se encontró el objeto
    if idacta is not None or folioc =='0':
        print("Se ya está registrada la casilla")
        if folioc =='0':
         print('Mostrar todas las casillas');
         with connection.cursor() as cursor:
            cursor.callproc('ObtenerResultados_catas_ALL_CASILLAS', [cargo, proceso.idproceso])
            candidatos = cursor.fetchall()
        else:
         print('Consulta normal a casillas');
         with connection.cursor() as cursor:
            cursor.callproc('ObtenerResultados_catas', [cargo, proceso.idproceso, folioc])
            candidatos = cursor.fetchall()
        if len(candidatos) > 0:
            data = {'message': "Success", 'candidatos': candidatos}
        else:
            data = {'message': "Not found"}

        return JsonResponse(data)
    else:
        print("No se encontraron registros que coincidan con el filtro")
        
        try:
            paquete_Entregado = get_object_or_404(Paquetes, folioc=folioc)

            with connection.cursor() as cursor:
                cursor.callproc('consulta_beta', [proceso.idproceso, cargo, folioc])
                print("Aun no grabamos la casilla y si se entregó el paquete")
                candidatos = cursor.fetchall()

            if len(candidatos) > 0:
                data = {'message': "Success", 'candidatos': candidatos}
            else:
                data = {'message': "Not found"}

            return JsonResponse(data)
        except ObjectDoesNotExist:
            print("Aun no grabamos la casilla pero no se entregó el paquete")
            data = {'message': "Not found"}
            return JsonResponse(data)


def Resumen_actas_consultar(request, idproceso, idtipocargo):
     # Lógica para años
  hoy = datetime.today().date()
  año_actual = hoy.year
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto        
  años = []
  try:
    with connection.cursor() as cursor:
        cursor.callproc('obtener_resumen_actas', [idproceso, idtipocargo])
        print("RESUMIENDO ACTAS")
        candidatos = cursor.fetchall()

    if len(candidatos) > 0:
        # Crear una lista para almacenar los candidatos con la suma
        candidatos_modificados = []
        for candidato in candidatos:
            # Usar 0 si el valor es None para asegurar que la suma funcione
            votos_12 = candidato[12] or 0
            votos_13 = candidato[13] or 0
            votos_14 = candidato[14] or 0
            votos_15 = candidato[15] or 0
            votos_16 = candidato[16] or 0
            total_votos = votos_12 + votos_13 + votos_14 + votos_15 + votos_16

            # Crear una nueva lista con los valores originales más la suma
            candidato_modificado = list(candidato)  # Convertir a lista si es necesario
            candidato_modificado.append(total_votos)  # Añadir la suma al final de la lista
            candidatos_modificados.append(candidato_modificado)  # Guardar en la nueva lista

        resume = {
            'message': "Success",
            'candidatos': candidatos_modificados  # Pasar los candidatos modificados
        }
    else:
        resume = {
            'message': "Not found"
        }

  except ObjectDoesNotExist:
    print("Error al resumir las actas")
    resume = {
        'message': "Not found"
    }

  print(resume)

# Crear una lista de años
  partidos_mostrados = [] 
  años = []
  for i in range(año_actual, año_actual+11, +1):
    años.append(i)

# Renderizar la plantilla con el contexto modificado
  return render(request, 'computos_eletorales/Resumen_actas/Index.html', {
    'años': años,
    'captura': 'Uno',
    'resumen': resume,
    'partidos_mostrados': partidos_mostrados,
    **context
})


def guardar_datos(request):

    if request.method == 'POST':

        # Decodificar los datos JSON enviados desde el cliente
        data = json.loads(request.body)
        estado_id = request.session['ID_ESTADO']

        # Obtener los datos del JSON decodificado
        tablaData = data.get('data')
        anio = data.get('anio')
        cboeleccion = data.get('cboeleccion')
        cbocargo = data.get('cbocargo')
        folioc = data.get('folioc')

        proceso = get_object_or_404(Procesos, descrip=cboeleccion, idestado=estado_id)
        cargos = get_object_or_404(Tipocargo, descrip_tcargo=cbocargo)
        casilla = get_object_or_404(Casillas, folioc=folioc)

        # Imprimir los valores en la consola de Django
        print("anio:", anio)
        print("cboeleccion:", cboeleccion)
        print("cbocargo:", cbocargo)
        print("seccion:", folioc)
        print("data:", tablaData)

        # Variables para mantener la suma de votos para cada coalición
        suma_votos = 0
        coalicion_anterior = None

        for fila in tablaData[1:]:  # Ignorar la primera fila ['Coalición/Individual', 'Siglas', 'Votos']
            coalicion_nombre = fila[0]
            partido_nombre = fila[1]
            votos_str = fila[2]  # Convertir a cadena de texto

            # Convertir votos_str a un entero
            try:
                votos = int(votos_str)
            except ValueError:
                # Manejar el caso donde no se pueda convertir la cadena a un entero
                print("Error: No se puede convertir votos a un entero")
                continue

            # Obtener el objeto de la coalición
            coalicion = get_object_or_404(Procesopartidos, coliacion=coalicion_nombre)

            # Obtener el objeto del partido
            partido = get_object_or_404(Partidos, partido=partido_nombre)

            # Obtener la casilla dentro del bucle para asegurarse de obtener una nueva casilla para cada fila de datos
            casilla = get_object_or_404(Casillas, folioc=folioc)

            # Verificar si es una nueva coalición
            if coalicion != coalicion_anterior:
                # Si es una nueva coalición, guardar los votos sumados para la coalición anterior
                if coalicion_anterior is not None:
                    nueva_acta = Actasmodif(
                        idproceso=proceso,
                        idtipo_cargo=cargos,
                        idprocesopartido=coalicion_anterior,
                        num_captura='1',
                        votos=suma_votos,
                        folioc=casilla
                    )
                    nueva_acta.save()
                # Reiniciar la suma de votos para la nueva coalición
                suma_votos = 0
                coalicion_anterior = coalicion

            # Sumar los votos para la coalición actual
            suma_votos += votos  # Corregido

            # Crear un nuevo registro de VotosPartido
            nuevo_registro = VotosPartido(
                idprocesopartido=coalicion,
                idproceso=proceso,
                idtipo_cargo=cargos,
                idpartido=partido,
                voto_partido=votos,
                folioc=casilla
            )
            print("Coalición:", coalicion_nombre)
            print("Partido:", partido_nombre)
            print("Votos:", votos)
            print("----------------------------------")
            # Guardar el nuevo registro en la base de datos
            nuevo_registro.save()

        # Guardar los votos sumados para la última coalición
        if coalicion_anterior is not None:
            nueva_acta = Actasmodif(
                idproceso=proceso,
                idtipo_cargo=cargos,
                idprocesopartido=coalicion_anterior,
                num_captura='1',
                votos=suma_votos,
                folioc=casilla
            )
            nueva_acta.save()

        # Procesar los datos y enviar una respuesta JSON
        response_data = {
            'data': tablaData,
            'anio': anio,
            'cboeleccion': cboeleccion,
            'cbocargo': cbocargo,
        }
        return JsonResponse(response_data)

    else:
        return JsonResponse({'error': 'Método no permitido' })


def porcentajes_Avances (request):
     # Lógica para años
  hoy = datetime.today().date()
  año_actual = hoy.year
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  

  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto
  años = []
  for i in range(año_actual, año_actual+11, +1):
    años.append(i)

  return render(request, 'computos_eletorales/porcentajes_de_avances/Index.html', {
    
      'años': años,
      **context
  })



def prueba_guardar_imagen(request):
    try:


    # Imagen base64 a decodificar
     imagen_base64 = '/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBUUFBgVFBQZGRgZGyMcGxsbGxodGxsbGhsbGhsbGxobIS0kGx0qHxsbJTclLC4xNDQ0GiM6PzozPi0zNDEBCwsLEA8QHxISHTMqIyozMzMzMzMzMzMzMTMzMzMzMzMzMzEzMzMzMzEzMzMzMzMzMzMxMzMzMzMzMzMzMzMzM//AABEIALEBHAMBIgACEQEDEQH/xAAcAAABBQEBAQAAAAAAAAAAAAAEAgMFBgcAAQj/xABIEAACAQIEAgcFBAkCBAQHAAABAhEAAwQSITFBUQUGImFxgZETMqGxwQdC0fAjUmJygpKiwuEzshRTY/EVJUNzJDSTs7TD4v/EABkBAAMBAQEAAAAAAAAAAAAAAAECAwAEBf/EACoRAAICAgIBAwMDBQAAAAAAAAABAhEDMRIhQSJRYQQTcTKR8RShsdHw/9oADAMBAAIRAxEAPwAPqlraHifmRPwqyNVY6oXeyycQ0jwIk/GrWBRoAmNKSaXXuWgYcyzauiJ7O3kajJYPbce6wCseZJ0BHnvU1hho45r+NCu+VCwExwqeR0kiuNXZl/R972WKxRyBstwmCJgC6wz6cVDZh4Vu3RlxLeHzOwVULyzEABRcfUk6ARWG4i+LXSGJkSGmRzVymb+lm+FWz7T8YVwFu0haHvkt3hEDQeYzXFPiBVYvpMjNW6L/ANG9ZMJiHa3ZxFt3X7oYSe9AffHeJpHTNub1gqe2CwUHgpRix02mAJ4aefzrawFyAwMMNQNiCNoI2NbJ1JN++MJiMSzPcX21rMY1tgAqTA1adJ4jfXWm5X0K8bXZeLcbbRwO48e7vFPxXroDTZOXcac+XiPz5U1iUKy15HdTgrglGwcRuupcV7FbkbiQXSFhrtz2Z0trBb9okCBRdtAYgdkbd8fSncQupG07+EfkUhroUfCBz5VKTtlYro8xNzKAF1Y6AfMnuqJxFwj9Hb7Tt7zd/wCFEvMkDV237hy8KfwGDFsc2O5oGG8B0eLYk6sdzRpWveFBviC5y2/NuVAYIe7rlXVvlWO9I2//ADHFA7lcV/8Aj3a13D21tTrJPrWTdJIT0w9s6Z3uL53rLqPU3BWMK6s4j/y7pK2N2S3H8QuL8wKzKrz0ViMuExw4exTTvFy2Br/E3rVGoox1dXV1ME6t86QsAtoYIaJidFgAQTA1HCsKwiZriL+syj1IFbrj8SoLydSxI48d4pJGAwiKSW24DvpF64plVBEeGs7Gh3uDIAPDURM/SmFuwRp+YpTBDOwcdknlqPjrT9nEMzNIM6j0GkUOuO3WJB103BpeFnWZE67a1mNQXgWGfLpJjefzNIx7D2jeJ4d5o3o9QHGu8f7oPyFRuLgux76DFoguqf8AqNry+IP4VeIrP+qj/po5r8pj51oCHSrMQTFKC17SorJGsdwm571+ooZACCDqCDI586Jw/wBPpP0qm9Y+mns2LrJ2WVsqnjLk6+UT5Us8bkuvBTHNLZXumLyJ0hjASAGtZRJHvZbTAeMrSut/SqXnTICQq6kgjMSF93n7pg8c1UkXDvOp3njO80Z0YvtLiWy2UOwUmJy5iFDR4kVuPVDRattnq9I7EoCRxDETW89U8Tbt4XCozZTbTM+fQhriM51O+pI05QKyvoPoizaxiW8VbZ2FwLlUjLm7ORmQrLISZ0OsbaEHUekuh2uBgpJZ3WQdSAnaywNRoDpHGpynxdUGUHVstI6RtFWfOMqmCYOhIB5d4ogODAnUiQOMc45VVL2HYHVnUzOu/hqNq4L3muf+t94h/pvktJSPd07uB/Dx+dKVuB0PL8Dxqi9Nvfyp7K4ymTP6TJIgcyAaJNjEJlH/ABruGIEFVO5C6kk8xw2murHk5x5I5si4ycS5xXZKrfRF+4jPazMQgESUO8EwAAR73Ge6vOj+ttm7c9kl2X4LkbUDQmSojWRryqoIu0Qv2ldY7uFKWrJCtcVmZ4llVSFGWdJJLa91Zw2Ou5faC/czbznafnVs+1qGGHvg6S9skeTDykNrVEsX1IyTqfkalKVHTjgmjVPsw6UfEWbpukF0cKG1zFWWdfOaubmPSqB9lT27du8huKGNwQhIBIC7gHeSSP4RV2vPM+G3pWuxJQafY1ezOwAMKN/wpSKFAVB517btk6nQUt7gEBdTRAciBdWMmsl+0Mmz0kLyDUi3dHebfZ//AFitatWidX9Kon2tdHyli8B7pa238Qzr/tf1rAKp0ng/ZWukwIhRbyRxt3Lyuh80Kms+rTOkcr9EXLwIzhLWGuL/AOzcm208ew6j+CszooJ1dXV1MYker65sXhxzvWx6uta1j0LXCfTTnr51lvVO3mx2FH/WQ/ysG+la0l/K0BGMGJ7MeOrT8KSWzATYbLEncR6U0cOx1kUY7KzzMQDpHLy/MU2YIETy/wC/540gQRSbfn5x9KMkkCd4/wA0wqQ2rEjlA0+tEe0C6AGBQY3Qd0ajZp4fHTX6VE4i1LE1MdGGc502Mfyt+NQl+6MxHLT0oilW6t3/ANOhPIg/A/StPt1lfQwy3EY6dqP5lIHxIrUbZq7JDsUqvBShWRhdgbefxBrK+vpIQCdHukx+6pj/AH1qK58yZQuXN2iSZGvAAa+ojvrP+tnRbYhWVBLo8qvMHssNduB8qzbSpeRoqzNlEmKsHQx9iwuCMwMSeDRKwPH5UrF9S8YiZ/YlliTlIJH8O/pNM9A9C3btxCi5gXymPutyedhQcJaGUkbB0l0Kl3EWr8lSoIbLuSpV1M8DlV1n9scqmb11fZrldnUEQWZm0AY+88k/Gh+jWIMEzoYHgJ+lB9VsTbaAqqvaLXCCfeZCAJOmgBGm0VvqcavldaX7gwybVPtIcxfSotXVtB7klQcyucsFnXYmPuHSKkHLH3jPkgPqADUL07jLYxOIVj/6FpVIBYks1/Tsgk6D8zUvasYdmVReBLGBo+p8wBXBmwyVJOzojkj7UR3SwVzkF02mUZ805QRtlzSPTu8KZue2S0LhW0VI0yvcJ1IAJJMQd9+Irzrl1XZns3rALAQriRwMhp8CRHy1l3rL1hsYXC2beVrjW4zKgXQBWXtAk5RqDrPDhV8UHGKQmSEZO0+3/YhbnWS5hA942wwZhbKy+VWjMNz2Zj4baVS8d1sYXDcw9u3YbgyIC4nVodtgT3UB010/dxZBuMAo922krbT91JMHv3qEZ5NdAsMaiiQwPShS7nuEsG0YkkkSZmtCw1+z7BbkJEGWIHkZjXhWVstO2b5UER4d1Kw1bLH1dxAbEsC0LlIWdMxXbfjqxrQeiunGtXFzklDowOsAxqOUTt41kOEuZXR5jKwPoauz4qb4UEBMrOTzXM8/BV9ajNU7R7H0rhLE4SV9/wCTYSC40935inEtARFQXVHpH2iG03vJ7vevL+E6eBFWANTKVo8rNieObi/BwqJ61dHDFYW5ZHvEZk/fQ5l9SI8CalHNLFsRNGyNGAiV6OxgO5uYcf1X2OnPSqZWv/aP0dbsYfEvbIAvX7bFYEB8lwv5kuT3TWQU6MdXV1dRMT/UdZx1nuLN/LbdvpWlX7pUq3qPETy23rPvs7t5sfbnYLcJ/wDouPmRWk4lNF2O546axx86ST7Mhi5odCSpiDt/2I+hplnIB1BIPw/MU4SNAOZJHCYn6/Ch0fUnfupWMhOckgcTy7qUwaSdKbQyw12Bk95P4U8241rBJrowQjkgbHfiIA+tV64up8Tw76snQ4ZrLl1ynURmnTQAyRpttVdy+PwoIVFOwLjjwdT/AFCa1LDPIUzOnr31lCOpB00jWtS6M0RRyAjXhwrpZMkK9FJBr3MBQAOo3zqr4O6Bjbyk6jae9mnz0HrVmnQ/nhWa9Zsc1jHsy7kxrtrBE8xJFMmk02FK7RqOFbsjWaYTCWEutcS2odx+kiRmAM5iuxaTvvrWbYfrrjQPdtsOWT8GBq09FdL3b9sXTbZCZEKDBA4glZg/Terxyxk+hZYJRV9fuWrpK6lpPbknKhGaADoSFnnxqsdT7uGtq6XHti2CrRcK9sC32jDe9DcKNF/2tt7VxffEZXzBTGo1BB0IB0POs+wzkGXt5UWRGvvcjLdqI48q5/qldJrr/RXAqT7NT6I6XtZRcXBi3mkBraIVKGCpzLlJkHUAEAqdTvQfT/WG2CttLdwXM6XMxRspiSVzKSSw2IGnlrVBwHTt9UX2dxlSOypg5VOoGo76krPWbE8XVvFF+grm5pMr9tssvTPWe4bWXCo4QjVxLREjKpUaeJ1HIHajWvaXGYW7buwBLBVZiBqSW0233qwWutN3iiHyI+tSVvrQciubepZlOViPcCNO3/U+FByT8jRTj4MpwHRbYzEizhlgOREzlWdJYiSF7qI64dVrvR11bburq65kddJjRgVOqkH1BHgNOwnTGHQkpZyEsGJRUEsDIJiJM86R0+uDx5Q4gsSgIUgspAaCfdEHUcaZZFexXGXsYuh4UqK0a51EwLapiXXuLIY8ioNB3vs+H3MXI77TfNWpuaAVPD9IvbACqmnEoJ48fOpDC9KIWV7mhRToBo7FhAgcImRymKKxPUq8m16wR3uyn0ZfrQy9VcQGGa2GTibbK5010UGdTA2rSplYZHDRdOrF7EMvt7KByhntGAw3YSvGJ5xmI13rVEIYBhswkeB1FY30I90nJbDW3nKFdGQFYjiACBqdY7pNaqmLRLYRCSyIAuYEA5RAllBCzFRTab9in1GRZafkkMo41wFDdH4s3ASyBCDEB1edNwV+oowJTRlejmlBp0zJftRQphGDCM+NZh+6bZYH4z51khrZ/tqCjDWRx9qT4yrDXyHwrGSKrHRNia6vYropjFv+zTTFs36tpz6lV/uq9Xb4nLDSIGoMaE6zy1NUr7NrX6W+x2FpQdYHavWjudJ7Jq54p8zaEamBEzpB174M+tSnsKEXcSFU7b+nPXjP0qOFyToRJPynnXuPbURsOfM+NC221oIIWi9sMNiNdeOw+tP23lx3Gh1cqGaPdE6wRPeDodaeDzcJEAZp0A4a7CBRMWrAuf8Ahn9OHMzVckcj8KnwxXCsI7RJkb6xwI33qB9meVACKCbUVovVvE5rCZuCgT8R4aEVndsQPA1cOp+Jz4ZhB7IMd8D4aADyroZMt6GnFNITXWnFrIB6BoazvrbYDY2GEhkPrkUg+qzWig1n3XFf/jUj7ygeodfnFLPTHx/qRWMBixGvn41YujutjWUCAgqNgRPlpFVDCIWZlIAbMZXw0NTuC6DDb0kFJO0yzkmqaJ49crlzsKmYnaAN+4naoXHYe4ie0uLAuAkAntbTqOG9S/QfR9v/AIhE0BEsoP3mUaLy5nyojr6P0dsDjn+Sj6081Jq5OwJpdJEDYtwqjkB8qfVaUFpaLXC2dSieijEH6FP/AHLn+yzQsUdtbtjnnb1YJ/ZQvpha7Q2q08opCCnCYE6ee1JY9CDdUMELDMRIWdSBuYp4VWbnQ11sQbgce9nzTqNfcG/DTaIpzpB8Rnu5PaDM9tUjNAGUlyOETEmq/bT0yPOrtFoS642Zh4E1411jvB/eCn5iqpc6UxCs4fs+ztGdBlZwwVXBI4hgY7qkOhcdcuEZnUjLJj2Z10/UcsN+Kig4SirsZTjJ1RNri2XYDyGX/bFPWumbicP6n+pNDFaZdampy9xnjj7EyvWNspLWw0EDUz7wY7kT93nxoiz1tUbrcX91jH8pJquun6Pxf/av/wDdAYoEDTeRtvuJ+FFyDCClKvBb+sGEwvSmHV7l+4nsGXMckmbhKgZQI1Ma8I1pjDfZjglALC+8iQWbQzrtbAI8696pFreEe885XuMGXUAosACPNtasfRfWW1cA9ncUiICsI0GkcKtHI0qZzZcaUmo6Kxifs2wTaIGQ/s3Gn0eaiMX9lIH+niGB4B0DfFCPlWrpj1bRkkd0Eehr1bdtiMhgcQJHwOnwqiyPwyLRk/QPVS5gvatdZGVwiqVzbh82oYAjYUdi7nZ0Ejfh4cp5Crt1nwg9jm7RVJZoyh4jdZGUkT3bnWqFbuYW5GXEhOa3VKd+jjs0W7ZkN3VDAjKJ012M7a6kTFNYXCwZ4jbxkCrBa6FdbZZctxSZlDmO0EDTXy+FNW8Adj2Z5gg95M0OQQAKVUMujZh3wQYnlpM7UjDE+0LRrJPdvyo44Yrpusk6d2g/PfXWcPDErvyjnpHpWTAySxTZcOkcY+gqu3nJYmDvpB0irHj3HswAZywSO1xZo3Ea5Tx4axQmCtK65lAgnl3CjYpmlkaMBz/z8qtvUxQEdOTNPnBHzqpK+pPP8KsvUq7LuBzn+mPpXQIy8WBoPAU5mpFral0UA6aq/WvoprpFy2JKKdB+zJ+oq0GmHcrIUKQdSp356a0evJuzH7NopdYXEhgTqRr6/nepzDNtv5U919tqqW79sQTcIIIg6rrPmpqJ6OxwZQT5ik0ysXZYbOHlsyAe0UEodIDgdgnX9aOIprrDjXvJh/aLluahwPdLZlGdeQYCY4GR317hcbtz8foOPfSem8QLl22eOUT4gsZ+ApZuosolbQgLSwtcBTiiuA7BJWjbywtscrY/qZ3/ALqEdZHfw8aPxSwwHEIinxFtAfjNbwbyBYi/7OOyTvtwAE+Z7q8fHWzKsJH8JBAAJ3OtFAU8EpbXsFp+5Fm5hxqUCxxy7ea/PanVFkzDMPvaM68YJEGNzTzYi3LA/dBzEqcoCxmGaI0nbx5GlI1qA3YAZcwMAdkQ5O2w0NM3+ROP4GVW3wuty1eeJ3DTx08qIwtlQcwfNpH3OfNQJ2+FIW3ZYqAVJIDKA241YECfE+tOHoy2NlI0I0J2III8NT6mlclq2FRY+RTbivbGGVJy8d/IRwpTCp+eii+Rq6vZUc8zepC/2UMy0dfX3RyUf1Ev/dQtxaLNFuPaL70XhbYwlq3dto6OgchtRmcltDwMMNZFDXeqOFOtovZPIHMs/un8TS16QsY2x7PA4m1nVAArSCFAiCvvA6cRFRuGvY3CKExCF1GmcdoEeM6+proprx0cLdtu+x1uh8bZM22FxR+odY70I19Kk+hOkbly4UuKVIUnUQdCBHxpOD6dtPsxU8jt/ipnD3s/EHTRt9OU8B58K0eLYsroH6f7WGuKdiAD4FlH1rNMV1dtn3GZT6j46/GtL6dX9A3iv+4VVSlUk2CJTP8AwLEWjms3CDztu1tvUEfOjLPWXpCz2bjZ1/Vu2wy/zrDHzarMyacqU1maTmxqRB2OuNoke1weWPvWHj0ttCjzY0aOs2BB9oly5mMAo9uCOM5l7B79Z8aVf6GtXJzWxPMaH1FRGO6oTHsXgk7PrwJ334GmU0ZxLRatNibXtLShlOXYjUZATPa3kkRE6a1IdH4AqsEEGddDvAn41l6dWcbZfOinPwe2+VwO5gVPoaOTGdJgQ3/FT3oWPqykn1pt6E0VO0ZFT3VN8t4Ru3x3H1FQlob1MdX7mW+nIyPkfpXSK9GmWtQKcimsOZHlT6imJjN9JGlDMvoPzFHOJFR2CxIdn/ZMUrCis/aJbnCE/q3FPrK/WqHgCcqsNxp6Vo3X21ODud2U+jrWf9GW/wBGO+T8aVlIkjZuxBoy02a4p5fLKfxpr2eYso/9O2hOn3nkxodezHqafwafpPBT8cvfU8j9JWH6g8LS1WuC0oCuJs7aB8W5VCQJOgA5liFA9SKV0h0vGIdWSBneT3KXKacyizHCV50bgUm4gO2dSfAMCfgKbKA6kCSZPjz8adOPHtCNScumB2ulO1lZBtMq2YAFXbUwO0MkEftCnB0v2Xb2bQiyfIAkCQAYmN+FLbCWgDNtAsyZVYnadt9Y865Vs9oyms5tRrqCZ84oXH2N6vcZti27shV1gywzjLPZc6K07xrG88zLeDS1cCgNcy5SVBZYCKbbMJUkj7mhM6d5k9EtSxBWT70Nz3kTA8a5MDaMQTopA/SP7pG3vajT4Uea+QcX8AmANpSjq7kRCjKT2dAMxUTlGYatsSakk6Rtn7xGsaq41Bg7jQTpO06U3awSDKVLabQ51EggHXUSPyCa5uj1PFgNZAI7UuXg6frE7RvSScW+7GipJdUPri7Z1DruBvxbYefCl5gRIMio7/wdAAAzAAggSNGUKA22vu/1NzovCWCFFvNOsAxG+mvOkko+GMnLygjEDtEcgB/KoX6UDjWyo55KflRt55ZjzYn1NQvWTEezsN+0Qv8Acfgpox7lXyCTqN/BSGuEPnUlWmQQSCDO4I1FXHoH7S8Xh4S9GIt8Q+jx+/EN/ECe+qPcvTtTZavRo843HAdM9F9IQFb2N4/dPZae4TDbbI3lVj6D6KuWHfNczoQMpnv1njO24r5pJq19XevmLwhCi57W2PuXCTpI0VveXQabgTtSPErtB5OqN/x2H9ohUGDIjyPGq7isIymGEH4HwPGhOrn2j4PE5UdvYXDHZcgKT+zc92OHayk8quRVXXUBlInmCDsQfrSyiZOinGya9NsipjHdHm2ZXVPl40LkqbGsCC01iXNtXcASiMwJ1EhTAOsxMTUj7IGozptYsXjOyZY00LMo+tCg2Qr9PXrts2xaFt3EJczkICeJ0lePOoTEdYsVYY27rjMuhjIw/my61fcLaK4RCsA+zBExALDfXxqM6N6v2rwd7qDN7RgOEqIyk98U0aXgDZmq2wUnjIHkQfqKXZu+zdHgkKw0ESQQQRr40i3OUcjuOMgiI8j8q9cazwkT6ifhXaSNK6ExYuARMZFOog8eHmKliageiMRbZlNt1ZcrLKGVlcnLuqdUzQFEXASCJ4/hQ2EweR3bi3Hw50W7ACZoOxcOdgTMmR3aba0LMiL61282FvCJ7DfAZtPSqD0as208AK0rpcTbuE7ezb/aazTox8ygn7xJ072O3hyoMpEmcO4Fy+OVwD+VFWPWadw2ruRyH1/CmPYFLl0sB2nz9k6dpVPKRrNEdGpmzhdSCAe7shh8GqeS3GkWxtKXYWBXsU2+AuEzmca8CPSDQ2Jstbj2l11kaTGseVcn22dP3F/zJPBaOT+qjn+hgPiRSBUcnSFtVuTfALAKBA07eYkab6Aa92m9Js4kXDCXszbwqg6eEHSg4OjKask3QMIO34GRqO+mTgbZMlddeJ4ggga6CCdKaWzdj3nPebZ5Acu4nzr32F7/AJjDxt/4pUmtMZtPaG8RZshsjIZbXj97sk7zw4Uq0bdx9AxMRuIACleB00P9Q50ss8n9Io7su2o318R51yu//MTb9Xjz3puTrYtK9Dn/AIZbmRI2OkcJjcc9fGiMHhVtzlnWBqZgKIAHlQyPc/5ien+ad9pc/WSPP8aVtvqxkku0gxjXuGPbU8jm/l7X0oEPd4lDy334TrS7Fy52icmin9bdhk/uoRj2aUuh8Gp3qtgLN43FvW1fQBVYSdQwbLxBgxpwJqrJcufeCxxgn8Kl+jcTlAHFm07joAZ8aC9LBP1RaPOt32Yo4FzAhVYDW2SYaNsjHQHuMeNZNi8A9p2R1KsphlYEEHvBrfOiusbuy22QMWIAaYI55tO1p56Ub1g6vYfGplvJ2gIW4sC4ng0ajuMjurqx5b2cc8bifNpSvKufWjqLiMJLge0tf8xBqo/6ibr46jvG1VB7ddKdk6G6n+get+Mwelm6cv6j9pIBmAp93f7pFQUV5FYBt3V77VsNehMUhsOTGbVre25I7S68xAnerl7G1eQXLDqytsUIKN4EaV8v1IdEdN4jCNnw91kO5AMqeHaQyreYpHBMKZ9CNaIOu9QvWfSw4iMz2x4jPPlsfSq50H9qivlt461HD21sT4ZrZ1jnBPhU10niFxljNgnW7FwMcragBSdUaGXVtiJ7qlKLWx07LLhbQFtFI2RR6KBSLmHUaBdP8mo/A9Y7bQl1TbcaagxPhuPDXxqWYhoIIIjeaCM0YblGQfxfOKTd90+H+adS4uVlP6xjnEHh4t8KYW2WUeHyrrTJEv1MvC3dW3EZiSD/AAkEfXzNaLtWXdA5vaW8gY5WBYDL7gInj3jzrTDc0maVswi/e4Eb6bVH4m3ckG20cDTuJxPaiaYOLhZPj+PnSckNQ5jXzW3U8QR6isl6Ov8As2KuIkid9NOIG/CtPtYgOA3Pn86q2GwVu/ba2uHUXspAd4idg0jX1FUj6hbobOJU2/aQ2XLvBggDffQ8dae6CNx7vtLbhcOSTknM2oiCY07Wu9ROP6DxttAr22e2mwRgwjwXteo0rugekHskoUdl/VyksDvoQOfCnqjN2jRrSLxP58qrHWx5ugDgg9SSfwqTsdLWvZqzuEJ3V59oDJEFACRtUB0reFy4zKZUxBgjQKBsdankfQca9RFvaB4VIdDYYZyQIyiZG5zSN/I+tCxU10MnZY8z8gPqTXNklUTqxq5Egs8z60+ksVX9ZgvqYpg05hW/SJ3Et/Ipf6VypWzqbpD+IId2aPeYn1JNDthxypxDS6Wx0uiJ6TxFuwoZ+JgAbnmfAfnevMRjbNsZi0jKrSoJlWJVSI31B9KV0lgUvMue3cbIdNVAI4jU7GB36Vz9GBmn2Z0KwDcEfo8xUe6TEsZE8BVUo0rIycrdA9/pS0sxmbtBZGWCWXMIJIER86kMKA6hoidYkH4gkUKvQSrsir2i4h30LAAxBHDSpOwAoVZExG+p9SSdjzoT416Qwu/UPIgFKt+8O7X0E/SkzXKdCeZjyGp/t9aktjskOqU3MTp9xGbbvyf3H0q75ApnNJ4zvqe7uFV/qFhMpu3ABJyrMb+8xE+a1cLqZhGx76rCHptHP9RJOdLQAgzba8+7xqm9Zvs5tYnM9gLauamIi25/aA9wnmvPY1c7dp7ZJyj4kem80m7eI358FJ/GrQnSs52rPnjpjq9ew1w27yZG4cQwHFWGjDw24xUS9iK+ksfhLd+2bd1A6HgdCDzB0KnvEGsv6z/Z7ctzcwpa6m5Q63F8I/1B4a9x3q8ciYrjRnRt15Ap25bIJB3Gh7iNwaaIqgh009hsU9tw9t2RxsysVYeY4UzFdFYxeOjftBYgJjbK302zqAl0DyhW8Oz41ZbGPwFxQ1vHi2D9y4CGU8jJHw0rIqIs7UrxxYeTC3d7hnKFHjRJvKtsKGEgR56n60OmFuvpr8qct9EsDJePiKZGHOgukVs3g7EgZTxMSTs0cNzJ4gVf7PSilcwYFefAd0jSqMmCQROp5kAfCilw2iNEcDI011gDj51qsBZn6RQyZB0GxBMCeXjTL49QSDsACI1meZ2obB2BkzdlT3zroedO28ECoOkDXfs6/GaX7ZuQFielgBMa75QJJ8hTSI57cshkkQxBgniB8jUyMIkDaPX40n2Y79OfdVIxoRuyJe9fDAi88DvHxEQfOlu+KuCGvsF/ZyqT5gfKKKVG4ivWZRrPdv8A4pm2ZHYTBLb1gFjuSBMmoB7ua5c/e+YzfWrC94BJ5Tvrt51WcMfePNz8IX6VHJorDY9FTvRqxbHeSfiahBU/hlhFHID5VyZNHZi2OtS8P7zHkjf1Qn91INKtbOe5V9Wzf2VKOystClNDTeJIGUa6Huk/TL8aIU0rNFBdBfYP7G6dPaR4AH6Dv/OlOJhW1z3GPw4zz8BQt9i7gJcT3YXtmQ3ak5Bo2hG+2XvmhiilIa7KqoAIUg5WIyksxObtBdf2d+NUSb/gm2l/JIpgLZntFoMHtbEa6xqD/inbeFRSCBqNpJMb8z3n1oGzi1thiA5BYkklYmGLQAdIyNw1MxXjdKOZC250MEGVJ4AGPA+sbaq4yegqUUSzNpSm0Cjuk+La/wC3LQWHul4kEEtEEEcYG/dFFPcBJPDh4cPhUmqGuzQOp9vJhQY99mb45B8FqaZOXp+dqH6Ms+zs204qig+MCfjNFBq6oKkkcUnbbGvbEaEac+NIu2wRIg+O3j3GnWAOlDvbI1I05j6iiwIHUAqSADy1P55U3mHlTipbzZiChPEE5Tw1UGJjjSL9oq0hpB2/D886nckMV7rJ1RsYyWYZLn/MUa6cHXZ/PXkRWT9Yuqd/Bmbi5k4XF1Q8p4oe4+RNbvtuCB4V46BgRAIOhBggjlruO6rQyNCuNnzSyRSCK1zrF9ntu5L4WLb/APLP+mf3TvbPdqO4VmfSPRlyw5t3bbIw4HlzB2Yd40q0ZqWibVEfT1namytFYXDsVkAxNOmCi42bJggjfiR6Um5hSeKgfnh/mpBbTV6tocdaNAsjEwaycxLcsunmZB9KkLWGRDIXkBxjv/zTuWNhXiLqaKQrHnRI7u+P+9DCwpbMzMwn3Tt/2p+3bpUevAU4Ae7eYgBUJ1j3ogDbXiK6+xIjXyp5bZ48OHfXlxaBgS6J589KYdvzNPZO+Y323oW94UDDONxOVGC8RHjUTZYAADiSfUyfnRF9YnmaCUQw5VKaLY2SCCdO/wCcCrEKr+D1dR3/AC1+lT4rjy7OzD5FGh8Wlw24tsVl9SInsIYEHvuA+VPE0uewveWb1hf7KSLrspJX0RJw99hDMNSTozDLmCxEDXL24G2op1Oj2LKzMDl4QdYMg+9odW5jtUfmoN8PmOrtvMAwN/z6Uym/wK4L8i7eFVGzF47MfdA3YztIMseNNrbsIInYAQC2wOZdF00mZpm5hkDAezLSJmdBGnr+NO2byiTcCJPCRPGZM67/ADo97tg61SHExduewhOYzIXiYEk8DB48jRRegmxq/dk+APfx8qZuYxv1Y7yQKVxbCpJElbuak8gfU9kfEg+Vee1qK/4lssZgCTJgE6DbX19BTmGY/eJPp9Kb7TEeRdl36v8AW90i3iJdOFzd1/eH3x8fGr1YurcUOjBlbUMDIPnWN27nKrT1N6Yt23Np5UudGlis8mWYB/aA8as1RzJmgGuBpsRM8Y+FOAUphu6kjhQbgroF8uB7wRtUhXMO6tQbAExA0DaA8G+hpVzBmZQ+W/oafu4cQYGh4HY0Mjm3tMD7u8eFCjWMMpG9RXT/AENaxlsW7mYQcwZSAwPGCQRqOYqyLiLdzSJPI7j891DX8Gy6jUVtdo29mLdZepF3Dzctzct8wO2n76jcftDTmBUJgR2B5/Ot5dDWb9abVlsQ2S0BAh8oABeSWO2u4E91UjJsFUPPwrxa6urqOcUd69rq6sHwe2veX88qeT3vSva6mQojFe8/j9aGvfn0rq6gEj0pq/vXV1AwBe3b88qAfcV1dSSKQJHo3/UXxP8AtapwV1dXBl2d2LRzUpvct/un/wC49dXUi0UfgbpNdXVmEBx+x8D9KGwuzfvGurqtHRCewy5tUba96urqMNgnoLbh50rhXtdVznFj3aKwfvp+8PmK6upZaMbDhv8ATWiOFdXVJaCKFctdXUxhPPxpjE7+VdXUDEaf9X0qcf3PKurqCCyMxG486zHrB/8AM3f3voK6uquLbBLR/9k='  # Tu cadena de imagen base64

    # Decodificar la imagen base64
     imagen_bytes = base64.b64decode(imagen_base64)

# Ruta de la carpeta del proyecto y de la carpeta 'images'
     ruta_proyecto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Subir un nivel desde la carpeta de la aplicación
     ruta_images = os.path.join(ruta_proyecto, 'images')

# Crear la carpeta 'images' si no existe
     if not os.path.exists(ruta_images):
         os.makedirs(ruta_images)

# Nombre del archivo de imagen que deseas crear
     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
     nombre_imagen = f'imagen_{timestamp}.jpg'  # Puedes cambiar la extensión según el tipo de imagen

# Ruta completa del archivo de imagen
     ruta_imagen = os.path.join(ruta_images, nombre_imagen)

# Guardar la imagen decodificada en la carpeta 'images'
     with open(ruta_imagen, 'wb') as archivo_imagen:
         archivo_imagen.write(imagen_bytes)

# Imprimir si se logró guardar la imagen y la ruta donde se guardó
     ruta_relativa_imagen = os.path.join('images', nombre_imagen)
     print("Ruta relativa de la imagen:", ruta_relativa_imagen)

        # Retornar una respuesta HTTP para indicar que la operación fue exitosa
     return HttpResponse("La imagen se ha guardado correctamente en la ruta estática. Ruta: {}".format(ruta_imagen))

    except Exception as e:
        # Imprimir si ocurrió algún error al intentar guardar la imagen
        print("Error al guardar la imagen:", str(e))
        # Retornar una respuesta HTTP para indicar que ocurrió un error
        return HttpResponse("Error al intentar guardar la imagen.")


def votos_partido (request):
     # Lógica para años
  hoy = datetime.today().date()
  año_actual = hoy.year
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
  años = []
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto

  for i in range(año_actual, año_actual+11, +1):
    años.append(i)

  return render(request, 'computos_eletorales/Votos_por_Partido/Index.html', {
    
      'años': años,
      'captura': 'Uno',
        **context
  })


def Resumen_actas(request):
     # Lógica para años
  hoy = datetime.today().date()
  año_actual = hoy.year
  Usuario = Inicio.objects.get(id_usuario=request.session['ID_USUARIO'])
  Pantallas = UsuariosPantallas.objects.get(id_usuario=request.session['ID_USUARIO'])

  context = {}
  if Usuario.per_regiscandidatura is not None:
     context['regiscandidatura'] = Usuario.per_regiscandidatura
  if Pantallas.revision_ople is not None:
     context['revision_ople'] = Pantallas.revision_ople
  if Pantallas.registro_de_gubernatura is not None:
      context['registro_de_gubernatura'] = Pantallas.registro_de_gubernatura
  if Pantallas.registro_de_ayuntamiento is not None:
      context['registro_de_ayuntamiento'] = Pantallas.registro_de_ayuntamiento
  if Pantallas.diputaciones_de_mayoria is not None:
      context['diputaciones_de_mayoria'] = Pantallas.diputaciones_de_mayoria
  if Pantallas.diputaciones_de_rp is not None:
      context['diputaciones_de_rp'] = Pantallas.diputaciones_de_rp
  if Pantallas.armado_de_documentacion is not None:
      context['armado_de_documentacion'] = Pantallas.armado_de_documentacion
  if Pantallas.entrega_a_los_caes is not None:
      context['entrega_a_los_caes'] = Pantallas.entrega_a_los_caes
  if Pantallas.caes_entrega_a_los_presidentes is not None:
      context['caes_entrega_a_los_presidentes'] = Pantallas.caes_entrega_a_los_presidentes
  if Pantallas.entrega_de_paquetes_en_ca is not None:
      context['entrega_de_paquetes_en_ca'] = Pantallas.entrega_de_paquetes_en_ca
  if Pantallas.resumen_de_paquetes is not None:
      context['resumen_de_paquetes'] = Pantallas.resumen_de_paquetes
  if Pantallas.traslado_de_paquetes is not None:
      context['traslado_de_paquetes'] = Pantallas.traslado_de_paquetes
  if Pantallas.registro_de_representantes is not None:
      context['registro_de_representantes'] = Pantallas.registro_de_representantes
  if Pantallas.representantes_ople is not None:
      context['representantes_ople'] = Pantallas.representantes_ople
  if Pantallas.registro_de_observadores is not None:
      context['registro_de_observadores'] = Pantallas.registro_de_observadores
  if Pantallas.agregar_candidatos is not None:
      context['agregar_candidatos'] = Pantallas.agregar_candidatos
  if Pantallas.computo_de_votos is not None:
      context['computo_de_votos'] = Pantallas.computo_de_votos
  if Pantallas.porcentajes_de_avances is not None:
      context['porcentajes_de_avances'] = Pantallas.porcentajes_de_avances
  if Pantallas.resumen_de_actas is not None:
      context['resumen_de_actas'] = Pantallas.resumen_de_actas
  if Pantallas.votos_por_partido is not None:
      context['votos_por_partido'] = Pantallas.votos_por_partido
  if Pantallas.principios is not None:
      context['principios'] = Pantallas.principios
  if Pantallas.acciones_afirmativas is not None:
      context['acciones_afirmativas'] = Pantallas.acciones_afirmativas
  if Pantallas.documentos is not None:
      context['documentos'] = Pantallas.documentos
  if Pantallas.entidades_federativas is not None:
      context['entidades_federativas'] = Pantallas.entidades_federativas
  if Pantallas.distritos is not None:
      context['distritos'] = Pantallas.distritos
  if Pantallas.municipios is not None:
      context['municipios'] = Pantallas.municipios
  if Pantallas.cargos_entrega is not None:
      context['cargos_entrega'] = Pantallas.cargos_entrega
  if Pantallas.partidos is not None:
      context['partidos'] = Pantallas.partidos
  if Pantallas.casillas is not None:
      context['casillas'] = Pantallas.casillas
  if Pantallas.centros_de_acopio is not None:
      context['centros_de_acopio'] = Pantallas.centros_de_acopio
  if Pantallas.usuarios is not None:
      context['usuarios'] = Pantallas.usuarios
  if Pantallas.tipo_eleccion is not None:
      context['tipo_eleccion'] = Pantallas.tipo_eleccion
  if Pantallas.partidos_coaliciones is not None:
      context['partidos_coaliciones'] = Pantallas.partidos_coaliciones
  if Pantallas.eleccion_documentos is not None:
      context['eleccion_documentos'] = Pantallas.eleccion_documentos
  if Usuario.per_paquetes is not None:
        context['paquetes'] = Usuario.per_paquetes
  if Usuario.per_reprecomputos is not None:
        context['reprecomputos'] = Usuario.per_reprecomputos
  if Usuario.per_computoselectorales is not None:
        context['computoselectorales'] = Usuario.per_computoselectorales
  if Usuario.per_observadores is not None:
        context['observadores'] = Usuario.per_observadores
  if Usuario.per_configuracion is not None:
        context['configuracion'] = Usuario.per_configuracion  
  logos = get_object_or_404(Oples, idestado=Usuario.idestado.idestado)
  context['logo'] = logos.logo # Agregar 'años' al diccionario de contexto        
  años = []
  for i in range(año_actual, año_actual+11, +1):
    años.append(i)

  return render(request, 'computos_eletorales/Resumen_actas/Index.html', {
    
      'años': años,
      'captura': 'Uno',
        **context
  })

def Imprimir_reporte_global(request, anio, nombreeleccion, idcargo):
    # Crear un nuevo documento PDF
    pdf = FPDF('L', 'mm', 'Letter')  # Orientación horizontal
    pdf.set_auto_page_break(auto=True, margin=2)  # Auto salto de página con un margen de 2mm
    pdf.set_margins(left=5, top=10, right=15)  # Márgenes izquierdo y derecho de 5mm, superior de 10mm
    pdf.add_page()  # Agregar una página en blanco

    # Obtener datos del estado, partido, proceso y tipo de cargo
    partido = get_object_or_404(Partidos, idpartido=request.session['ID_PARTIDO'])
    estado = get_object_or_404(Estados, idestado=request.session['ID_ESTADO'])
    ople = get_object_or_404(Oples, idestado=request.session['ID_ESTADO'])
    proceso = get_object_or_404(Procesos, descrip=nombreeleccion, idestado=request.session['ID_ESTADO'])
    tipo_cargo = get_object_or_404(Tipocargo, idtipo_cargo=idcargo)

    # Establecer el tamaño y tipo de fuente
    pdf.set_font('Arial', '', 11)

    # Agregar el logo en la esquina superior izquierda
    pdf.image(ople.logo.path, x=10, y=8, w=30)
    pdf.image(partido.logo.path, x=pdf.w - 40, y=8, w=30)  # Esquina superior derecha

    # Agregar título
    pdf.cell(0, 5, ople.nombre_completo, 0, 1, 'C')
    pdf.cell(0, 5, f'{estado.nombre_edo}', 0, 1, 'C')
    pdf.cell(0, 5, f'{proceso.descrip}', 0, 1, 'C')
    pdf.cell(0, 5, f'{tipo_cargo.descrip_tcargo}', 0, 1, 'C')

    # Obtener la fecha actual en español
    fecha_actual = format_date(datetime.now(), format='full', locale='es_ES')
    pdf.cell(0, 5, f'{fecha_actual}', 0, 1, 'C')
    pdf.ln(25)

    # Encabezados de columna
    pdf.set_font('Arial', 'B', 10)
    epw = pdf.w - 2 * pdf.l_margin  # Ancho máximo de la página
    encabezados = ['Nombres', 'Apellido', 'Sobrenombre', 'Género', 'Estado', 'Ocupación', 'Domicilio']
    anchos_columnas = [0] * len(encabezados)  # Inicializar anchos de columnas

    # Obtener candidatos para el proceso y cargo especificados
    candidatos = Candidatos.objects.filter(idproceso=proceso.idproceso, idtipo_cargo=idcargo)

    # Calcular el ancho máximo de cada columna
    for candidato in candidatos:
        genero = 'Hombre' if candidato.genero == 'M' else 'Mujer' if candidato.genero == 'F' else 'No Binario'
        for i, campo in enumerate([candidato.nombres, f"{candidato.apaterno} {candidato.amaterno}", candidato.apodo, genero, candidato.idestado.nombre_edo, candidato.ocupacion, candidato.domicilio]):
            ancho_campo = pdf.get_string_width(campo) + 6
            anchos_columnas[i] = max(anchos_columnas[i], ancho_campo)

    # Ajustar el ancho de las columnas
    col_width = epw / sum(anchos_columnas)
    col_positions = []
    x = pdf.l_margin
    for ancho in anchos_columnas:
        col_positions.append(x)
        pdf.cell(ancho * col_width, 7, encabezados[len(col_positions) - 1], 1, 0, 'C')
        x += ancho * col_width
    pdf.ln(7)

    # Agregar datos de candidatos a la tabla
    pdf.set_font('Arial', '', 10)
    for candidato in candidatos:
        x = pdf.l_margin
        genero = 'Hombre' if candidato.genero == 'M' else 'Mujer' if candidato.genero == 'F' else 'No Binario'
        for i, campo in enumerate([candidato.nombres, f"{candidato.apaterno} {candidato.amaterno}", candidato.apodo, genero, candidato.idestado.nombre_edo, candidato.ocupacion, candidato.domicilio]):
            pdf.cell(anchos_columnas[i] * col_width, 7, campo, 1)
            x += anchos_columnas[i] * col_width
        pdf.ln(7)

    # Guardar el PDF en un objeto de bytes
    pdf_data = pdf.output(dest='S').encode('latin1')

    # Devolver el PDF como respuesta
    response = HttpResponse(pdf_data, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Reporte_de_Candidatos.pdf"'
    return response


def ConteodeActas(request, idcargo, nombreeleccion):
    estado_id = request.session['ID_ESTADO']
    proceso = get_object_or_404(Procesos, descrip=nombreeleccion, idestado=estado_id)

    with connection.cursor() as cursor:
        # Llamada al procedimiento almacenado
        cursor.callproc('contarCotejadasRecontadas', [proceso.idproceso, idcargo ])
        # Obtenemos los resultados
        actas = cursor.fetchall()

    if len(actas) > 0:
        data = {'message': "Success", 'actas': actas}
    else:
        data = {'message': "Not found"}

    return JsonResponse(data)


def convertAndSave64(imagen_base64):
    try:
        # Decodificar la imagen base64
        imagen_bytes = base64.b64decode(imagen_base64)

        # Ruta de la carpeta del proyecto Django
        ruta_proyecto = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 

        # Ruta de la carpeta 'images'
        ruta_images = os.path.join(ruta_proyecto, 'images')

        # Crear la carpeta 'images' si no existe
        os.makedirs(ruta_images, exist_ok=True)

        # Generar un nombre de archivo único usando UUID
        nombre_unico = f'{uuid.uuid4()}.jpg'  # Cambia la extensión si es necesario

        # Ruta completa del archivo de imagen
        ruta_imagen = os.path.join(ruta_images, nombre_unico)

        # Guardar la imagen decodificada en la carpeta 'images'
        with open(ruta_imagen, 'wb') as archivo_imagen:
            archivo_imagen.write(imagen_bytes)

        # Devolver la ruta relativa de la imagen
        ruta_relativa_imagen = os.path.join('images', nombre_unico)
        return ruta_relativa_imagen

    except Exception as e:
        print(f"Error al guardar la imagen: {e}")
        return None


 #Servicios para la Aplicacion movil 

@csrf_exempt
def check_password(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            # 1. Buscar al usuario de manera segura sin lanzar Http404 HTML
            try:
                usuario_obj = Inicio.objects.get(usuario=username)
            except Inicio.DoesNotExist:
                return JsonResponse({
                    "data": {"idUsuario": None, "usuario": None, "timeCoordenadas": None},
                    "ok": False,
                    "code": 3,
                    "msg": "Usuario o Contraseña Incorrectos",
                    "token": ""
                })

            # 2. Verificar si la sesión ya está activa
            if usuario_obj.activo:
                return JsonResponse({
                    "ok": False,
                    "code": 4,
                    "msg": "Usuario en uso, por favor cierre sesión en su otro dispositivo.",
                    "token": ""
                })

            # 3. Llamar al procedimiento almacenado
            with connection.cursor() as cursor:
                cursor.callproc('check_user_password', [username, password])
                result = cursor.fetchone()

            if result and verify_password(usuario_obj.passencript, password):
                return JsonResponse({
                    "data": {
                        "idUsuario": result[4],
                        "usuario": f"{result[1]} {result[2]} {result[3]}",
                        "timeCoordenadas": result[7] if result[7] is not None else 0,
                        "requiereFotosPaquete": True if result[6] else False,
                    },
                    "ok": True,
                    "code": 1,
                    "msg": "Conexión Exitosa y Autenticación",
                    "token": ""
                })
            else:
                return JsonResponse({
                    "data": {"idUsuario": None, "usuario": None, "timeCoordenadas": None},
                    "ok": False,
                    "code": 3,
                    "msg": "Usuario o Contraseña Incorrectos",
                    "token": ""
                })

        except Exception as e:
            print("Error en check_password:", str(e))
            return JsonResponse({
                "ok": False,
                "code": 500,
                "msg": f"Error en el servidor: {str(e)}",
                "token": ""
            })



@csrf_exempt
def save_transfer_rqt(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        paquete = data.get('paquete')
        base64Sup = data.get('base64Sup')
        base64Inf = data.get('base64Inf')
        datos_separados = [dato.strip() for dato in paquete.split("|")]
        # Año|idestado|idProceso|idtipo_cargo|idtipoc|num_elec|casilla|Cae|NumeroPaquete
        anio = datos_separados[0]
        idestado = datos_separados[1]
        idProceso = datos_separados[2]
        idtipo_cargo = datos_separados[3]
        idtipoc = datos_separados[4]
        num_elec = datos_separados[5]
        casilla = datos_separados[6]
        Cae = datos_separados[7]
        NumeroPaquete = datos_separados[8]

        fecha = data.get('fecha')
        latitud = data.get('latitud')
        longitud = data.get('longitud')
        idUsuario = data.get('idUsuario')

        fecha_obj = datetime.strptime(fecha, '%d-%m-%Y %H:%M:%S')
        # Separar la fecha y la hora
        fecha_mysql = fecha_obj.strftime('%Y-%m-%d')  # Formato: 'YYYY-MM-DD'
        hora_mysql = fecha_obj.strftime('%H:%M:%S')   # Formato: 'HH:MM:SS'

        try:
            rutaimg1 = convertAndSave64(base64Sup)
            #time.sleep(2)
            rutaimg2 = convertAndSave64(base64Inf)
            
            with connection.cursor() as cursor:
                cursor.callproc('InsertTransladadoPaquetes', [NumeroPaquete, casilla, latitud, longitud, fecha_obj, idUsuario, rutaimg1, rutaimg2])
                connection.commit()  # Confirmar los cambios en la base de datos

            # Intentar realizar la actualización de CadenaCustodiaBi
            try:
                Bi = get_object_or_404(CadenaCustodiaBi, id_paquete=NumeroPaquete)

                # Actualizar los campos
                Bi.fecha_paq= fecha_mysql
                Bi.hora_paq = hora_mysql
                Bi.longitud_ini_paq = longitud
                Bi.latitud_ini_paq = latitud
                Bi.estatus_paq = 'Inicio'
                Bi.cantidad_ruta = 1
                Bi.cantidad_casilla = 0
                Bi.cantidad_enca=0
                Bi.cantidad_entregadoca=0

                # Guardar los cambios en la base de datos
                Bi.save()

            except Exception as e:
                # Imprimir el error en consola, pero no detener el proceso
                print(f"Error al actualizar CadenaCustodiaBi: {e}")
                return JsonResponse({"ok": True, "code": 1, "msg": "Todo Correcto, pero hubo un problema con la actualización de CadenaCustodiaBi"})
            
            return JsonResponse({"ok": True, "code": 1, "msg": "Todo Correcto, Inicio del Recorrido del Paquete"})

        except Exception as e:
            print(f"Error al actual" + str(e))
            if 'El Paquete no pertenece a este CAE' in str(e):
                return JsonResponse({"ok": False, "code": 2, "msg": "El Paquete no pertenece a este CAE"})
            elif 'El paquete aún no puede iniciar su traslado' in str(e):
                return JsonResponse({"ok": False, "code": 2, "msg": "El paquete aún no puede iniciar su traslado"})
            else:
                return JsonResponse({"ok": False, "code": 3, "msg": "Ya inició el recorrido del paquete" })
        
        finally:
            # Cerrar la conexión a la base de datos
            connection.close()
            # Limpiar las variables de memoria
            del base64Sup, base64Inf

@csrf_exempt
def register_route_rqt(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        fecha = data.get('fecha')
        latitud = data.get('latitud')
        longitud = data.get('longitud')
        idUsuario = data.get('idUsuario')
        paquetes = data.get('paquetes')

        rutas_insertadas = True
        updates_exitosos = True

        try:
            # Convertir la fecha y hora al formato de MySQL
            fecha_obj = datetime.strptime(fecha, '%d-%m-%Y %H:%M:%S')
            fecha_mysql = fecha_obj.strftime('%Y-%m-%d')  # Formato: 'YYYY-MM-DD'
            hora_mysql = fecha_obj.strftime('%H:%M:%S')   # Formato: 'HH:MM:SS'
        except ValueError:
            return JsonResponse({
                "ok": False,
                "code": 0,
                "msg": "Formato de fecha y hora incorrecto",
                "token": ""  # Agrega la lógica de generación de token aquí
            })

        try:
            for paquete in paquetes:
                datos_separados = [dato.strip() for dato in paquete.get('paquete').split("|")]

                # Año|idestado|idProceso|idtipo_cargo|idtipoc|num_elec|casilla|Cae|NumeroPaquete
                anio = datos_separados[0]
                idestado = datos_separados[1]
                idProceso = datos_separados[2]
                idtipo_cargo = datos_separados[3]
                idtipoc = datos_separados[4]
                num_elec = datos_separados[5]
                casilla = datos_separados[6]
                Cae = datos_separados[7]
                NumeroPaquete = datos_separados[8]

                try:
                    with connection.cursor() as cursor:
                        cursor.callproc('InsertCoordenadasPaquetes', [fecha_obj, longitud, latitud, idUsuario, NumeroPaquete, casilla])
                except Exception as e:
                    print(f"Error al insertar coordenadas para el paquete {NumeroPaquete}: {e}")
                    rutas_insertadas = False

                try:
                    Bi = get_object_or_404(CadenaCustodiaBi, id_paquete=NumeroPaquete)

                    # Actualizar los campos
                    Bi.fecha_paq = fecha_mysql
                    Bi.hora_paq = hora_mysql
                    Bi.longitud_ini_paq = longitud
                    Bi.latitud_ini_paq = latitud
                    Bi.estatus_paq = 'Ruta'
                    Bi.cantidad_ruta = 1  # Incrementar el contador de ruta
                    Bi.cantidad_casilla = 0
                    Bi.cantidad_enca=0
                    Bi.cantidad_entregadoca=0

                    # Guardar los cambios en la base de datos
                    Bi.save()

                except Exception as e:
                    print(f"Error al actualizar CadenaCustodiaBi para el paquete {NumeroPaquete}: {e}")
                    updates_exitosos = False

            if rutas_insertadas and updates_exitosos:
                return JsonResponse({
                    "ok": True,
                    "code": 1,
                    "msg": "Coordenadas y actualizaciones registradas con éxito",
                    "token": ""  # Agrega la lógica de generación de token aquí
                })
            elif rutas_insertadas and not updates_exitosos:
                return JsonResponse({
                    "ok": True,
                    "code": 2,
                    "msg": "Coordenadas registradas con éxito, pero hubo un problema con la actualización de CadenaCustodiaBi",
                    "token": ""  # Agrega la lógica de generación de token aquí
                })
            elif not rutas_insertadas and updates_exitosos:
                return JsonResponse({
                    "ok": True,
                    "code": 3,
                    "msg": "Actualizaciones realizadas con éxito, pero hubo errores al registrar las coordenadas",
                    "token": ""  # Agrega la lógica de generación de token aquí
                })
            else:
                return JsonResponse({
                    "ok": False,
                    "code": 4,
                    "msg": "Hubo errores al registrar las coordenadas y las actualizaciones",
                    "token": ""  # Agrega la lógica de generación de token aquí
                })

        except Exception as e:
            return JsonResponse({
                "ok": False,
                "code": 0,
                "msg": str(e),
                "token": ""  # Agrega la lógica de generación de token aquí
            })
        finally:
            connection.close()
            del paquetes, data, fecha, latitud, longitud, idUsuario


@csrf_exempt
def deliver_package_rqt(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            paquete = data.get('paquete')
            base64Sup = data.get('base64Sup')
            base64Inf = data.get('base64Inf')
            fecha = data.get('fecha')
            latitud = float(data.get('latitud'))
            longitud = float(data.get('longitud'))
            idUsuario = data.get('idUsuario')
            
            # Convertir la fecha y hora al formato de MySQL
            fecha_obj = datetime.strptime(fecha, '%d-%m-%Y %H:%M:%S')
            fecha_mysql = fecha_obj.strftime('%Y-%m-%d')  # Formato: 'YYYY-MM-DD'
            hora_mysql = fecha_obj.strftime('%H:%M:%S')   # Formato: 'HH:MM:SS'

            # Separar los datos del paquete
            datos_separados = [dato.strip() for dato in paquete.split("|")]
                # Año|idestado|idProceso|idtipo_cargo|idtipoc|num_elec|casilla|Cae|NumeroPaquete
            anio = datos_separados[0]
            idestado = datos_separados[1]
            idProceso = datos_separados[2]
            idtipo_cargo = datos_separados[3]
            idtipoc = datos_separados[4]
            num_elec = datos_separados[5]
            casilla = datos_separados[6]
            Cae = datos_separados[7]
            NumeroPaquete = datos_separados[8]

            with connection.cursor() as cursor:
                #cursor.callproc('Consultar_cordenadas', [num_paquete])
                #result = cursor.fetchone()

                if True: #result:
                    # Suponiendo que `result` contiene coordenadas de la BD
                    
                    #longitud_db, latitud_db = result
                    margen_error = 5.0

                    if True: #abs(latitud - latitud_db) <= margen_error and abs(longitud - longitud_db) <= margen_error:
                        rutaimg1 = convertAndSave64(base64Sup)
                        #time.sleep(1)
                        rutaimg2 = convertAndSave64(base64Inf)
                        cursor.callproc('InsertTransladadoPaquetesDelivery', [fecha_obj, longitud, latitud, idUsuario, rutaimg1, rutaimg2, 1, NumeroPaquete, casilla])
                        connection.commit()  # Confirmar los cambios en la base de datos
                        rows_affected = cursor.rowcount

                        if rows_affected == 0:
                            return JsonResponse({"ok": False, "code": 0, "msg": "El paquete ya ha llegado al Centro de Acopio."})
                        
                        try:
                            # Intentar realizar la actualización de CadenaCustodiaBi
                            Bi = get_object_or_404(CadenaCustodiaBi, id_paquete=NumeroPaquete)

                            # Actualizar los campos
                            Bi.fecha_paq = fecha_mysql
                            Bi.hora_paq = hora_mysql
                            Bi.longitud_fin_paq = longitud
                            Bi.latitud_fin_paq = latitud
                            Bi.estatus_paq = 'Llego'
                            Bi.cantidad_ruta = 0  # Incrementar el contador de ruta
                            Bi.cantidad_casilla = 0
                            Bi.cantidad_enca=1
                            Bi.cantidad_entregadoca=0

                            # Guardar los cambios en la base de datos
                            Bi.save()

                            return JsonResponse({"ok": True, "code": 1, "msg": "Llegada al centro de acopio correcta y CadenaCustodiaBi actualizada."})

                        except Exception as e:
                            print(f"Error al actualizar CadenaCustodiaBi para el paquete {NumeroPaquete}: {e}")
                            return JsonResponse({"ok": True, "code": 2, "msg": "Llegada al centro de acopio correcta, pero hubo un problema al actualizar CadenaCustodiaBi."})

                    else:
                        return JsonResponse({"ok": False, "code": 50, "msg": "Centro de acopio equivocado"})
                else:
                    return JsonResponse({"ok": False, "code": 0, "msg": "No se encontraron resultados para el paquete proporcionado."})
        
        except Exception as e:
            error_message = str(e)
            if "'" in error_message:
                error_message = error_message.split("'")[1]
            return JsonResponse({"ok": False, "code": 0, "msg": error_message})
        
        finally:
            connection.close()
            del base64Sup, base64Inf
    else:
        return JsonResponse({"ok": False, "code": 0, "msg": "La solicitud debe ser de tipo POST."})



@csrf_exempt
def deliver_package(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            paquete = data.get('paquete')
            fecha = data.get('fecha')
            latitud = float(data.get('latitud'))
            longitud = float(data.get('longitud'))
            idUsuario = data.get('idUsuario')

            # Convertir la fecha y hora al formato MySQL
            fecha_obj = datetime.strptime(fecha, '%d-%m-%Y %H:%M:%S')
            fecha_mysql = fecha_obj.strftime('%Y-%m-%d')  # Formato: 'YYYY-MM-DD'
            hora_mysql = fecha_obj.strftime('%H:%M:%S')   # Formato: 'HH:MM:SS'

            # Separar los datos del paquete
            datos_separados = [dato.strip() for dato in paquete.split("|")]
            anio = datos_separados[0]
            idestado = datos_separados[1]
            idProceso = datos_separados[2]
            idtipo_cargo = datos_separados[3]
            idtipoc = datos_separados[4]
            num_elec = datos_separados[5]
            casilla = datos_separados[6]
            Cae = datos_separados[7]
            NumeroPaquete = datos_separados[8]

            with connection.cursor() as cursor:
                # Llamar al procedimiento almacenado para consultar las coordenadas
                #cursor.callproc('Consultar_cordenadas', [num_paquete])
                
                #result = cursor.fetchone()

                if True: #result:
                    # Suponiendo que `result` contiene coordenadas de la BD
                    #longitud_db, latitud_db = result
                    margen_error = 5.0

                    if True: #abs(latitud - latitud_db) <= margen_error and abs(longitud - longitud_db) <= margen_error:
                        # Llamar al procedimiento almacenado para registrar la entrega del paquete
                        cursor.callproc('InsertTransladadoPaquetesEntrega', [NumeroPaquete, idUsuario, latitud, longitud, fecha_obj, 1, casilla])
                        connection.commit()

                        try:
                            # Intentar realizar la actualización de CadenaCustodiaBi
                            Bi = get_object_or_404(CadenaCustodiaBi, id_paquete=NumeroPaquete)

                            # Actualizar los campos
                            Bi.fecha_paq = fecha_mysql
                            Bi.hora_paq = hora_mysql
                            Bi.longitud_fin_paq = longitud
                            Bi.latitud_fin_paq = latitud
                            Bi.estatus_paq = 'Entregado'
                            Bi.cantidad_ruta = 0  # Incrementar el contador de ruta
                            Bi.cantidad_casilla = 0
                            Bi.cantidad_enca=0
                            Bi.cantidad_entregadoca=1
                            # Guardar los cambios en la base de datos
                            Bi.save()

                            return JsonResponse({
                                "ok": True,
                                "code": 1,
                                "msg": "Paquete entregado con éxito y CadenaCustodiaBi actualizada.",
                                "token": ""  # Agrega la lógica de generación de token aquí
                            })

                        except Exception as e:
                            print(f"Error al actualizar CadenaCustodiaBi para el paquete {NumeroPaquete}: {e}")
                            return JsonResponse({
                                "ok": True,
                                "code": 2,
                                "msg": "Paquete entregado con éxito, pero hubo un problema al actualizar CadenaCustodiaBi.",
                                "token": ""  # Agrega la lógica de generación de token aquí
                            })

                    else:
                        return JsonResponse({
                            "ok": False,
                            "code": 50,
                            "msg": "No se puede entregar el paquete fuera del centro de acopio.",
                            "token": ""  # Agrega la lógica de generación de token aquí
                        })
                else:
                    return JsonResponse({
                        "ok": False,
                        "code": 0,
                        "msg": "No se encontraron resultados para el paquete proporcionado.",
                        "token": ""  # Agrega la lógica de generación de token aquí
                    })
        except Exception as e:
            error_message = str(e)
            if "'" in error_message:
                error_message = error_message.split("'")[1]
            return JsonResponse({
                "ok": False,
                "code": 0,
                "msg": error_message,
                "token": ""  # Agrega la lógica de generación de token aquí
            })
    else:
        return JsonResponse({
            "ok": False,
            "code": 0,
            "msg": "La solicitud debe ser de tipo POST.",
            "token": ""  # Agrega la lógica de generación de token aquí
        })


@csrf_exempt
def UpdateCredentials(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('newpassword')
        palabra_secreta = data.get('palabra_secreta')

        try:
            with connection.cursor() as cursor:
                if palabra_secreta:
                    # Llama al procedimiento con la palabra secreta
                    cursor.callproc('ActualizarUsuarioYPassEncriptConPalabraSecreta', [username, password, palabra_secreta])
                else:
                    # Llama al procedimiento sin la palabra secreta
                    cursor.callproc('ActualizarPassEncript', [username, password])

            return JsonResponse({
                "data": None,
                "ok": True,
                "code": 1,
                "msg": "Contraseña Actualizada",
                "token": ""  # Agrega la lógica de generación de token aquí
            })
        except Exception as e:
            print (e)
            return JsonResponse({
                "data": None,
                "ok": False,
                "code": 0,
                "msg": "Palabra Secreta Incorrecta",
                "token": ""
            })
@csrf_exempt
def SaveIncident(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            paquete = data.get('paquete')
            fecha = data.get('fecha')
            latitud = float(data.get('latitud'))
            longitud = float(data.get('longitud'))
            idUsuario = data.get('idUsuario')
            comentario = data.get('comentario')
            todos = data.get('todos')
            estatus = data.get('estatus')

            # Convertir la fecha y hora al formato MySQL
            fecha_obj = datetime.strptime(fecha, '%d-%m-%Y %H:%M:%S')
            fecha_mysql = fecha_obj.strftime('%Y-%m-%d')  # Formato: 'YYYY-MM-DD'
            hora_mysql = fecha_obj.strftime('%H:%M:%S')   # Formato: 'HH:MM:SS'

            # Separar los datos del paquete
            datos_separados = [dato.strip() for dato in paquete.split("|")]
            anio = datos_separados[0]
            idestado = datos_separados[1]
            idProceso = datos_separados[2]
            idtipo_cargo = datos_separados[3]
            idtipoc = datos_separados[4]
            num_elec = datos_separados[5]
            casilla = datos_separados[6]
            Cae = datos_separados[7]
            NumeroPaquete = datos_separados[8]
            incidentes_actualizados = False
            bi_actualizado = False

            if todos:
                with connection.cursor() as cursor:
                    # Llamar al procedimiento almacenado para obtener paquetes sin repetir
                    cursor.callproc('obtener_paquetes_sin_repetir', [idUsuario])
                    results = cursor.fetchall()

                    print("Resultados del procedimiento obtener_paquetes_sin_repetir:")
                    for result in results:
                        num_paquete = result[0]

                        try:
                            with connection.cursor() as cursor_inner:
                                cursor_inner.callproc('UpdateTransladadoIncidencia', [
                                    num_paquete, idUsuario, latitud, longitud, fecha_obj, comentario, casilla, estatus
                                ])
                                connection.commit()  # Confirmar los cambios en la base de datos
                                
                                # Actualizar la tabla CadenaCustodiaBi
                                try:
                                    bi_record = get_object_or_404(CadenaCustodiaBi, id_paquete=num_paquete)
                                    bi_record.fecha_paq = fecha_mysql
                                    bi_record.hora_paq = hora_mysql
                                    bi_record.longitud_ini_paq = longitud
                                    bi_record.latitud_ini_paq = latitud
                                    bi_record.estatus_paq = estatus
                                    bi_record.cantidad_ruta = 0
                                    bi_record.cantidad_casilla = 0
                                    bi_record.cantidad_enca = 0
                                    bi_record.cantidad_entregadoca = 0
                                    if estatus == 'Incidente':
                                        bi_record.emergencia = 0
                                        bi_record.incidencia = 1
                                    else: 
                                        bi_record.emergencia = 1
                                        bi_record.incidencia = 0 
                                    bi_record.comentarios = comentario    
                                    bi_record.save()
                                    bi_actualizado = True
                                except Exception as e:
                                    print(f"Error al actualizar CadenaCustodiaBi para num_paquete {num_paquete}: {e}")
                                
                                incidentes_actualizados = True
                        except Exception as e:
                            print(f"Error al actualizar incidente para num_paquete {num_paquete}: {e}")

                mensaje = "Incidentes actualizados con éxito"
                if bi_actualizado:
                    mensaje += " y tabla CadenaCustodiaBi actualizada correctamente."
                else:
                    mensaje += " Incidentes actualizados pero no se pudo actualizar la tabla CadenaCustodiaBi."
                
                return JsonResponse({
                    "data": None,
                    "ok": incidentes_actualizados,
                    "code": 1,
                    "msg": mensaje,
                    "token": ""  # Agrega la lógica de generación de token aquí
                })
            else:
                with connection.cursor() as cursor:
                    cursor.callproc('UpdateTransladadoIncidencia', [
                        NumeroPaquete, idUsuario, latitud, longitud, fecha_obj, comentario, casilla, estatus
                    ])
                    connection.commit()  # Confirmar los cambios en la base de datos

                    # Actualizar la tabla CadenaCustodiaBi
                    try:
                        bi_record = get_object_or_404(CadenaCustodiaBi, id_paquete=NumeroPaquete)
                        bi_record.fecha_paq = fecha_mysql
                        bi_record.hora_paq = hora_mysql
                        bi_record.longitud_ini_paq = longitud
                        bi_record.latitud_ini_paq = latitud
                        bi_record.estatus_paq = estatus
                        bi_record.cantidad_ruta = 0
                        bi_record.cantidad_casilla = 0
                        bi_record.cantidad_enca = 0
                        bi_record.cantidad_entregadoca = 0
                        if estatus == 'Incidente':
                            bi_record.emergencia = 0
                            bi_record.incidencia = 1
                        else: 
                            bi_record.emergencia = 1
                            bi_record.incidencia = 0 
                        bi_record.comentarios = comentario    
                        bi_record.save()
                        bi_actualizado = True
                    except Exception as e:
                        print(f"Error al actualizar CadenaCustodiaBi para num_paquete {num_paquete}: {e}")

                mensaje = "Incidente guardado con éxito"
                if bi_actualizado:
                    mensaje += " y tabla CadenaCustodiaBi actualizada correctamente."
                else:
                    mensaje += " Incidente guardado pero no se pudo actualizar la tabla CadenaCustodiaBi."

                return JsonResponse({
                    "data": None,
                    "ok": True,
                    "code": 1,
                    "msg": mensaje,
                    "token": ""  # Agrega la lógica de generación de token aquí
                })
        except Exception as e:
            error_message = str(e)
            print(f"Error al guardar el incidente: {error_message}")
            return JsonResponse({
                "data": None,
                "ok": False,
                "code": 2,
                "msg": "Error al guardar el incidente",
                "token": ""
            })
        finally:
            connection.close()  # Asegurarse de cerrar la conexión a la base de datos
    else:
        return JsonResponse({
            "data": None,
            "ok": False,
            "code": 0,
            "msg": "La solicitud debe ser de tipo POST.",
            "token": ""  # Agrega la lógica de generación de token aquí
        })




@csrf_exempt
def reset_packages(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # Verificar si se proporciona la clave específica
        if 'clave' in data and data['clave'] == 'RESTABLERCER_PAQUETES_87$#0OP':
            try:
                with connection.cursor() as cursor:
                    # Utilizar el cursor proporcionado por la conexión
                    cursor.callproc('reset_translado')

                return JsonResponse({
                    "ok": True,
                    "msg": "Se resetearon los paquetes con éxito"
                })
            except Exception as e:
                return JsonResponse({
                    "ok": False,
                    "msg": "Error al resetear los paquetes: " + str(e)
                })
        else:
            return JsonResponse({
                "ok": False,
                "msg": "Clave incorrecta"
            })

@csrf_exempt
def obtener_paquetes_por_uduario(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # Verificar si se proporciona el ID de usuario
        if 'idUsuario' in data:
            id_usuario = data['idUsuario']
            try:
                with connection.cursor() as cursor:
                    # Llamar al procedimiento almacenado con el ID de usuario proporcionado
                    cursor.callproc('obtenerPaquetesPorUsuario', [id_usuario]) #Para obtener los que puedes tener INCIDENCIAS
                    # Obtener el resultado del procedimiento almacenado
                    result = cursor.fetchone()

                # Comprobar si se obtuvo un resultado
                if result:
                    qr_data = result[0]  # asumiendo que el resultado es una cadena de texto
                    return JsonResponse({
                        "qr": qr_data,
                    })
                else:
                    return JsonResponse({
                        "ok": False,
                        "msg": "No se encontraron paquetes para el usuario proporcionado"
                    })

            except Exception as e:
                return JsonResponse({
                    "ok": False,
                    "msg": "Error al obtener los paquetes: " + str(e)
                })
        else:
            return JsonResponse({
                "ok": False,
                "msg": "ID de usuario no proporcionado en la solicitud"
            })
    else:
        return JsonResponse({
            "ok": False,
            "msg": "Método no permitido, solo se permite POST"
        })            



@csrf_exempt
def obtener_estatus_paquete_por_uduario(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # Verificar si se proporciona el ID de usuario
        if 'idUsuario' in data:
            id_usuario = data['idUsuario']
            try:
                with connection.cursor() as cursor:
                    # Llamar al procedimiento almacenado con el ID de usuario proporcionado
                    cursor.callproc('GetTransladadoPaquetesPorUsuario', [id_usuario])
                    # Obtener el resultado del procedimiento almacenado
                    result = cursor.fetchone()

                # Comprobar si se obtuvo un resultado
                if result:
                    qr_data = result[0] 
                    print (result[0] ) # asumiendo que el resultado es una cadena de texto
                    return JsonResponse({
                        "paquetes": qr_data,
                    })
                else:
                    return JsonResponse({
                        "ok": False,
                        "msg": "No se encontraron paquetes para el usuario proporcionado"
                    })

            except Exception as e:
                return JsonResponse({
                    "ok": False,
                    "msg": "Error al obtener los paquetes: " + str(e)
                })
        else:
            return JsonResponse({
                "ok": False,
                "msg": "ID de usuario no proporcionado en la solicitud"
            })
    else:
        return JsonResponse({
            "ok": False,
            "msg": "Método no permitido, solo se permite POST"
        })            
    


@csrf_exempt
def obtener_paquetes_por_uduario_incidencia(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # Verificar si se proporciona el ID de usuario
        if 'idUsuario' in data:
            id_usuario = data['idUsuario']
            try:
                with connection.cursor() as cursor:
                    # Llamar al procedimiento almacenado con el ID de usuario proporcionado
                    cursor.callproc('GetTransladadoPaquetesPorUsuario', [id_usuario])
                    # Obtener el resultado del procedimiento almacenado
                    result = cursor.fetchone()

                # Comprobar si se obtuvo un resultado
                if result:
                    qr_data = result[0] 
                    print (result[0] ) # asumiendo que el resultado es una cadena de texto
                    return JsonResponse({
                        "paquetes": qr_data,
                    })
                else:
                    return JsonResponse({
                        "ok": False,
                        "msg": "No se encontraron paquetes para el usuario proporcionado"
                    })

            except Exception as e:
                return JsonResponse({
                    "ok": False,
                    "msg": "Error al obtener los paquetes: " + str(e)
                })
        else:
            return JsonResponse({
                "ok": False,
                "msg": "ID de usuario no proporcionado en la solicitud"
            })
    else:
        return JsonResponse({
            "ok": False,
            "msg": "Método no permitido, solo se permite POST"
        })                


@csrf_exempt
def desactivar_usuario(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # Verificar si se proporciona el ID de usuario
        if 'idUsuario' in data:
            id_usuario = data['idUsuario']
            try:
                # Intentar obtener el objeto del usuario
                usuario_obj = get_object_or_404(Inicio, id_usuario=id_usuario)

                # Actualizar el campo 'activo' para desactivar el usuario
                usuario_obj.activo = False
                usuario_obj.save()

                return JsonResponse({
                    "ok": True,
                    "msg": "Usuario desactivado exitosamente"
                })

            except Exception as e:
                return JsonResponse({
                    "ok": False,
                    "msg": "Error al desactivar el usuario: " + str(e)
                })
        else:
            return JsonResponse({
                "ok": False,
                "msg": "ID de usuario no proporcionado en la solicitud"
            })
    else:
        return JsonResponse({
            "ok": False,
            "msg": "Método no permitido, solo se permite POST"
        })
