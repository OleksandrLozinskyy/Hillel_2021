from django.db import models
from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    model = Post
    context_object_name = 'object_list'
    qs = []
    posts = Post.objects.all().order_by('-created_at')[:10]
    for post in posts:
        qs.append([post, post.like_set.filter(status=True).count, post.like_set.filter(status=False).count])
    queryset = qs
    template_name = "../core/posts.html"

class PostView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = "../core/post.html"    

    def get_object(self, queryset=None):
        return Post.objects.get(id=self.kwargs.get('pk'))