# Generated by Django 3.1.5 on 2021-01-30 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_categories', '0001_initial'),
        ('shop_products', '0013_auto_20210130_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_favorite',
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(default='', to='shop_categories.Category'),
        ),
    ]