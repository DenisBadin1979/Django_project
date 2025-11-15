from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, DeleteView

import catalog
from catalog.forms import ProductForm, ProductModeratorForm
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

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy ('catalog:product_list')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy ('catalog:product_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm
        raise PermissionDenied

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy ('catalog:product_list')

    def get_queryset(self):
        """Ограничиваем queryset только теми продуктами, которые пользователь может удалить"""
        user = self.request.user
        queryset = super().get_queryset()

        # Если пользователь имеет право удалять любые продукты
        if user.has_perm('catalog.delete_product'):
            return queryset

        # Иначе показываем только свои продукты
        if hasattr(Product, 'owner'):
            return queryset.filter(owner=user)

        # Если нет поля owner и нет прав - пустой queryset
        return queryset.none()
