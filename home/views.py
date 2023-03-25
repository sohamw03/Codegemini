from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Home page")

def contact(request):
    return HttpResponse("Contact page")

def about(request):
    return HttpResponse("About page")