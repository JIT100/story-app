from django.shortcuts import render,get_object_or_404
from .models import Article,Category
# Create your views here.
def article_list(request,*args,**kwargs):
    articles=Article.objects.order_by('-published_date')[:3]
    content={
        'articles':articles
    }
    return render(request,'article_list1.html',content)

def article_detail(request,id):
    article=get_object_or_404(Article,id=id)
    content={
        'article':article
    }
    return render(request,'article_detail.html',content)

def articles_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    articles = Article.objects.filter(category=category)
    context = {'category': category, 'articles': articles}
    return render(request, 'articles/articles_by_category.html', context)