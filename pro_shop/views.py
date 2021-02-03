import itertools

from django.shortcuts import render

from shop_blog.models import Blog
from shop_categories.models import Category
from shop_contact_us.models import ContactUs
from shop_products.models import Product
from shop_settings.models import Setting, SocialNetwork
from shop_sliders.models import Slider


def meta(request):
    setting = Setting.objects.first()
    context = {
        "setting": setting
    }
    return render(request, "shared/Meta.html", context)


def header(request):
    categories = Category.objects.all()
    setting = Setting.objects.first()
    networks = SocialNetwork.objects.all()
    context = {
        "categories": categories,
        "setting": setting,
        'networks': networks
    }
    return render(request, "shared/Header.html", context)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def home_page(request):
    latest_product = Product.objects.order_by("-id").all()[:8]
    latest_group = list(my_grouper(4, latest_product))
    popular_product = Product.objects.order_by("-visit_count").all()[:8]
    popular_group = list(my_grouper(4, popular_product))
    discount_product = Product.objects.get_by_discount().all()[:8]
    discount_group = list(my_grouper(4, discount_product))
    latest_blog = Blog.objects.order_by("-id").all()[:4]
    sliders = Slider.objects.all()

    contact_us = ContactUs.objects.last()

    context = {
        "latest_product": latest_group,
        "popular_product": popular_group,
        "discount_product": discount_group,
        "latest_blog": latest_blog,
        "contact_us": contact_us,
        "sliders": sliders
    }
    return render(request, "home_page.html", context)


def footer(request):
    setting = Setting.objects.first()
    networks = SocialNetwork.objects.all()
    context = {
        "setting": setting,
        'networks': networks
    }
    return render(request, "shared/Footer.html", context)
