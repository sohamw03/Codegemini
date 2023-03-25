from django.shortcuts import render, HttpResponse

# Create your views here.
def blogHome(request):
    return HttpResponse("Blog home, to keep all the blogposts.")

def blogPost(request, slug):
    return HttpResponse(f"Blog post page here. with slug : {slug}")