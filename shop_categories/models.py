from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=300)
    title_in_url = models.CharField(max_length=500, default="category-name")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title
