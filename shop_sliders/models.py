from django.db import models


# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="sliders", verbose_name="image (1100 * 414)")
    link = models.URLField()

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"

    def __str__(self):
        return self.title
