from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.blogHome, name='blogHome'),
    path("<slug:slug>", views.blogPost, name='post_detail'),
]
