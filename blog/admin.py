from django.contrib import admin
from .models import Post, Comment


# Register your models here.
admin.site.register(Comment)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    class Media:
        js = ("tinyInject.js",)
