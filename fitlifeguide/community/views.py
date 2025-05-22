from django.shortcuts import render,redirect
from .models import BlogPost,Forum
from .forms import BlogPostForm
from django.shortcuts import render, get_object_or_404
from .models import Forum, Thread
from .forms import ThreadForm  # We'll create this form next
from django.contrib.auth.decorators import login_required
from .forms import ThreadCreateForm


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


@login_required
def thread_create(request):
    if request.method == 'POST':
        form = ThreadCreateForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.author = request.user
            thread.save()
            # Redirect to the newly created thread page (adjust the URL name as needed)
            return redirect('thread_detail', slug=thread.slug)
    else:
        form = ThreadCreateForm()

    return render(request, 'community/thread_create.html', {'form': form})




def forum_threads(request, slug):
    forum = get_object_or_404(Forum, slug=slug)
    threads = forum.threads.all()  # Using related_name='threads' in Thread model's FK to Forum

    context = {
        'forum': forum,
        'threads': threads,
    }
    return render(request, 'community/forum_threads.html', context)

def thread_detail(request, slug):
    thread = get_object_or_404(Thread, slug=slug)
    return render(request, 'community/thread_detail.html', {'thread': thread})



def forum_threads(request, slug):
    forum = get_object_or_404(Forum, slug=slug)
    threads = forum.threads.order_by('-created_at')  # Assuming related name `threads`
    return render(request, 'community/forum_threads.html', {'forum': forum, 'threads': threads})

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
