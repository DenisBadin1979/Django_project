from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from blog.models import Article


#
def home_blog(request):
    return render(request, "base_blog.html")


class ArticleListView(ListView):
    model = Article
    template_name = "blog/article_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Article.objects.filter(publication_attribute=True).order_by("-create_at")


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/article_detail.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        # Увеличение счетчика просмотров
        obj = super().get_object(queryset)
        obj.numbers_views += 1
        obj.save()
        return obj


class ArticleCreateView(CreateView):
    model = Article
    template_name = "blog/article_form.html"
    fields = ["heading", "content", "preview", "publication_attribute"]
    success_url = reverse_lazy("blog:article_list")


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = "blog/article_form.html"
    fields = ["heading", "content", "preview", "publication_attribute"]

    def get_success_url(self):
        # Перенаправление на просмотр этой статьи после редактирования
        return reverse_lazy("blog:article_detail", kwargs={"pk": self.object.pk})


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "blog/article_delete.html"
    success_url = reverse_lazy("blog:article_list")
