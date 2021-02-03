from django.urls import path

from shop_products.views import ProductList, ProductListByLatest, ProductListByDiscount, ProductListByPopular, \
    product_detail, ProductListByCategory, Search

urlpatterns = [
    path("products", ProductList.as_view()),
    path("products/<product_id>/<title>", product_detail),
    path("products/<product_id>/<title>/", product_detail),
    path("products/seach", Search.as_view()),
    path("products/search/", Search.as_view()),
    path("products/<category_name>/", ProductListByCategory.as_view()),
    path("products/<category_name>/", ProductListByCategory.as_view()),
    path("products/", ProductList.as_view()),
    path("products/discount", ProductListByDiscount.as_view()),
    path("products/discount/", ProductListByDiscount.as_view()),
    path("products/latest", ProductListByLatest.as_view()),
    path("products/latest/", ProductListByLatest.as_view()),
    path("products/popular", ProductListByPopular.as_view()),
    path("products/popular/", ProductListByPopular.as_view()),
]