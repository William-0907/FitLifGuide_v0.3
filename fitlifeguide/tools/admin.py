from django.contrib import admin
from .models import MealPlan, MealPlanner, WorkoutPlan, WorkoutPlanner

admin.site.register(MealPlan)
admin.site.register(MealPlanner)
admin.site.register(WorkoutPlan)
admin.site.register(WorkoutPlanner)

