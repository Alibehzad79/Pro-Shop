# Generated by Django 3.1.5 on 2021-02-01 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_blog', '0008_blogcomment_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='count',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
