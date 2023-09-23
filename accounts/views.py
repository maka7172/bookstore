from django.shortcuts import render
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCrationForm
from django.urls import reverse_lazy


# class SignUpView(generic.CreateView) :
#     form_class = CustomUserCrationForm 
#     template_name = 'signup.html'
#     success_url = reverse_lazy('login')


