from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("adminlogin", views.admin_login, name='adminlogin'),
]