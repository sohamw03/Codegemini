from django.shortcuts import render, HttpResponse
from .models import Contact

# Create your views here.
def home(request):
    return render(request, "home/home.html")


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
