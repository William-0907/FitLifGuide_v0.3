from django import forms
from .models import MealPlanner, WorkoutPlan, WorkoutPlanner

class MealPlannerForm(forms.ModelForm):
    class Meta:
        model = MealPlanner
        fields = ['food_items', 'calories', 'notes']
        widgets = {
            'food_items': forms.Textarea(attrs={
                'rows': 3, 
                'placeholder': 'Enter food items, one per line',
                'class': 'bg-dark text-light border-secondary'
            }),
            'notes': forms.Textarea(attrs={
                'rows': 2, 
                'placeholder': 'Any additional notes (optional)',
                'class': 'bg-dark text-light border-secondary'
            }),
            'calories': forms.NumberInput(attrs={
                'placeholder': 'Enter calories (optional)',
                'class': 'bg-dark text-light border-secondary'
            })
        }

class WorkoutPlanForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'bg-dark text-light border-secondary'
        })
    )

    class Meta:
        model = WorkoutPlanner
        fields = ['date', 'title', 'exercises', 'duration_minutes', 'goal', 'notes']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter workout title',
                'class': 'bg-dark text-light border-secondary'
            }),
            'exercises': forms.Textarea(attrs={
                'rows': 4, 
                'placeholder': 'List your exercises here (e.g., 3x10 Push-ups, 4x12 Squats...)',
                'class': 'bg-dark text-light border-secondary'
            }),
            'duration_minutes': forms.NumberInput(attrs={
                'placeholder': 'Duration in minutes',
                'class': 'bg-dark text-light border-secondary'
            }),
            'goal': forms.TextInput(attrs={
                'placeholder': 'What do you want to achieve? (e.g., Build strength, Improve cardio)',
                'class': 'bg-dark text-light border-secondary'
            }),
            'notes': forms.Textarea(attrs={
                'rows': 3, 
                'placeholder': 'Additional notes, reminders, or instructions...',
                'class': 'bg-dark text-light border-secondary'
            }),
        } 