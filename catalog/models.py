from django.db import models

import users


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Продукт",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта", help_text="Укажите описание продукта"
    )
    image = models.ImageField(upload_to="catalog/photo", blank=True, null=True)
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        verbose_name="Категория",
        help_text="Введите категорию продукта",
        blank=True,
        null=True,
        related_name="products",
    )
    purchase_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена продукта"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    publication_attribute = models.BooleanField(default=False, verbose_name="Публикация продукта")

    owner = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE,verbose_name="Владелец")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукты"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name", "purchase_price"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
           ]




class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Категория",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Укажите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
