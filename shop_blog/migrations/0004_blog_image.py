# Generated by Django 3.1.5 on 2021-01-31 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_blog', '0003_auto_20210131_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='', upload_to='blog/images'),
            preserve_default=False,
        ),
    ]