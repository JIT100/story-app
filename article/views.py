from django.shortcuts import render,get_object_or_404
from .models import Article,Category
from .forms import StoryForm
from django.views.generic.edit import FormView,CreateView
from django.urls import reverse_lazy
# Create your views here.
def story_list(request,*args,**kwargs):
    stories=Article.objects.order_by('-published_date')
    content={

        'stories':stories
    }
    return render(request,'story_list.html',content)

def story_detail(request,id):
    story=get_object_or_404(Article,id=id)
    content={
        'story':story
    }
    return render(request,'story_detail.html',content)

def stories_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    articles = Article.objects.filter(category=category)
    context = {'category': category, 'articles': articles}
    return render(request, 'story/story_category.html', context)

class storyFormView(CreateView):
    form_class=StoryForm
    template_name='story_create.html'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    success_url=reverse_lazy('home')