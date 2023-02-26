from django.urls import path

from Manage_System import views

urlpatterns = [
    path('', views.index),
]
