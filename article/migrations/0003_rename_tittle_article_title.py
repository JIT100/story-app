# Generated by Django 4.1.7 on 2023-02-26 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_contributor_age_contributor_email_contributor_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tittle',
            new_name='title',
        ),
    ]
