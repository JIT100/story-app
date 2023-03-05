from django.urls import include,path
from .views import(
    article_list, 
    articles_by_category,
    article_detail,
)
urlpatterns=[
    path('',article_list,name='home'),
    path('article/<int:id>/',article_detail,name='article_detail'),
    path('article/<slug:category_slug/',articles_by_category,name='articles_by_category'),
]