from django.contrib import admin
from .models import ProductModel
# Register your models here.
@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','pname','price','stock','created_at','updated_at']