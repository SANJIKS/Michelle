# Generated by Django 5.0.6 on 2024-06-06 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0007_category_is_about_category_is_bar_category_is_coffe_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='weight',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='custom_black_en',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='custom_black_kg',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='custom_black_ru',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='custom_black_tu',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='custom_orange_en',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='custom_orange_kg',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='custom_orange_ru',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='custom_orange_tu',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='main_title_en',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='main_title_kg',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='main_title_ru',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='main_title_tu',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
