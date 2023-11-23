from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def main(request):
    posts = Post.objects.all()
    for post in posts:
        print(post.image)
    return render(request, 'main.html', {'posts':posts})

def detail(request, pk):
    post = Post.objects.get(id=int(pk))
    return render(request, 'singlepost.html', {'post':post})