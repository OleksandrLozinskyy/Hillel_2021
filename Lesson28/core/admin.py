from django.contrib import admin
from .models import Post, Likes

# Register your models here.

class Likes(admin.TabularInline):
    model = Likes


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'user_id', 'views')
    inlines = [
        Likes,
    ]
    ordering = ('id',)


