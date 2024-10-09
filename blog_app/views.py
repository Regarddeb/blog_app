from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from blog.models import BlogPost


class HomeView(ListView):
    model = BlogPost
    template_name = 'home.html'
    context_object_name = 'posts'

class AppLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('')

class AppLogoutView(LogoutView):
    next_page = 'home'