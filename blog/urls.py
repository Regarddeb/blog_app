from django.urls import path
from .views import *

urlpatterns = [
    path('my_blogs', BlogPostListView.as_view(), name='my_blogs'),
    path('create_blog_form', BlogPostCreateView.as_view(), name='create_blog_form'),
    path('edit_blog_form/<int:id>/', BlogPostEditView.as_view(), name='edit_blog_form'),
    path('show_blog/<int:id>/', BlogShowView.as_view(), name='show_blog'),

    # apis
    path('api/blog/all', BlogPostView.as_view(), name='api/blog'),
    path('api/blog/create', BlogPostView.as_view(), name='api/blog/create'),
    path('api/blog/delete/<int:id>', BlogPostView.as_view(), name='api/blog/delete'),
    path('api/blog/update/<int:id>', BlogPostView.as_view(), name='api/blog/update'),
]