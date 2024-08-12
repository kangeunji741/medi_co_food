from django.contrib import admin

from main.models import DiseaseCategory, Like, Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','product_id', 'price']
                    # '상품명 ']

admin.site.register(Product, ProductAdmin)



class DiseaseCategoryAdmin(admin.ModelAdmin):
    list_display = ['dcate_id', 'disease_name']


admin.site.register(DiseaseCategory, DiseaseCategoryAdmin)


class LikeAdmin(admin.ModelAdmin):
    list_display = ['like_id', 'user', 'product', 'created_at']
admin.site.register(Like, LikeAdmin)