from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required

# from django.http import HttpResponse


# create  views
def posts_list(request):
    posts = Post.objects.all().order_by("-date")
    return render(request, "posts/posts.html", {"posts": posts})


def post_page(request, slug):
    # return HttpResponse(slug)
    post = Post.objects.get(slug=slug)
    return render(request, "posts/post_page.html", {"post": post})


@login_required(login_url="/users/login")
def post_new(request):
    return render(request, "posts/post_new.html")