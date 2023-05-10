from django.contrib import admin
from .models import Post


# Add user to list view
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')


# Register your models here.
admin.site.register(Post, PostAdmin)
