from django.contrib import admin
from . import models
from .models import User

# Register your models here.
@admin.register(models.User)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'username']