"""
URL configuration for moonlight_relax project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from salon import views
from .settings import MEDIA_ROOT, MEDIA_URL


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', views.homepage, name='homepage'),
    path('servicii/', views.servicii, name='servicii'),
    path('programare/', views.programare, name='programare'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('politica-confidentialitate/', views.politica_confidentialitate, name='politica_confidentialitate'),
    path('termeni-si-conditii/', views.termeni_si_conditii, name='termeni_si_conditii'),


] + static(MEDIA_URL, document_root=MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        # ... restul pattern-urilor tale de URL
    ] + urlpatterns