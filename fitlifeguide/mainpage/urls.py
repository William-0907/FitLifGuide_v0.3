from .views import home,about,contact,welcome
from django.urls import path

urlpatterns = [
    path('home/', home, name='home'),
    path('', welcome, name='welcome'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]