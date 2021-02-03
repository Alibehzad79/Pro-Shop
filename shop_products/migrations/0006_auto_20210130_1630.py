# Generated by Django 3.1.5 on 2021-01-30 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_products', '0005_auto_20210130_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(blank=True, choices=[('10', '10'), ('20', 20), ('30', 30), ('40', 40), ('50', 50), ('60', 60), ('70', 70), ('80', 80), ('90', 90), ('100', 100)], default=0, null=True),
        ),
    ]
