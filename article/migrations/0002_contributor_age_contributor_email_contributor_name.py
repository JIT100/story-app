# Generated by Django 4.1.7 on 2023-02-26 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='age',
            field=models.PositiveIntegerField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='contributor',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='contributor',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Full Name'),
        ),
    ]