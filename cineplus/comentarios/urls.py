"""
URL configuration for cineplus project.

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
from django.urls import path
from . import views

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.lista_reseñas, name='lista_reseñas'),
    path('reseña/nueva/', views.crear_reseña, name='crear_reseña'),
    path('reseña/<int:reseña_id>/', views.detalle_reseña, name='detalle_reseña'),
    path('reseña/<int:reseña_id>/comentar/', views.agregar_comentario, name='agregar_comentario'),
    path('imagenes_reseñas/',views.detalle_reseña, name='imagenes_reseñas/')
]

# Configuración para servir archivos multimedia en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)