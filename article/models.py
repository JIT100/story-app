from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.urls import reverse
from .storage import OverwriteStorage
User = get_user_model()

# Create your models here.
class Contributor(models.Model):
    user=models.ForeignKey(User,related_name="user_profile", on_delete=models.CASCADE)
    name=models.CharField(max_length=150,verbose_name='Full Name',null=True,blank=True)
    age=models.PositiveIntegerField(max_length=10,null=True,blank=True)
    email = models.EmailField(unique=True,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,blank=True)
    class USER_ROLE(models.TextChoices):
        AUTHOR='Auth',_('Author')
        READER='READ',_('Reader')
    user_role=models.CharField(max_length=4,choices=USER_ROLE.choices,default=USER_ROLE.READER)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('articles_by_category', args=[self.slug])
    
class Article(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField(blank=True,null=True)
    published_date=models.DateTimeField(auto_now_add=True,blank=True)
    date_modified = models.DateTimeField(auto_now=True)
    author=models.ForeignKey(Contributor,related_name='article_author',on_delete=models.CASCADE)
    class LANGUAGE (models.TextChoices):
        ENGLISH='ENG',_('English'),
        FRENCH='FR',_('French')
        HINDI='HI',_('Hindi')
        BENGALI='BEN',_('Bengali')
        SPANISH='ES',_('Spanish')

    language=models.CharField(max_length=4,choices=LANGUAGE.choices,default=LANGUAGE.ENGLISH)
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        related_name='article_category'
    )
    image=models.ImageField(upload_to='images/',storage=OverwriteStorage())
    def __str__(self):
        return self.title