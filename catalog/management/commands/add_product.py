from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Load test data from fixture"

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Category.objects.all().delete()
        Product.objects.all().delete()
        call_command("loaddata", "category_fixture.json")
        call_command("loaddata", "product_fixture.json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))
