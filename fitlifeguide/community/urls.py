from django.urls import path
from . import views

urlpatterns = [
    path('posts/create/', views.create_post_view, name='create_post'),
    path('posts/', views.posts_view, name='posts'),
    path('posts/<slug:slug>/', views.post_detail_view, name='post_detail'),
    path('forums/', views.forum_list, name='forum_list'),
    path('forums/<slug:slug>/', views.forum_threads, name='forum_threads'),
    path('threads/create/', views.thread_create, name='thread_create'),
    path('forums/<slug:slug>/new-thread/', views.thread_create, name='new_thread'),  # Create a new thread
    path('threads/<slug:slug>/', views.thread_detail, name='thread_detail'),

]

