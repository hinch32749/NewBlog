from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import slugify


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заглавие')
    publish = models.DateField(auto_now_add=True, verbose_name='Опубликовано')
    author = models.ForeignKey('Author', on_delete=models.CASCADE,
                               related_name='blog_posts', verbose_name='Автор')
    description = models.TextField(max_length=2500, verbose_name='Содержание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Блоги'
        verbose_name = 'Блог'
        ordering = ('publish', )


class Author(AbstractUser):
    biography = models.TextField(max_length=2500, verbose_name='Биография')

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        pass


class Comment(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    description = models.TextField(max_length=500, verbose_name='Комментарий')
    publish = models.DateField(auto_now_add=True, verbose_name='Опубликовано')
