# Generated by Django 3.1.5 on 2021-02-01 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_blog', '0010_auto_20210201_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_blog.blog'),
        ),
    ]