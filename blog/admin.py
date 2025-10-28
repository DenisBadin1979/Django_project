from django.contrib import admin

from blog.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "heading", "content", "publication_attribute")
    list_filter = ("heading", "create_at")
    search_fields = ("heading", "content", "publication_attribute")
