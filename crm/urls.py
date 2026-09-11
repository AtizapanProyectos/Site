from django.urls import path
from . import views

app_name = 'crm'

urlpatterns = [
    # Vista principal
    path('', views.dashboard, name='dashboard'),
    
    # APIs Web Dashboard
    path('api/encolar/', views.api_encolar_mensajes, name='api_encolar_mensajes'),
    path('api/estado/', views.api_estado_cola, name='api_estado_cola'),
    path('api/contacto/nuevo/', views.api_agregar_contacto, name='api_agregar_contacto'),
    path('api/mensaje/<int:mensaje_id>/cancelar/', views.api_cancelar_mensaje, name='api_cancelar_mensaje'),
    path('api/mensaje/<int:mensaje_id>/reintentar/', views.api_reintentar_mensaje, name='api_reintentar_mensaje'),

    # Endpoints para el Bot Nocturno (bot_nocturno.py)
    path('api/whatsapp/pendientes/', views.bot_pendientes, name='bot_pendientes'),
    path('api/whatsapp/actualizar/', views.bot_actualizar, name='bot_actualizar'),
    path('api/pendientes/', views.bot_pendientes, name='bot_pendientes_alt'),
    path('api/actualizar/', views.bot_actualizar, name='bot_actualizar_alt'),
]
