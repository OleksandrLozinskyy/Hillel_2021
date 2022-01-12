from django.contrib.auth import get_user_model, models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.forms import forms
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from users.forms import LoginForm, UserCreationForm
from .models import Profile, User
from core.models import Post
# Create your views here.

User = get_user_model()

class LoginView(LoginView):
    model = User
    form_class = LoginForm
    template_name = "../registration/login.html"

class UserRegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "../registration/register.html"
    success_url = reverse_lazy('users:login')


class ProfileView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    edirect_field_name = reverse_lazy('users:profile')
    model = Profile
    context_object_name = 'user_data'
    template_name = "../users/profile.html"

    @property
    def username(self):
        username = self.request.user
        return username


    def get_object(self, queryset=None):
        profile = Profile.objects.get(user=self.request.user.pk)
        profile.posts = Post.objects.filter(user_id=self.username)
        profile.user = User.objects.get(id=self.request.user.id)
        profile.sex = 'Male' if profile.sex else 'Female'
        print(profile)
        return profile 

    # def get_context_data(self, queryset=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['posts'] = Post.objects.filter(user_id=self.username)
    #     context['user'] = User.objects.get(id=self.request.user.id)
    #     print(context)
    #     return context 

""" class LoginView(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        
        user = authenticate(request, username=username, password=password)
        if user == None:
            attempt = request.session.get("attempt") or 0 """
            