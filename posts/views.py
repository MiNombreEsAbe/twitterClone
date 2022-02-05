from http.client import HTTPResponse
from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import Postform

# Create your views here.


def index(req):
    # If method = post
    if req.method == 'POST':
        form = Postform(req.POST, req.FILES)
        print(req.POST, req.FILES)

        # If form = valid, save
        if form.is_valid():
            form.save()

            # Redirect to home
            return HttpResponseRedirect('/')

        # Else, give error
        return HttpResponseRedirect(form.errors.as_json())

    # Get all posts
    posts = Post.objects.all().order_by('-createdAt')[:20]

    # Show the page
    return render(req, 'posts.html', {'posts': posts})


def delete(req, post_id):
    # Find post based on the post id
    post = Post.objects.get(id=post_id)

    # Delete the post
    post.delete()

    # Redirect to home
    return HttpResponseRedirect('/')


def addLike(req, post_id):
    # Find the post based on the id
    post = Post.objects.get(id=post_id)

    # Increment the likes of the post by 1
    post.likes += 1

    # Save the post
    post.save()

    # Redirect the user to the home page
    return HttpResponseRedirect('/')
