from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Forum, Thread
from .forms import BlogPostForm, ThreadForm


def posts_view(request):
    posts = BlogPost.objects.filter(published=True).select_related('author')
    return render(request, 'community/posts.html', {'posts': posts})


def post_detail_view(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    return render(request, 'community/post_detail.html', {'post': post})


@login_required
def create_post_view(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts')
    else:
        form = BlogPostForm()
    return render(request, 'community/create_post.html', {'form': form})


def forum_list(request):
    forums = Forum.objects.all()
    return render(request, 'community/forum_list.html', {'forums': forums})


def forum_threads(request, slug):
    forum = get_object_or_404(Forum, slug=slug)
    threads = forum.threads.order_by('-created_at')
    return render(request, 'community/forum_threads.html', {'forum': forum, 'threads': threads})


@login_required
def thread_create(request, slug):
    forum = get_object_or_404(Forum, slug=slug)
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.forum = forum
            thread.author = request.user
            thread.save()
            return redirect('thread_detail', slug=thread.slug)
    else:
        form = ThreadForm()
    return render(request, 'community/thread_create.html', {'form': form, 'forum': forum})


def thread_detail(request, slug):
    thread = get_object_or_404(Thread, slug=slug)
    return render(request, 'community/thread_detail.html', {'thread': thread})
