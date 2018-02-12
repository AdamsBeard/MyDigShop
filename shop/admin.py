from django.contrib import admin
from .models import Notice, Category, Goods
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'visible', 'id',]
    prepopulated_fields = {'slug': ('title',)}


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['good', 'fkey', 'datetime']

admin.site.register(Notice)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Goods, GoodsAdmin)