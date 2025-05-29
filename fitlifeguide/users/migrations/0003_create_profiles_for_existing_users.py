from django.db import migrations

def create_profiles_for_existing_users(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Profile = apps.get_model('users', 'Profile')
    
    for user in User.objects.all():
        Profile.objects.get_or_create(user=user)

def reverse_func(apps, schema_editor):
    pass

class Migration(migrations.Migration):
    dependencies = [
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.RunPython(create_profiles_for_existing_users, reverse_func),
    ] 