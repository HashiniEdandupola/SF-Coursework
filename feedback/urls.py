from django import views
from django.urls import path
from . import views

urlpatterns = [
    # path("", views.feedbacks, name='feedbacks'),
    path('', views.feedback_form, name='feedback_insert'),
    path('<int:id>/', views.feedback_form, name='feedback_update'),
    path('delete/<int:id>/', views.feedback_delete, name='feedback_delete'),
    path('list/', views.feedback_list, name='feedback_list'),
    path('success/', views.feedback_success, name='feedback_success'),
]
