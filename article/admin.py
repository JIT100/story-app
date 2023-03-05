from django.contrib import admin
from .models import Contributor,Article,Category
# Register your models here.
admin.site.register(Contributor)
admin.site.register(Article)
admin.site.register(Category)

