from django.contrib import admin
from django.urls import path
import include

urlpatterns = [
  path('', include('galeria.urls')),
]