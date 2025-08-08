from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
          
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, related_name="subcategories", on_delete=models.CASCADE, null=True)
        
    def __str__(self):
        return str(self.name or "Unnamed SubCategory")
    
class ModelName(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name or "SubCategory"

class Video(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    model_name = models.ForeignKey(ModelName, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    youtube_link = models.URLField()

    def __str__(self):
        return self.title


class Master(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    
class BotUser(models.Model):
    chat_id = models.BigIntegerField(unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name or str(self.chat_id)
