from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
from django.contrib.auth.decorators import login_required
from community.models import BlogPost
from tools.models import MealPlanner, WorkoutPlanner


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully.")
            return redirect("login")
        else:
            # Form is invalid — render the form again with errors
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})



@login_required
def profile(request):
    posts = BlogPost.objects.filter(author=request.user)
    meals = MealPlanner.objects.filter(user=request.user).order_by('-date')[:7]
    workouts = WorkoutPlanner.objects.filter(user=request.user).order_by('-date')[:7]

    return render(request, 'users/profile.html', {
        'posts': posts,
        'meals': meals,
        'workouts': workouts,
    })


class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm
    template_name = 'users/login.html'




def logout(request):
    return render(request,'mainpage/about.html')