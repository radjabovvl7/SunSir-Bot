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
    list_display = ('id', 'title', 'subcategory', 'category')
    list_filter = ('subcategory', 'category')
    search_fields = ['title']


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone']