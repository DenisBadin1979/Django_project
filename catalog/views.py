from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView, TemplateView

from catalog.models import Product


class HomeView(TemplateView):
    template_name = "catalog/base.html"


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
