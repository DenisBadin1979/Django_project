from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_from_prod_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()

    key = "product_list"
    prods = cache.get(key)
    if prods is not None:
        return prods
    prods = Product.objects.all()
    cache.set(key, prods)
    return prods


def get_products_by_category(request, category_name):
    return Product.objects.filter(category__name=category_name).selec_rlated('category')
