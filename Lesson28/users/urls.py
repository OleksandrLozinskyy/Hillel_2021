from django.urls import path
from .views import ProfileView, UserRegisterView

app_name='users'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('register/', UserRegisterView.as_view(), name='signup')
]