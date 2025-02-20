# Generated by Django 4.2.14 on 2024-07-29 12:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_alter_article_author_alter_article_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=38, unique=True, validators=[django.core.validators.MinLengthValidator(2, 'Article Title must be more than 2 characters')]),
        ),
    ]
