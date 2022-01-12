from django.urls import path

from core.models import Post
from .views import PostListView, PostView, PostCreate, PostUpdate, PostDelete

app_name='posts'

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('post/<int:pk>/', PostView.as_view(), name='preview'),
    path('add_post/', PostCreate.as_view(), name='add_post'),
    path('update_post/<int:pk>/', PostUpdate.as_view(), name='update_post'),
    path('delete_post/<int:pk>/', PostDelete.as_view(), name='delete_post'),
]