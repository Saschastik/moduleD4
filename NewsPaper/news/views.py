from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.core.paginator import Paginator
from django.views import View
from .models import *
from .filters import NewsFilter
from .forms import PostForm

# Create your views here.

class PostList(ListView):
    model = Post
    template_name = 'news.html' 
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')
    paginate_by = 2
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_premium'] = not self.request.user.groups.filter(name='authors').exists()
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'details_news.html' 
    context_object_name = 'new_s'
    queryset = Post.objects.filter(type='NW')

class PostCreateView(CreateView):
    template_name = 'add_post.html'
    form_class = PostForm


class PostUpdateView(UpdateView):
    template_name = 'post_update.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id_id = self.kwargs.get('pk')
        return Post.objects.get(pk=id_id)


class PostDeleteView(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


class SearchList(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())

        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return super().get(request, *args, **kwargs)

