from django.shortcuts import render, HttpResponse, redirect
from .models import Post, Comment
from django.contrib import messages
import django.utils

# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {"allPosts": allPosts}
    return render(request, "blog/bloghome.html", context)


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = Comment.objects.filter(post=post)
    context = {"post": post, "comments": comments}
    return render(request, "blog/blogpost.html", context)

# APIs
def postComment(request):
    if request.method == "POST":
        data = request.POST.get("comment")
        user = request.user
        print(user, type(user))
        postsno = request.POST.get("postid")
        post = Post.objects.get(sno=postsno)
        if not request.user.is_anonymous:
            comments = Comment(data=data, user=user, post=post)
            comments.save()
            messages.success(request, "Your comment has been posted succesfully")
        else:
            messages.warning(request, "Please login or signup to post comments")
    return redirect(f"/blog/{post.slug}")