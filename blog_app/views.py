from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from blog.models import BlogPost


class HomeView(ListView):
    model = BlogPost
    template_name = 'home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPost.objects.filter(is_deleted=False)


class AppLoginView(LoginView):
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse_lazy('home')


class AppLogoutView(LogoutView):
    next_page = 'home'


class RegisterView(CreateView):
    model = User
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
