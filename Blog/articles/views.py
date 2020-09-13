from django.shortcuts import render, get_objet_or_404
from .models import Post
# Create your views here.

def post_list(request):
    posts = Post.published.all()
    return render(request, 'articles/list.html', {posts:'posts'})


def post_detail(request, year, month, day, post):
    post = get_bject_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)

    return render(request, 'articles/detail.html', {post:'post'})



