# Generated by Django 3.1.5 on 2021-02-01 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_about_us', '0002_auto_20210201_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='image',
            field=models.ImageField(default='', upload_to='AboutUs/Gallery'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='AboutUsGallery',
        ),
    ]
