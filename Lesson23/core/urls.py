from django.urls import path
from .views import PostListView, PostView


urlpatterns = [
    path('', PostListView.as_view()),
    path('post/<int:pk>/', PostView.as_view())
]
