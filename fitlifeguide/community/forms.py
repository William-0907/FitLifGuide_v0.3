from django import forms
from .models import BlogPost,Thread, Forum


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ThreadCreateForm(forms.ModelForm):
    forum = forms.ModelChoiceField(queryset=Forum.objects.all(), empty_label="Select a forum")

    class Meta:
        model = Thread
        fields = ['forum', 'title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Thread Title'}),
            'forum': forms.Select(attrs={'class': 'form-select'}),
        }


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'content']  # Adjust if you have other fields
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
