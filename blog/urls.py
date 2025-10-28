from django.urls import path

from blog.apps import BlogConfig
from blog.views import home_blog, ArticleListView

app_name = BlogConfig.name

urlpatterns = [
    path("base/", home_blog, name="base"),
    path("", ArticleListView.as_view(), name="article_list")
]