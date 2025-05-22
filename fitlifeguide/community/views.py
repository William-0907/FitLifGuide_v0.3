from django.shortcuts import render,redirect
from .models import BlogPost
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


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