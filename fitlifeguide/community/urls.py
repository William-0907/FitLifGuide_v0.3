from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts_view, name='posts'),
    path('posts/<slug:slug>/', views.post_detail_view, name='post_detail'),
    path('posts/create/', views.create_post_view, name='create_post'),
]
