from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Contact
from blog.models import Post


# HTML PAGES
def home(request):
    allPosts = Post.objects.all()[:3]
    context = {"allPosts": allPosts}
    return render(request, "home/home.html", context)


def contact(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        content = request.POST.get("content", "")
        contact = Contact(name=name, email=email, phone=phone, content=content)
        contact.save()
        thank = True
    return render(request, "home/contact.html", {"thank": thank})


def about(request):
    return render(request, "home/about.html")


def search(request):
    query = request.GET["query"]
    allPosts = Post.objects.filter(title__icontains=query).union(
        Post.objects.filter(author__icontains=query),
        Post.objects.filter(content__icontains=query),
        Post.objects.filter(timestamp__icontains=query),
    )
    context = {"allPosts": allPosts, "query": query}
    return render(request, "home/search.html", context)


# AUTHENTICATION APIs
def handleSignup(request):
    if request.method == "POST":
        # Get the post parameters
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        rpassword = request.POST["rpassword"]
        # Check for erroneous inputs
        if name.isalnum() != True:
            messages.error(request, "Username should only contain letters and numbers!")
            return redirect("home")
        if len(name) > 15:
            messages.error(request, "Username must be under 15 characters!")
            return redirect("home")
        if password != rpassword:
            messages.error(request, "Password do not match!")
            return redirect("home")

        # Create the user
        myuser = User.objects.create_user(
            username=name, email=email, password=rpassword
        )
        myuser.save()
        messages.success(request, "Your iCoder account has been succesfully created!")
        return redirect("home")
    else:
        return HttpResponse('<h1 style="text-align:center">404 - Not Found</h1>')


def handleLogin(request):
    if request.method == "POST":
        name = request.POST["name"]
        password = request.POST["password"]
        user = authenticate(username=name, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Succesfully logged in")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")
    return HttpResponse('<h1 style="text-align:center">404 - Not Found</h1>')


def handleLogout(request):
    logout(request)
    messages.success(request, "Logged out!")
    return redirect("home")
