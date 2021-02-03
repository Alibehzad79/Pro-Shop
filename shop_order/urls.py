from django.urls import path

from shop_order.views import order_panel, new_order

urlpatterns = [
    path('add-user-order', new_order),
    path("order-panel", order_panel),
]
