from django.urls import path
from django.views.decorators.cache import cache_page

from blog.views import ArticleListView
from catalog.apps import CatalogConfig
from catalog.views import ContactsView, HomeView, ProductDetailView, ProductListView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, ProductsByCategoryView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path("catalog/", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("", ProductListView.as_view(), name="product_list"),
    path("product/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path("product/new/", ProductCreateView.as_view(), name="product_create"),
    path("product/update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("product/delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/<str:category_name>/', ProductsByCategoryView.as_view(), name='product_category'),
    ]
