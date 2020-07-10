from django.urls import path

from .views import CategoriesList, CategoriesArticlesList, ArticleDetail

app_name = 'categories'

urlpatterns = [
    path('', CategoriesList.as_view(), name='categories_list'),
    path('<str:slug>/', CategoriesArticlesList.as_view(), name='categories_articles_list'),
    path('article/<str:slug>/', ArticleDetail.as_view(), name='articles_detail')
]
