from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from catalog.models import Product


def home(request):
    return render(request, "base.html")

class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


# def contacts(request):
#     return render(request, "contacts.html")





class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product


