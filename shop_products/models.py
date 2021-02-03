from django.db import models

# Create your models here.
from django.db.models import Q
from django_countries.fields import CountryField

from shop_categories.models import Category


class ProductManager(models.Manager):
    def get_by_is_all(self):
        lookup = (
                Q(is_discount=False) |
                Q(is_discount=True) |
                Q(is_active=True)
        )
        return self.get_queryset().filter(lookup)

    def get_by_discount(self):
        lookup = (
                Q(is_discount=True) &
                Q(is_active=True)
        )
        return self.get_queryset().filter(lookup)

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def get_by_category(self, category_name):
        lookup = (
                Q(is_discount=False) |
                Q(is_discount=True) |
                Q(is_active=True)
        )
        return self.get_queryset().filter(lookup, categories__title_in_url__iexact=category_name)

    def get_by_search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(categories__title__icontains=query) |
                Q(categories__title_in_url__icontains=query) |
                Q(material__icontains=query)

        )
        return self.get_queryset().filter(lookup, is_active=True)


class Product(models.Model):
    SIZE = (
        ("XS", "XS"),
        ("XS - S", "XS - S"),
        ("XS - S - M", "XS - S - M"),
        ("XS - S - M - L", "XS - S - M - L"),
        ("XS - S - M - L - XL", "XS - S - M - L - XL"),
        ("XS - S - M - L - XL - XXL", "XS - S - M - L - XL - XXL"),
        ("XS - S - M - L - XL - XXL - 1X", "XS - S - M - L - XL - XXL - 1X"),
        ("XS - S - M - L - XL - XXL - 1X - 2X", "XS - S - M - L - XL - XXL - 1X - 2X"),
        ("XS - S - M - L - XL - XXL - 1X - 2X - 3X", "XS - S - M - L - XL - XXL - 1X - 2X - 3X"),
        ("XS - S - M - L - XL - XXL - 1X - 2X - 3X - 4X", "XS - S - M - L - XL - XXL - 1X - 2X - 3X - 4X"),
        (
            "XS - S - M - L - XL - XXL - 1X - 2X - 3X - 4X - 5X",
            "XS - S - M - L - XL - XXL - 1X - 2X - 3X - 4X - 5X"),
        ("XS - S - M - L - XL - XXL - 1X - 2X - 3X - 4X - 5X - 6X",
         "XS - S - M - L - XL - XXL - 1X - 2X - 3X - 4X - 5X - 6X")

    )
    DISCOUNT = (
        (10, 10),
        (20, 20),
        (30, 30),
        (40, 40),
        (50, 50),
        (60, 60),
        (70, 70),
        (80, 80),
        (90, 90),
        (100, 100),

    )

    Rating_CHOICES = (
        (1, 'Poor'),
        (2, 'Average'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent')
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="product/images", verbose_name="image(800*800)")
    size = models.CharField(max_length=1000, choices=SIZE, default=None)
    color = models.CharField(max_length=500, default="")
    material = models.CharField(max_length=5000, default="")
    made_in = CountryField(default="")
    discount = models.IntegerField(choices=DISCOUNT, default=0, blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True)
    is_discount = models.BooleanField(default=False, verbose_name="It has a discount / no discount")
    is_active = models.BooleanField(default=False, verbose_name="Activate / deactivate")
    visit_count = models.IntegerField(default=0, blank=True, null=True, editable=False)

    objects = ProductManager()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title

    def absolute_product_url(self):
        return f'/products/{self.id}/{self.title.replace(" ", "-")}'

    def price_discount(self):
        return self.price - (self.price * self.discount / 100)


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="gallery")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"

    def __str__(self):
        return self.title


class ProductComment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_number = models.IntegerField(default=1)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    text = models.TextField()

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.name
