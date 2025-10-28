from django.urls import path

from blog.views import ArticleListView
from catalog.apps import CatalogConfig
from catalog.views import home, ProductListView, ProductDetailView, ContactsView

app_name = CatalogConfig.name

urlpatterns = [
    path("base/", home, name="base"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path('', ProductListView.as_view(), name="product_list"),
    path("", ArticleListView.as_view(), name="article_list"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product_detail"),
]
