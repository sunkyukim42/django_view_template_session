from django.conf import settings
from django.db import models

class Article(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='articles',
        null=False,
        blank=False,
    )

    content = models.TextField(
        null=False,
        blank=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False,
        editable=False,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        null=False,
        blank=False,
        editable=False,
    )

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'article'
        verbose_name_plural = 'articles'

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments',
        null=False,
        blank=False,
    )

    content = models.TextField(
        null=False,
        blank=False,
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
        null=False,
        blank=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False,
        editable=False,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        null=False,
        blank=False,
        editable=False,
    )
