from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=13)
    content = models.TextField()
    timestamp = models.DateTimeField(blank=True)
    slug = models.SlugField(null=True, max_length=255)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
    
    
