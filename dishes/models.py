from django.db import models

class Category(models.Model):
    title_ru = models.CharField(max_length=120)
    title_kg = models.CharField(max_length=120)
    title_tu = models.CharField(max_length=120)
    title_en = models.CharField(max_length=120)
    image = models.ImageField(upload_to='categories/')
    link = models.CharField(max_length=100)
    number = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self) -> str:
        return self.title_ru

    class Meta:
        db_table = 'categories'  # Указываем имя таблицы в базе данных

class SubCategory(models.Model):
    title_ru = models.CharField(max_length=120)
    title_kg = models.CharField(max_length=120)
    title_tu = models.CharField(max_length=120)
    title_en = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='subcategories/')
    link = models.CharField(max_length=100)
    number = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.title_ru} -> {self.category.title_ru}"

    class Meta:
        db_table = 'subcategories'  # Указываем имя таблицы в базе данных

class SVG(models.Model):
    svg = models.FileField(upload_to='svgs/')

    def __str__(self) -> str:
        return str(self.svg)

    class Meta:
        db_table = 'svgs'  # Указываем имя таблицы в базе данных

class Dish(models.Model):
    title_ru = models.CharField(max_length=120)
    title_kg = models.CharField(max_length=120)
    title_tu = models.CharField(max_length=120)
    title_en = models.CharField(max_length=120)
    image = models.ImageField(upload_to='dishes/')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True)
    svgs = models.ManyToManyField(SVG, blank=True)
    text_ru = models.TextField()
    text_kg = models.TextField()
    text_tu = models.TextField()
    text_en = models.TextField()
    price = models.DecimalField(max_digits=10, default=0, decimal_places=2)
    number = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self) -> str:
        return self.title_ru

    class Meta:
        db_table = 'dishes'  # Указываем имя таблицы в базе данных
