from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from blog.views import ArticleListView
from catalog.apps import CatalogConfig
from catalog.views import ContactsView, HomeView, ProductDetailView, ProductListView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView
from users.views import RegisterView

app_name = "users"

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),

    path("logout/", LogoutView.as_view(next_page="catalog:product_list"), name="logout"),

    path("register/", RegisterView.as_view(), name="register"),
]