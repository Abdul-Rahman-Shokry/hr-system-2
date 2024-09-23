from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import signUpForm
from django.contrib.auth.views import PasswordChangeView
# Create your views here.

class signUpView(CreateView):
    form_class = signUpForm
    template_name = 'registration\signUp.html'
    success_url = reverse_lazy('branches')

class MyPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('branches')
    