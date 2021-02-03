from django.contrib import admin

# Register your models here.
from shop_settings.models import Setting, SocialNetwork, BusinessHours

admin.site.register(Setting)
admin.site.register(BusinessHours)
admin.site.register(SocialNetwork)

