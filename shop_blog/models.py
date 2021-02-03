from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
# Create your models here.
from django.db.models import Q


class Category(models.Model):
    title = models.CharField(max_length=300)
    title_in_url = models.CharField(max_length=500, default="category-name")

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=500)
    title_in_url = models.CharField(max_length=500, default="tag-name")

    class Meta:
        verbose_name = "Blog Tag"
        verbose_name_plural = "Blog Tags"

    def __str__(self):
        return self.title


class BlogManager(models.Manager):
    def get_by_published(self):
        return self.get_queryset().filter(is_published=True)

    def get_by_search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(categories__title__icontains=query) |
                Q(categories__title_in_url__icontains=query) |
                Q(tags__title__icontains=query) |
                Q(tags__title_in_url__icontains=query)
        )
        return self.get_queryset().filter(lookup, is_published=True).distinct()

    def get_by_id(self, blog_id):
        qs = self.get_queryset().filter(id=blog_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None


class Blog(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to="blog/images")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    published_date = models.DateTimeField()
    visit = models.IntegerField(default=0, editable=False)
    comment_count = models.IntegerField(default=0, editable=False)
    is_published = models.BooleanField(default=False)

    objects = BlogManager()

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title

    def get_blog_url(self):
        return f"/blog/{self.id}/{self.title.replace(' ', '-')}"


class BlogComment(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    comment = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    count = models.IntegerField(default=0, editable=False)
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.full_name
