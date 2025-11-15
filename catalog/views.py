from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, DeleteView

import catalog
from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product, Category
from catalog.services import get_from_prod_cache, get_products_by_category


class HomeView(TemplateView):
    template_name = "catalog/base.html"


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"



class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        return get_from_prod_cache()


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем все категории в контекст для меню
        context['all_categories'] = Category.objects.all()
        return context

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


class CategoryListView(ListView):
    """CBV для отображения всех категорий"""
    model = Category
    template_name = 'catalog/category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all()


class ProductsByCategoryView(ListView):
    """CBV для отображения продуктов по категории"""
    template_name = 'catalog/product_category.html'
    context_object_name = 'producat'
    paginate_by = 12

    def get_queryset(self):
        # Получаем категорию по имени из URL
        self.category = get_object_or_404(Category, name=self.kwargs['category_name'])
        # Возвращаем продукты этой категории
        return Product.objects.filter(category=self.category).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['category_name'] = self.category.name
        return context