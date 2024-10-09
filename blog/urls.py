from django.urls import path

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blogpost_list'),
]