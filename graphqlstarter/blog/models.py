from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        ordering = ['name']


class Article(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    category = models.ForeignKey(Category, related_name='articles', on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']
