from django.views.generic import ListView
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
        
