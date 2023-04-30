from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('success/', views.booking_success, name='booking_success'),
    path('', views.booking_form, name='booking_insert'),
    path('<int:id>/', views.booking_form, name='booking_update'),
    path('delete/<int:id>/', views.booking_delete, name='booking_delete'),
    path('list/', views.booking_list, name='booking_list')
]