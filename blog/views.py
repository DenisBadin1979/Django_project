from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Article


def home_blog(request):
    return render(request, "base.html")

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'post'
