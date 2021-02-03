from django.urls import path

from shop_blog.views import BlogList, Search, blog_detail

urlpatterns = [
    path("blog", BlogList.as_view()),
    path("blog/<blog_id>/<title>", blog_detail),
    path("blog/search", Search.as_view()),
]
