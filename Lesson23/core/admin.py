from django.contrib import admin
from .models import Post, Like
# Register your models here.


class Like(admin.TabularInline):
    model = Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'user_id')
    inlines = [
        Like,
    ]
    ordering = ('id',)
