# Generated by Django 5.2.1 on 2025-05-29 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_status_profile_status_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cover_image',
            field=models.ImageField(default='default-cover.jpg', upload_to='cover_pics'),
        ),
    ]
