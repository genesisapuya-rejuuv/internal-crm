from django.contrib import admin
from django.urls import path, include
from rejuuv import settings
from django.conf.urls.static import static
from management import views

urlpatterns = [
    path('', views.base, name='base')
]