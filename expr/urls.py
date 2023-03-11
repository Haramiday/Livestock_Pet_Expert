"""expr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from page.views import home, ask_goat, ask_chicken, ask_cow, ask_dog, ask_cat,info
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('gt',ask_goat, name='goat'),
    path('ck',ask_chicken, name='chicken'),
    path('cw',ask_cow, name='cow'),
    path('dg',ask_dog, name='dog'),
    path('ct',ask_cat, name='cat'),
    path('information/<int:id>',info, name='info'),
] 


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)