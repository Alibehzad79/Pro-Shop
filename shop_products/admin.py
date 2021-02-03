from django.contrib import admin

# Register your models here.
from shop_products.models import Product, Gallery, ProductComment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("__str__", "price", "visit_count", "is_discount", "is_active")
    list_editable = ("is_active",)
    list_filter = ("is_discount", "is_active")
    search_fields = ("title",)


@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ("__str__", "product", "email")
    list_filter = ("product",)
    search_fields = ("name",)


admin.site.register(Gallery)
