from django.shortcuts import render, HttpResponse, redirect
from .models import Post, Comment
from django.contrib import messages
import django.utils
from blog.templatetags import extras


# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {"allPosts": allPosts}
    print(allPosts)
    return render(request, "blog/bloghome.html", context)


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = Comment.objects.filter(post=post, parent=None)
    replies = Comment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    context = {"post": post, "comments": comments, "replyDict": replyDict}
    return render(request, "blog/blogpost.html", context)


# APIs
def postComment(request):
    if request.method == "POST":
        data = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get("parentSno")
        if not request.user.is_anonymous:
            if parentSno == "":
                comments = Comment(data=data, user=user, post=post)
                messages.success(request, "Your comment has been posted succesfully")
            else:
                parent = Comment.objects.get(sno=parentSno)
                comments = Comment(data=data, user=user, post=post, parent=parent)
                messages.success(request, "Your reply has been posted succesfully")
            comments.save()
        else:
            messages.warning(request, "Please login or signup to access our community")
    return redirect(f"/blog/{post.slug}")
