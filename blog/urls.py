from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.blogHome, name='blogHome'),
    path("postcomment", views.postComment, name='postComment'),
    path("<slug:slug>", views.blogPost, name='post_detail'),
]
