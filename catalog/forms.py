import re

from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.forbidden_words = [
            'казино', 'криптовалюта', 'крипта', 'биржа',
            'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
        ]


        self._apply_styling()

    def _apply_styling(self):
        """Применяет стилизацию ко всем полям формы"""

        # Общие классы для всех полей
        common_classes = 'form-control form-control-lg'
        error_classes = 'is-invalid'

        # Стилизация поля названия
        self.fields['name'].widget.attrs.update({
            'class': common_classes,
            'placeholder': 'Введите название продукта...',
            'autofocus': True,
        })

        # Стилизация поля описания
        self.fields['description'].widget.attrs.update({
            'class': f'{common_classes} form-textarea',
            'placeholder': 'Опишите особенности продукта...',
            'rows': 5,
        })

        # Стилизация поля цены
        self.fields['purchase_price'].widget.attrs.update({
            'class': common_classes,
            'placeholder': '0.00',
            'min': '0.01',
            'step': '0.01',
        })

        # Добавляем иконки и дополнительную стилизацию через data-атрибуты
        self.fields['name'].widget.attrs.update({
            'data-toggle': 'tooltip',
            'title': 'Укажите понятное название продукта',
        })

        self.fields['purchase_price'].widget.attrs.update({
            'data-toggle': 'tooltip',
            'title': 'Цена должна быть положительным числом',
        })



    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        self._check_forbidden_words_exact(name, 'названии')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        self._check_forbidden_words_exact(description, 'описании')
        return description

    def _check_forbidden_words_exact(self, text, field_name):
        """Проверка на точное совпадение слов (с учетом границ слов)"""
        if not text:
            return

        found_words = []
        for word in self.forbidden_words:
            # Используем регулярное выражение для поиска целых слов
            pattern = r'\b' + re.escape(word) + r'\b'
            if re.search(pattern, text, re.IGNORECASE):
                found_words.append(word)

        if found_words:
            error_message = self._get_error_message(found_words, field_name)
            raise ValidationError(error_message)

    def _get_error_message(self, found_words, field_name):
        if len(found_words) == 1:
            return f"В {field_name} обнаружено запрещенное слово: '{found_words[0]}'"
        else:
            words_list = "', '".join(found_words)
            return f"В {field_name} обнаружены запрещенные слова: '{words_list}'"

    def clean_purchase_price(self):
        """Валидация цены продукта"""
        price = self.cleaned_data.get('purchase_price')

        # Проверка на отрицательную цену
        if price is not None and price < 0:
            raise ValidationError(
                "Цена продукта не может быть отрицательной. "
                "Пожалуйста, введите положительное значение."
            )

        # Проверка на нулевую цену (опционально)
        if price == 0:
            raise ValidationError(
                "Цена продукта не может быть нулевой. "
                "Если продукт бесплатный, укажите символическую цену (например, 0.01)."
            )

        return price
