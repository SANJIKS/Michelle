# Generated by Django 5.0.6 on 2024-05-30 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0004_alter_category_table_alter_dish_table_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='text',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='title',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='title',
        ),
        migrations.AddField(
            model_name='dish',
            name='text_kg',
            field=models.TextField(default='a'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dish',
            name='text_ru',
            field=models.TextField(default='a'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dish',
            name='text_tu',
            field=models.TextField(default='a'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dish',
            name='title_en',
            field=models.CharField(default='a', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dish',
            name='title_kg',
            field=models.CharField(default='a', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dish',
            name='title_ru',
            field=models.CharField(default='a', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dish',
            name='title_tu',
            field=models.CharField(default='a', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='title_en',
            field=models.CharField(default='a', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='title_kg',
            field=models.CharField(default='a', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='title_ru',
            field=models.CharField(default='a', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='title_tu',
            field=models.CharField(default='a', max_length=120),
            preserve_default=False,
        ),
    ]
