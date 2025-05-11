from django.contrib import admin

from article.models import Article, Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'author'
    ]
    list_filter = [
        'title',
        'author'
    ]
    list_per_page = 10


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'article',
        'author',
    ]
    list_per_page = 10
