from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import BlogPost


class HomeView(ListView):
    model = BlogPost
    template_name = 'home.html'
    context_object_name = 'posts'