from django.urls import path
from .views import *

urlpatterns = [
    path('', ListPosts.as_view(), name='home'),
    path('post/<str:slug>/', GetPost.as_view(), name='getpost'),
    path('tag/<str:slug>/', PostsbyTag.as_view(), name='tag'),
]