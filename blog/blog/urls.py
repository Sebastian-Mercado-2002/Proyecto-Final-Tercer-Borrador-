"""
URL configuration for blog project.

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
from django.urls import path
from .views import index, aplicacion_de_la_ia, impacto_educacion, impacto_laboral, acerca_de, contacto, inicio, crear_post
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('aplicacion_de_la_ia/', aplicacion_de_la_ia, name='aplicacion_de_la_ia'),
    path('impacto_educacion/', impacto_educacion, name='impacto_educacion'),
    path('impacto_laboral/', impacto_laboral, name='impacto_laboral'),
    path('acerca_de/', acerca_de, name='acerca_de'),
    path('contacto/', contacto, name='contacto'),
    path('inicio/', inicio, name='inicio'),
    path('crear_post/', crear_post, name='crear_post'),  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
