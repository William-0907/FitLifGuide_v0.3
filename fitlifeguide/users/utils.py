# utils.py
from .models import EmailOTP
from django.core.mail import send_mail
import random

def generate_otp(user):
    code = f"{random.randint(100000, 999999)}"
    EmailOTP.objects.update_or_create(user=user, defaults={'code': code})
    send_mail(
        'Your Login OTP',
        f'Your OTP code is: {code}',
        'your_email@example.com',
        [user.email],
        fail_silently=False,
    )
