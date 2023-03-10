from django.forms import forms,ModelForm
from .models import Article

class StoryForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title','content','author','language','image']