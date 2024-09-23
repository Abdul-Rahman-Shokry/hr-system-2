# accounts/urls.py
from django.urls import path
from .views import signUpView,MyPasswordChangeView
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('signUp/', signUpView.as_view(), name='signUp'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', MyPasswordChangeView.as_view(), name='password_change'),
]