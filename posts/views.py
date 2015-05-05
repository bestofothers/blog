from django.shortcuts import render

from .models import Post, Comment, Category, Reply
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'posts'
    model = Post
    queryset=Post.objects.all().order_by('-created_at')
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class PostView(generic.DetailView):
    template_name = 'posts/more.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class CategoriesView(generic.ListView):
    template_name = 'posts/base.html'
    context_object_name = 'categories'
    model = Category

class CategoryView(generic.ListView):
    template_name = 'posts/category.html'
    model = Post
    context_object_name = 'category'