from django.db import models
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.core import validators


# Create your models here.
class Article(models.Model):
    title = models.CharField(
        max_length=38,
        validators=[validators.MinLengthValidator(2, "Article Title must be more than 2 characters")],
        unique=True)
    content = models.TextField(max_length=1000, default="there is nothing to display")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def last_updated(self):
        return naturaltime(self.updated_at)

    def __str__(self):
        return self.title
