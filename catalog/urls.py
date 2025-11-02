from django.urls import path

from blog.views import ArticleListView
from catalog.apps import CatalogConfig
from catalog.views import ContactsView, HomeView, ProductDetailView, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path("catalog/", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("", ProductListView.as_view(), name="product_list"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
]
