# Generated by Django 5.0.6 on 2024-06-06 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0008_dish_weight_subcategory_custom_black_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='image',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='link',
        ),
    ]
