# api-small-business/stores/serializers.py
from rest_framework import serializers
from . import models


class CitySerializer(serializers.ModelSerializer):
    """This class inherit from the ModelSerializer class 
    that generates serializer fields that are based on the corresponding model’s fields.
    """
    class Meta:
        model = models.City
        fields = ('id', 'name',)
        

class DistrictSerializer(serializers.ModelSerializer):
    """This class inherit from the ModelSerializer class 
    that generates serializer fields that are based on the corresponding model’s fields.
    """
    class Meta:
        model = models.District
        fields = ('id', 'name',)
     
        
class PointOfSaleSerializer(serializers.ModelSerializer):
    """This class inherit from the ModelSerializer class 
    that generates serializer fields that are based on the corresponding model’s fields.
    """
    # Display a foreign key value instead of the id
    city = serializers.CharField(source='city.name')
    district = serializers.CharField(source='district.name')
    
    class Meta:
        model = models.PointOfSale
        fields = ('id', 'name', 'address', 'zip_code', 'city', 'district', 'phone')
        

class SellerSerializer(serializers.ModelSerializer):
    """This class inherit from the ModelSerializer class 
    that generates serializer fields that are based on the corresponding model’s fields.
    """
    class Meta:
        model = models.Seller
        fields = ('id', 'first_name', 'middle_name', 'last_name', 'seller_id')
        
        
class ProductSerializer(serializers.ModelSerializer):
    """This class inherit from the ModelSerializer class 
    that generates serializer fields that are based on the corresponding model’s fields.
    """
    class Meta:
        model = models.Product
        fields = ('id', 'name', 'reference', 'brand', 'price', 'description')
        

class CustomerSerializer(serializers.ModelSerializer):
    """This class inherit from the ModelSerializer class 
    that generates serializer fields that are based on the corresponding model’s fields.
    """
    # Display a foreign key value instead of the id
    city = serializers.CharField(source='city.name')
    district = serializers.CharField(source='district.name')
    
    class Meta:
        model = models.Customer
        fields = (
            'id', 
            'first_name', 
            'middle_name', 
            'last_name', 
            'address', 
            'zip_code',
            'district',
            'city',
            'email',
            'phone')
        
        
class OrderSerializer(serializers.ModelSerializer):
    """This class inherit from the ModelSerializer class 
    that generates serializer fields that are based on the corresponding model’s fields.
    """
    # Display a foreign key value instead of the id
    customer = serializers.CharField(source='customer.first_name')
    
    class Meta:
        model = models.Order
        fields = ('id', 'customer', 'date')
        
        
class OrderDetailSerializer(serializers.ModelSerializer):
    """This class inherit from the ModelSerializer class 
    that generates serializer fields that are based on the corresponding model’s fields.
    """
    # Display a foreign key value instead of the id
    order = serializers.CharField(source='order.customer')
    product = serializers.CharField(source='product.name')
    seller = serializers.CharField(source='seller.seller_id')
    location = serializers.CharField(source='location.name')
    
    class Meta:
        model = models.OrderDetail
        fields = (
            'id',
            'quantity',
            'order',
            'product',
            'payment',
            'seller',
            'location')