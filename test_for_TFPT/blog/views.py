from django.shortcuts import render
from .models import *
from django.views.generic import DetailView, ListView


# def list_of_posts(request):
#     posts = Post.objects.filter(status='published')
#     return render(request, 'blog/index.html', {'posts': posts})


class ListPosts(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 10
    ordering = ['-time_of_creation']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class GetPost(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'


class PostsbyTag(ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = 5
    context_object_name = 'posts'
    ordering = ['-time_of_creation']

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список постов за тегом ' + str(Tag.objects.get(slug=self.kwargs['slug']))
        return context
