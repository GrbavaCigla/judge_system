from django.urls import path, include
from main.views import home, register

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='judge-home'),
    path('login/', auth_views.LoginView.as_view(), name='judge-login'),
    path('logout/', auth_views.LogoutView.as_view(), name='judge-logout'),
    path('register/', register, name='judge-register'),
]
