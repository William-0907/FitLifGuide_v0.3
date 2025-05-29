from . import views
from django.urls import path


urlpatterns = [
    path('videos/', views.videos_views, name='videos'),
    path('video/<str:video_id>/track/', views.track_video_click, name='track_video'),
]