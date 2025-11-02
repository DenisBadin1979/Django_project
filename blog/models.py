from django.db import models
from django.urls import reverse


class Article(models.Model):
    heading = models.CharField(
        max_length=100, verbose_name="Заголовок", help_text="Укажите заголовок статьи"
    )
    content = models.TextField(
        verbose_name="Содержимое статьи", help_text="Разместите содержимое стать"
    )
    preview = models.ImageField(
        verbose_name="Подходящая картинка",
        upload_to="blog/photo",
        blank=True,
        null=True,
    )
    create_at = models.DateTimeField(auto_now_add=True)
    publication_attribute = models.BooleanField(default=False)
    numbers_views = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["heading", "create_at", "numbers_views"]

    def __str__(self):
        return self.heading

    def get_absolute_url(self):
        return reverse("blog:article_detail", kwargs={"pk": self.pk})
