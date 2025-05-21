from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# -----------------------------
# Weekday Choices Enum
# -----------------------------

class WeekDay(models.TextChoices):
    MONDAY = 'Mon', _('Monday')
    TUESDAY = 'Tue', _('Tuesday')
    WEDNESDAY = 'Wed', _('Wednesday')
    THURSDAY = 'Thu', _('Thursday')
    FRIDAY = 'Fri', _('Friday')
    SATURDAY = 'Sat', _('Saturday')
    SUNDAY = 'Sun', _('Sunday')

# -----------------------------
# MEAL PLAN & PLANNER
# -----------------------------

class MealPlan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='meal_plan')
    name = models.CharField(max_length=100, default='My Meal Plan')
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Meal Plan"

class MealPlanner(models.Model):
    MEAL_TYPE_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]

    STATUS_CHOICES = [
        ('planned', 'Planned'),
        ('eaten', 'Eaten'),
        ('skipped', 'Skipped'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meals')
    meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE, related_name='entries')
    date = models.DateField()
    week_start = models.DateField(help_text="Start of the week")
    day_of_week = models.CharField(max_length=3, choices=WeekDay.choices)
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPE_CHOICES)
    food_items = models.TextField()
    calories = models.PositiveIntegerField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='planned')
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ('user', 'date', 'meal_type')
        ordering = ['-date', 'meal_type']

    def __str__(self):
        return f"{self.user.username} - {self.meal_type} on {self.date}"

# -----------------------------
# WORKOUT PLAN & PLANNER
# -----------------------------

class WorkoutPlan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='workout_plan')
    name = models.CharField(max_length=100, default='My Workout Plan')
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Workout Plan"

class WorkoutPlanner(models.Model):
    STATUS_CHOICES = [
        ('planned', 'Planned'),
        ('completed', 'Completed'),
        ('missed', 'Missed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='entries')
    date = models.DateField()
    week_start = models.DateField(help_text="Start of the week")
    day_of_week = models.CharField(max_length=3, choices=WeekDay.choices)
    title = models.CharField(max_length=200)
    exercises = models.TextField()
    duration_minutes = models.PositiveIntegerField(null=True, blank=True)
    goal = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='planned')
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.user.username} - {self.title} on {self.date}"

