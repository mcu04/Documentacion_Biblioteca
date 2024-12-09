"""
URL configuration for Documentacion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from Aplicaciones.seguimientodocumentos import views
from django.conf import settings
from django.conf.urls.static import static
from main.views import home
from Aplicaciones.seguimientodocumentos.views import pagina_inicio
from main import views as main_views


# from Aplicaciones.seguimientodocumentos.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', pagina_inicio, name='pagina_inicio'),  # Ahora la raíz apunta a esta vista
    path("seguimiento/", include("Aplicaciones.seguimientodocumentos.urls")),  # Incluye las rutas de seguimiento
    path("auth/", include("Aplicaciones.seguimientodocumentos.autenticacion.urls")),  # Incluye las rutas de autenticación
    path('biblioteca/', include('biblioteca.urls')),   # Incluir URLs de la biblioteca
    path('main/', main_views.home, name='home'),  # Página principal
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






