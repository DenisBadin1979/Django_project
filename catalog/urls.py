from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contact_post, contacts, home

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("contact_post/", contact_post, name="contact_post"),
]
