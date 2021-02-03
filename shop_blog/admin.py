from django.contrib import admin

# Register your models here.
from shop_blog.models import Category, Tag, Blog, BlogComment

admin.site.register(Category)
admin.site.register(Tag)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("__str__", "visit", "published_date", "is_published")
    list_editable = ("is_published",)
    list_filter = ("is_published", "published_date")
    search_fields = ("author", "title")


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ("__str__", "blog", "comment_date")
    list_filter = ("comment_date",)
    search_fields = ("full_name", "email", "blog")