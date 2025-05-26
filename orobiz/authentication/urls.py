# admin_panel/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # This maps to the base of this app’s URL
]
