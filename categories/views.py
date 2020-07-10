from django.views.generic import ListView, DetailView

from .models import Category, Article


class CategoriesList(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'categories/categories_list.html'


class CategoriesArticlesList(DetailView):
    model = Category
    template_name = 'categories/categories_articles_list.html'


class ArticleDetail(DetailView):
    model = Article
    template_name = 'categories/article_detail.html'



