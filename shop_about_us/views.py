from django.shortcuts import render

# Create your views here.

from shop_about_us.models import AboutUs


def abouts_us(request):
    abouts = AboutUs.objects.all()
    context = {
        "abouts": abouts
    }
    return render(request, "about_us/about_us.html", context)


