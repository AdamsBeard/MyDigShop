from django.contrib import admin
from .models import Notice, Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'visible', 'id',]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Notice)
admin.site.register(Category, CategoryAdmin)