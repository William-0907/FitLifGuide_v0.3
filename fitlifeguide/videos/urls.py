from . import views
from django.urls import path


urlpatterns = [
    path('videos/', views.videos_views, name='videos'),
]