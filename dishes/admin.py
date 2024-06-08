from django.contrib import admin
from .models import Category, SubCategory, SVG, Dish

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title_ru']

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['title_ru', 'category']

class DishAdmin(admin.ModelAdmin):
    list_display = ['title_ru', 'subcategory']

class SVGAdmin(admin.ModelAdmin):
    list_display = ['svg']

admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(SVG, SVGAdmin)
