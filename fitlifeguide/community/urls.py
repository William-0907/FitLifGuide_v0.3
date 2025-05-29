from django.urls import path
from . import views

urlpatterns = [
    # Blog URLs
    path('posts/', views.posts_view, name='posts'),
    path('posts/create/', views.create_post_view, name='create_post'),
    path('posts/<slug:slug>/', views.post_detail_view, name='post_detail'),
    path('posts/<slug:slug>/delete/', views.delete_post, name='delete_post'),
    path('posts/<slug:slug>/like/', views.like_post, name='like_post'),
    
    # Forum URLs
    path('forum/', views.forum_list, name='forum_list'),
    path('forum/<slug:slug>/', views.forum_threads, name='forum_threads'),
    path('forum/<slug:slug>/create/', views.thread_create, name='thread_create'),
    path('thread/<slug:slug>/', views.thread_detail, name='thread_detail'),
    path('thread/<slug:slug>/delete/', views.delete_thread, name='delete_thread'),
    path('thread/<slug:slug>/like/', views.like_thread, name='like_thread'),
    path('forum-post/<int:post_id>/delete/', views.delete_forum_post, name='delete_forum_post'),
    path('forum-post/<int:post_id>/like/', views.like_forum_post, name='like_forum_post'),
    
    # Comment URLs
    path('forum-post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('forum-comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('forum-comment/<int:comment_id>/like/', views.like_comment, name='like_comment'),
]
