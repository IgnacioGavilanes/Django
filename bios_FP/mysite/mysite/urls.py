"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from gym.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500

handler404 = error_404
handler500 = error_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('profile/', profile, name="profile"),
    path('contact/', contact, name='contact'),
    path('register/', new_user, name='register'),
    path('login/', user_login, name="login"),
    path('private/', private, name='private'),
    path('search/', search, name='search'),
    path('exit/', exit, name='exit'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
