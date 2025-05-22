from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
from django.contrib.auth.decorators import login_required
from community.models import BlogPost
from tools.models import MealPlanner, WorkoutPlanner

from .forms import OTPForm
from django.urls import reverse
from django.core.mail import send_mail
import random
from django.conf import settings

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string









def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully.")

            # Render HTML email content
            subject = 'Welcome to FitLifeGuide!'
            from_email = settings.EMAIL_HOST_USER
            to_email = user.email
            context = {'username': user.username}

            html_content = render_to_string('users/welcome_email.html', context)
            text_content = f"Hi {user.username},\n\nThanks for registering at FitLifeGuide."

            # Create and send email
            email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
            email.attach_alternative(html_content, "text/html")
            email.send()

            return redirect("login")
        else:
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





from django.shortcuts import redirect
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView
import random

class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm
    template_name = 'users/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')  # Replace 'home' with your actual homepage URL name
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.get_user()
        self.request.session['pre_2fa_user_id'] = user.id

        # Generate and send OTP
        otp = random.randint(100000, 999999)
        self.request.session['otp'] = str(otp)

        send_mail(
            'Your FitLifeGuide OTP',
            f'Your OTP is: {otp}',
            'noreply@fitlifeguide.com',
            [user.email],
            fail_silently=False,
        )

        return redirect('verify_otp')  # Make sure this URL is defined in your urls.py





def logout(request):
    return render(request,'mainpage/about.html')
    

def verify_otp(request):
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            input_otp = form.cleaned_data['otp']
            real_otp = request.session.get('otp')

            if input_otp == real_otp:
                user_id = request.session.get('pre_2fa_user_id')
                user = User.objects.get(id=user_id)
                login(request, user)
                
                # Clear OTP-related session data
                del request.session['otp']
                del request.session['pre_2fa_user_id']
                
                return redirect('home')  # or your post-login page
            else:
                form.add_error('otp', 'Invalid OTP')
    else:
        form = OTPForm()

    return render(request, 'users/verify_otp.html', {'form': form})
