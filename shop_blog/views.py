from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, DetailView

from shop_blog.forms import BlogCommentForm
from shop_blog.models import Blog, Category, Tag, BlogComment


class BlogList(ListView):
    template_name = "blog/blog_list.html"
    model = Blog
    paginate_by = 8

    def get_queryset(self, *args, **kwargs):
        return Blog.objects.get_by_published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[''] = ""
        return context


def blog_sidebar(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    populars = Blog.objects.order_by("-visit").all()[:3]
    recent = Blog.objects.order_by("-id").all()[:3]
    context = {
        "categories": categories,
        "tags": tags,
        "populars": populars,
        "recent": recent
    }
    return render(request, "blog/blog_sidebar.html", context)


class Search(ListView):
    template_name = "blog/blog_list.html"
    model = Blog
    paginate_by = 8

    def get_queryset(self):
        request = self.request
        query = request.GET.get("s")
        if query is not None:
            return Blog.objects.get_by_search(query)
        return Blog.objects.get_by_published()


def blog_detail(request, *args, **kwargs):
    blog_id = kwargs["blog_id"]
    detail: Blog = Blog.objects.get_by_id(blog_id)
    blog_form = BlogCommentForm(request.POST or None, initial={"blog_id": blog_id})

    if blog_form.is_valid():
        full_name = blog_form.cleaned_data.get("full_name")
        email = blog_form.cleaned_data.get("email")
        comment = blog_form.cleaned_data.get("comment")
        blog_id = blog_form.cleaned_data.get("blog_id")

        blog: Blog = Blog.objects.get_by_id(blog_id)

        new_comment = BlogComment.objects.create(full_name=full_name, email=email, comment=comment, blog_id=blog.id)
        if new_comment is not None:
            return redirect(f"/blog/{blog.id}/{blog.title.replace(' ', '-')}")
        BlogComment.count += 1
        BlogComment.save()

        blog_form = BlogCommentForm()

    detail.visit += 1
    detail.save()

    comments = BlogComment.objects.filter(blog=blog_id)

    context = {
        "detail": detail,
        "blog_form": blog_form,
        "comments": comments
    }

    return render(request, "blog/blog_detail.html", context)
