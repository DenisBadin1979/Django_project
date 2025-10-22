from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "contacts.html")


def contact_post(request):
    if request.method == "POST":
        # Получение данных из формы
        name = request.POST.get("name")
        message = request.POST.get("message")
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "contacts.html")

def product_list(request):
    prod_list = Product.objects.all()
    context = {"prod" : prod_list}
    return render(request, "product_list.html", context)

def product_detail(request, pk):
    prod_detail = get_object_or_404(Product, pk=pk)
    context = {"produ" : prod_detail}
    return render (request, "prod_detail.html", context)
