from django.shortcuts import render, redirect

def home(request):
    return render(request, 'mainpage/home.html')

def welcome(request):
    if request.user.is_authenticated:
        return redirect('home')  # or use the name of the URL pattern
    return render(request, 'mainpage/landingpage.html')

def about(request):
    return render(request, 'mainpage/about.html')

def contact(request):
    return render(request, 'mainpage/contact.html')
