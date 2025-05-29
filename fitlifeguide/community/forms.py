from django import forms
from .models import BlogPost, Thread, BlogComment, ForumComment, Forum


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
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-light',
                'placeholder': 'Enter a descriptive title for your thread'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control bg-dark text-light',
                'rows': 8,
                'placeholder': 'Write your thread content here...'
            })
        }


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write your comment here...'
            })
        }


class ForumCommentForm(forms.ModelForm):
    parent = forms.ModelChoiceField(
        queryset=ForumComment.objects.all(),
        required=False,
        widget=forms.HiddenInput()
    )

    class Meta:
        model = ForumComment
        fields = ['content', 'parent']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write your reply here...'
            })
        }
