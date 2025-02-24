"""
URL configuration for desafio_login project.

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
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from . import views 

urlpatterns = [
    path('admin/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    #path('admin/login/', CustomLoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('registrar/', views.registrar_usuario, name="registrar"),
    path('menu/', views.menu_page, name="menu")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
