# Generated by Django 3.1.5 on 2021-02-02 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_settings', '0002_setting_site_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialnetwork',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]