from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class UserProfileManager(models.Manager):
    def get_by_id(self, user_id):
        qs = self.get_queryset().filter(id=user_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=0, blank=True, null=True)
    about_me = models.CharField(max_length=500, blank=True, null=True)
    web_site = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="Users/Profile", blank=True, null=True)

    objects = UserProfileManager()

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "Users Profile"

    def __str__(self):
        return f"{self.user}"
