from django.http.response import Http404
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostForm
from django.contrib.auth import get_user_model



User = get_user_model()
class PostListView(ListView):
    model = Post
    context_object_name = 'object_list'
    template_name = "../core/posts.html"
    ordering = ['-created_at']

    def get_queryset(self):
        qs = super(PostListView, self).get_queryset()
        for post in qs:
            post.likes = post.likes_set.filter(status=True).count() 
            post.dislikes = post.likes_set.filter(status=False).count()
        return qs

class PostView(DetailView):
    model = Post
    context_object_name = 'post_data'
    template_name = "../core/post.html" 
    
    def changeViewsCount(self):
        post = Post.objects.get(id=self.kwargs.get('pk'))
        post.views += 1
        post.save()
        

    def get_object(self, queryset=None): 
        self.changeViewsCount()
        post = Post.objects.get(id=self.kwargs.get('pk'))
        post.likes = post.likes_set.filter(status=True).count() 
        post.dislikes = post.likes_set.filter(status=False).count()    
        return post


class PostDelete(LoginRequiredMixin, DeleteView):
        model = Post
        template_name = '../core/delete_post.html'
        context_object_name = 'post_data'
        success_url = reverse_lazy('posts:list')

        def get_object(self, queryset=None):
            obj = super(PostDelete, self).get_object(queryset)
            if obj.user_id != self.request.user:
                raise Http404('You are not own this post')
            return obj


class PostCreate(LoginRequiredMixin, CreateView):

        model = Post
        template_name = "../core/add_post.html"
        form_class = PostForm
        login_url = 'login'
        permission_denied_message = 'Are you fucking haker?' 	
        raise_exception = False 


        def form_valid(self, form):
            user = self.request.user
            form.instance.user_id = user
            return super().form_valid(form)
        

class PostUpdate(LoginRequiredMixin, UpdateView):
        model = Post
        context_object_name = 'post_data'
        template_name = "../core/update_post.html"
        form_class = PostForm

        def get_object(self, queryset=None): 
            obj = super(PostUpdate, self).get_object(queryset)
            if obj.user_id != self.request.user:
                raise Http404('You are not own this post')
            return obj
