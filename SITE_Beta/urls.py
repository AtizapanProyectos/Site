"""
URL configuration for SITE_Beta project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from django.conf import settings
from crm import views as crm_views

urlpatterns = [
    path('secure-admin/', admin.site.urls),
    path('crm/', include('crm.urls')),

    # Endpoints globales para el Bot Nocturno (bot_nocturno.py)
    path('api/whatsapp/pendientes/', crm_views.bot_pendientes, name='global_bot_pendientes'),
    path('api/whatsapp/actualizar/', crm_views.bot_actualizar, name='global_bot_actualizar'),
    path('api/whatsapp/estado/', crm_views.bot_reporte_estado, name='global_bot_estado'),
    path('api/whatsapp/', crm_views.bot_reporte_estado, name='global_bot_index'),

    path('', include('Siteone.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
