from django.contrib import admin

from goods.models import Categories, Products

# common way
#admin.site.register(Categories)
#admin.site.register(Products)

# for autodilling
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
