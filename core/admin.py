from django.contrib import admin
from .models import Category, SubCategory, Video, Master

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'name']


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'name']


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['id', 'title', 'model_name', 'category', 'subcategory']
    list_filter = ['category', 'subcategory']
    autocomplete_fields = ['category', 'subcategory']

@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone']