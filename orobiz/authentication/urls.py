# admin_panel/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This maps to the base of this app’s URL
    
]
