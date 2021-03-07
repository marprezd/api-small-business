# api-small-business/stores/admin.py
from django.contrib import admin
from . import models


@admin.register(models.Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name',)
    
    
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'reference')
    search_fields = ('name', 'reference')
    
    
@admin.register(models.District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
 
    
@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name',)
    

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer',)
    search_fields = ('customer',)
    

@admin.register(models.OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity')
    search_fields = ('order', 'seller', 'product')
    

@admin.register(models.PointOfSale)
class PointOfSaleAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'address')
    search_fields = ('name', 'city', 'zip_code')