from django.urls import path

from shop_contact_us.views import contact_us

urlpatterns = [
    path("contact-us", contact_us)
]
