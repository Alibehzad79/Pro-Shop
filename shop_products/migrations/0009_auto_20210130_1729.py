# Generated by Django 3.1.5 on 2021-01-30 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_products', '0008_auto_20210130_1637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='reviews',
            new_name='visit_count',
        ),
    ]