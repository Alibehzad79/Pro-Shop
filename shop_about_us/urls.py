from django.urls import path

from shop_about_us.views import abouts_us

urlpatterns = [
    path("about-us", abouts_us)
]
