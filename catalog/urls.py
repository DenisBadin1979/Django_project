from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contact_post, contacts, home, product_list, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("contact_post/", contact_post, name="contact_post"),
    path('', product_list, name="product_list"),
    path('product/<int:pk>/', product_detail, name="product_detail"),
]
