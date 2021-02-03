from django.db import models


# Create your models here.

class Setting(models.Model):
    site_logo = models.ImageField(upload_to="site_setting/logo", default="")
    title = models.CharField(max_length=1000)
    description = models.TextField()
    phone = models.CharField(max_length=25)
    email = models.EmailField()
    address = models.CharField(max_length=2000)
    get_in_touch_text = models.CharField(max_length=2000, blank=True, null=True)
    copy_right = models.CharField(max_length=500)

    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.title


class SocialNetwork(models.Model):
    title = models.CharField(max_length=500)

    link = models.URLField()

    class Meta:
        verbose_name = "Social Network"
        verbose_name_plural = "Social Networks"

    def __str__(self):
        return self.title


class BusinessHours(models.Model):
    text = models.CharField(max_length=500, default="Monday - Friday - 9am to 5pm")

    class Meta:
        verbose_name = "Business Hours"
        verbose_name_plural = "Business Hours"

    def __str__(self):
        return self.text
