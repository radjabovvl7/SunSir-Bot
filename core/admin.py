from django.contrib import admin
from .models import Category, SubCategory, Video, Master, ModelName, BotUser

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")


@admin.register(ModelName) 
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "subcategory", "model_name")
    list_filter = ("category", "subcategory", "model_name")
    search_fields = ("title",)


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone")

#--------Foydalanuvchilar Admini--------
@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ("id", "chat_id", "full_name", "username", "phone_number")
    search_fields = ("chat_id", "full_name", "username")