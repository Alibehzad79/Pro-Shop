from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from shop_order.forms import OrderDetailForm
from shop_order.models import Order
from shop_products.models import Product


@login_required(login_url="/login")
def new_order(request):
    order_form = OrderDetailForm(request.POST or None)

    if order_form.is_valid():
        order: Order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        if order is None:
            Order.objects.create(owner_id=request.user.id, is_paid=False)

        productId = order_form.cleaned_data.get("productId")
        count = order_form.cleaned_data.get("count")
        if count <= 0:
            count = 1
        product: Product = Product.objects.get_by_id(product_id=productId)
        order.orderdetail_set.create(product_id=product.id, price=product.price, count=count)
        return redirect(f'/products/{product.id}/{product.title.replace(" ", "-")}')
    return redirect("/")


@login_required(login_url="/")
def order_panel(request, *args, **kwargs):
    context = {
        "order": None,
        "details": None,
        "total": 0
    }
    open_order: Order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if open_order is not None:
        context["order"] = open_order
        context["details"] = open_order.orderdetail_set.all()
        context["total"] = open_order.total()

    return render(request, "order/order_panel.html", context)
