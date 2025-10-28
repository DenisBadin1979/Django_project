from django.urls import path

from blog.apps import BlogConfig
from blog.views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, \
    home_blog

app_name = BlogConfig.name

urlpatterns = [
    # path("base/", home_blog, name="base"),
    path("", ArticleListView.as_view(), name="article_list"),
    path('post/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('post/create/', ArticleCreateView.as_view(), name='article_create'),
    path('post/<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('post/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
]