from django.contrib import admin

# Register your models here.
from shop_contact_us.models import ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("__str__", "subject", "full_name", "is_read")
    list_filter = ("is_read",)
    list_editable = ("is_read",)
    search_fields = ("subject", "full_name")
