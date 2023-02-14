from django.shortcuts import render
from django.views.generic import ListView,DetailView
from.models import Post
from django.conf import settings
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy

def error_404_view(request, exception):
    return render(request, "error_page.html")

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'summary' ,'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'summary' ,'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')