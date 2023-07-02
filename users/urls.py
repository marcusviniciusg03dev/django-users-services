from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.signin, name='users-login'),
    path('register/', views.register, name='users-register'),
]