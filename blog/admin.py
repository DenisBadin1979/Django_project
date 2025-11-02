from django.contrib import admin

from blog.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "heading", "content", "publication_attribute")
    list_filter = ("publication_attribute", "create_at", "numbers_views")
    search_fields = ("heading", "content", "publication_attribute")
