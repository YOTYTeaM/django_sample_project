# Generated by Django 4.2.14 on 2024-07-31 12:52

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_alter_article_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, populate_from='title', unique=True),
        ),
    ]
