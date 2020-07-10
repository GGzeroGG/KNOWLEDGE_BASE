from django.db import models
from django.shortcuts import reverse

from treebeard.mp_tree import MP_Node

from markitup.fields import MarkupField


class Category(MP_Node):
    """Предстовление о модели категорий"""

    name = models.CharField('Название', max_length=100)
    slug = models.SlugField('Url', max_length=100, unique=True)

    def get_absolute_url(self):
        """Создание персональной ссылки для экземпляра модели"""

        return reverse('categories:categories_articles_list', kwargs={'slug': self.slug})

    def __str__(self):
        return 'Category: %s' % self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Article(models.Model):
    """Предстовление о можели стати"""

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='article')

    name = models.CharField('Название', max_length=100)
    slug = models.SlugField('Url', max_length=100, unique=True)

    number = models.FloatField('Порядковый номер стати')
    content = MarkupField()

    def get_absolute_url(self):
        """Создание персональной ссылки для экземпляра модели"""

        return reverse('categories:articles_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return 'Article: %s' % self.name

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
