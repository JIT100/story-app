from django.urls import include,path
from .views import(
    story_list, 
    stories_by_category,
    story_detail,
    storyFormView
)
urlpatterns=[
    path('',story_list,name='home'),
    path('story/create',storyFormView.as_view(),name='story-create'),
    path('story/<int:id>/',story_detail,name='story_detail'),
    path('story/<slug:category_slug/',stories_by_category,name='articles_by_category'),
]