from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, get_object_or_404

from blog.models import BlogPost
from .serializers.BlogRequestSerializer import *

class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blogs/my_blogs.html'
    context_object_name = 'my_posts'

    def get_queryset(self):
        return BlogPost.objects.filter(author=self.request.user, is_deleted=False)


class BlogPostCreateView(TemplateView):
    template_name = 'blogs/create_blog_form.html'
    
    
class BlogPostEditView(TemplateView):
    template_name = 'blogs/edit_blog_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = self.kwargs.get('id')
        context['post'] = get_object_or_404(BlogPost, id=post_id)
        return context
    
    
class BlogPostView(LoginRequiredMixin, APIView):

    def post(self, request):
        request_serialized = BlogRequestSerializer(data=request.data)
        if not request_serialized.is_valid():
            return Response(request_serialized.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        try:
            data = request_serialized.validated_data
            BlogPost.objects.create(
                title=data['title'].title(),
                content=data['content'],
                author=request.user
            )
            return Response({}, status=status.HTTP_201_CREATED)
        except Exception as e:
            error_message = {
                'message': str(e)
            }
            return Response(error_message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self, request, id):
        request_serialized = BlogRequestSerializer(data=request.data)
        if not request_serialized.is_valid():
            return Response(request_serialized.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        try:
            data = request_serialized.validated_data
            blog = get_object_or_404(BlogPost, id=id)
            
            blog.title = data['title']
            blog.content = data['content']
            blog.save()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            error_message = {
                'message': str(e)
            }
            return Response(error_message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return 

    def delete(self, request, id):
        blog = get_object_or_404(BlogPost, id=id)
        blog.soft_delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)