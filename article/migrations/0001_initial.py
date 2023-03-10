# Generated by Django 4.1.7 on 2023-02-26 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_role', models.CharField(choices=[('Auth', 'Author'), ('READ', 'Reader')], default='READ', max_length=4)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True, null=True)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('language', models.CharField(choices=[('ENG', 'English'), ('FR', 'French'), ('HI', 'Hindi'), ('BEN', 'Bengali'), ('ES', 'Spanish')], default='ENG', max_length=4)),
                ('image', models.ImageField(upload_to='images/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_author', to='article.contributor')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='article_category', to='article.category')),
            ],
        ),
    ]
