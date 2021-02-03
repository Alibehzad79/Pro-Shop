import itertools

from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView

from shop_categories.models import Category
from shop_order.forms import OrderDetailForm
from shop_products.forms import ProductCommentForm
from shop_products.models import Product, Gallery, ProductComment


class ProductList(ListView):
    template_name = "products/products_list.html"
    paginate_by = 10
    model = Product

    def get_queryset(self):
        return Product.objects.get_by_is_all().distinct()


class ProductListByDiscount(ListView):
    template_name = "products/products_list.html"
    paginate_by = 10
    model = Product

    def get_queryset(self):
        return Product.objects.get_by_discount()


class ProductListByLatest(ListView):
    template_name = "products/products_list.html"
    paginate_by = 10
    model = Product

    def get_queryset(self):
        return Product.objects.order_by("-id")


class ProductListByPopular(ListView):
    template_name = "products/products_list.html"
    paginate_by = 10
    model = Product

    def get_queryset(self):
        return Product.objects.order_by("-visit_count")


class Search(ListView):
    template_name = "products/products_list.html"
    paginate_by = 10
    model = Product

    def get_queryset(self):
        request = self.request
        query = request.GET.get("q")
        if query is None:
            raise Http404()
        return Product.objects.get_by_search(query)


class ProductListByCategory(ListView):
    template_name = "products/products_list.html"
    paginate_by = 10
    model = Product

    def get_queryset(self, *args, **kwargs):
        category_name = self.kwargs["category_name"]
        category = Category.objects.filter(title_in_url__iexact=category_name).first()
        if category is None:
            raise Http404()
        return Product.objects.get_by_category(category_name)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def product_detail(request, *args, **kwargs):
    product_id = kwargs["product_id"]
    user_order_form = OrderDetailForm(request.POST or None, initial={"productId": product_id})
    product = Product.objects.get_by_id(product_id)
    categories = Category.objects.filter(id=product_id)
    galleries = Gallery.objects.filter(product=product)
    related_product = Product.objects.get_queryset().filter(categories__product=product).distinct()
    related_group = list(my_grouper(4, related_product))

    comment_form = ProductCommentForm(request.POST or None, initial={"productId": product_id})

    if comment_form.is_valid():
        name = comment_form.cleaned_data.get("name")
        email = comment_form.cleaned_data.get("email")
        text = comment_form.cleaned_data.get("text")
        productId = comment_form.cleaned_data.get("productId")
        product: Product = Product.objects.get_by_id(product_id=productId)
        new_comment = ProductComment.objects.create(name=name, email=email, text=text, product=product,
                                                    id_number=product.id)
        if new_comment is not None:
            return redirect(f"/products/{product.id}/{product.title.replace(' ', '-')}")
        comment_form = ProductCommentForm()

    comments = ProductComment.objects.filter(id_number=product_id)
    product.visit_count += 1
    product.save()

    if product is None:
        raise Http404()
    context = {
        "product": product,
        'categories': categories,
        "related_product": related_group,
        "galleries": galleries,
        "comment_form": comment_form,
        "comments": comments,
        "user_order_form": user_order_form
    }
    return render(request, "products/product_detail.html", context)
