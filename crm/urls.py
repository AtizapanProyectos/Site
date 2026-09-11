from django.urls import path
from . import views

app_name = 'crm'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('api/encolar/', views.api_encolar_mensajes, name='api_encolar_mensajes'),
    path('api/estado/', views.api_estado_cola, name='api_estado_cola'),
    path('api/contacto/nuevo/', views.api_agregar_contacto, name='api_agregar_contacto'),
    path('api/mensaje/<int:mensaje_id>/cancelar/', views.api_cancelar_mensaje, name='api_cancelar_mensaje'),
    path('api/mensaje/<int:mensaje_id>/reintentar/', views.api_reintentar_mensaje, name='api_reintentar_mensaje'),
]
