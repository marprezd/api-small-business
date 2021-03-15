# api-small-business/stores/views.py
from os import name
from django.db.models import fields
from rest_framework import viewsets
from django_filters import rest_framework as filters
from django_filters import CharFilter
from . import serializers
from . import models


class CityFilter(filters.FilterSet):
    """ 
    This class inherits from FilterSet class and allows to users filter searches based on the name field.
    """
    name = CharFilter(field_name='name', lookup_expr='icontains')
    
    class Meta:
        model = models.City
        fields = ['name']
        
class CityViewSet(viewsets.ModelViewSet):
    """ 
    This class inherit from ModelViewSet and enable viewing and editing cities.
    """
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer
    filter_class = CityFilter
    search_fields = ('name',)
    ordering_fields = ('name',)
    
    
class DistrictFilter(filters.FilterSet):
    """ 
     This class inherits from FilterSet class and allows to users filter searches based on the name field.
     """
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = models.District
        fields = ['name']
       

class DistrictViewSet(viewsets.ModelViewSet):
    """ 
    This class inherit from ModelViewSet and enable viewing and editing districts.
    """
    queryset = models.District.objects.all()
    serializer_class = serializers.DistrictSerializer
    filter_class = DistrictFilter
    search_fields = ('name',)
    ordering_fields = ('name',)
    
    
class PointOfSaleFilter(filters.FilterSet):
    """ 
    This class inherits from FilterSet class and allows to users filter searches based on the name, city, and district fields.
    """
    name = CharFilter(field_name='name', lookup_expr='icontains')
    city = CharFilter(field_name='city', lookup_expr='icontains')
    district = CharFilter(field_name='district', lookup_expr='icontains')
    
    class Meta:
        model = models.PointOfSale
        fields = ['name', 'city', 'district']
        
        
class PointOfSaleViewSet(viewsets.ModelViewSet):
    """ 
    This class inherit from ModelViewSet and enable viewing and editing points of sale.
    """
    queryset = models.PointOfSale.objects.all()
    serializer_class = serializers.PointOfSaleSerializer
    filter_class = PointOfSaleFilter
    search_filter = ('^name', '^city', '^district')
    ordering_fields = ('name',)
    
    
class SellerFilter(filters.FilterSet):
    """ 
    This class inherits from FilterSet class and allows to users filter searches based on the first_name and seller_id fields.
    """
    first_name = CharFilter(field_name='first_name', lookup_expr='icontains')
    seller_id = CharFilter(field_name='seller_id', lookup_expr='icontains')
    
    class Meta:
        model = models.Seller
        fields = ['first_name', 'seller_id']
        
        
class SellerViewSet(viewsets.ModelViewSet):
    """ 
    This class inherit from ModelViewSet and enable viewing and editing sellers.
    """
    queryset = models.Seller.objects.all()
    serializer_class = serializers.SellerSerializer
    filter_class = SellerFilter
    search_fields = ('^first_name', '^seller_id')
    ordering_fields = ('first_name',)
    
    
class ProductFilter(filters.FilterSet):
    """ 
    This class inherits from FilterSet class and allows to users filter searches based on the name, brand, and price fields.
    """
    name = CharFilter(field_name='name', lookup_expr='icontains')
    brand = CharFilter(field_name='brand', lookup_expr='icontains')
    price = CharFilter(field_name='price', lookup_expr='iexact')
    
    class Meta:
        model = models.Product
        fields = ['name', 'brand', 'price']
        
class ProductViewSet(viewsets.ModelViewSet):
    """ 
    This class inherit from ModelViewSet and enable viewing and editing products.
    """
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_class = ProductFilter
    search_fields = ('^name', '^brand', 'price')
    ordering_fields = ('name',)
    
class CustomerFilter(filters.FilterSet):
    """ 
    This class inherits from FilterSet class and allows to users filter searches based on the first_name, last_name, and city.
    """
    first_name = CharFilter(field_name='first_name', lookup_expr='icontains')
    last_name = CharFilter(field_name='last_name', lookup_expr='icontains')
    city = CharFilter(field_name='city', lookup_expr='icontains')
    
    class Meta:
        model = models.Customer
        fields = ['first_name', 'last_name', 'city']
    
class CustomerViewSet(viewsets.ModelViewSet):
    """ 
    This class inherit from ModelViewSet and enable viewing and editing customers.
    """
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    filter_class = CustomerFilter
    search_fields = ('^first_name', '^last_name', '^city')
    ordering_fields = ('first_name',)
    
    
class OrderFilter(filters.FilterSet):
    """ 
    This class inherits from FilterSet class and allows to users filter searches based on the customer field.
    """
    customer = CharFilter(field_name='customer', lookup_expr='icontains')
    
    class Meta:
        model = models.Order
        fields = ['customer']
class OrderViewSet(viewsets.ModelViewSet):
    """ 
    This class inherit from ModelViewSet and enable viewing and editing orders.
    """
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    filter_class = OrderFilter
    search_fields = ('customer',)
    ordering_fields = ('customer',)  
    
    
class OrderDetailFilter(filters.FilterSet):
    """ 
    This class inherits from FilterSet class and allows to users filter searches based on the order, payment, and product fields.
    """
    order = CharFilter(field_name='order', lookup_expr='icontains')
    product = CharFilter(field_name='product', lookup_expr='icontains')
    payment = CharFilter(field_name='payment', lookup_expr='icontains')
    
    class Meta:
        model = models.OrderDetail
        fields = ['order', 'product', 'payment']


class OrderDetailViewSet(viewsets.ModelViewSet):
    """ 
    This class inherit from ModelViewSet and enable viewing and editing order details.
    """
    queryset = models.OrderDetail.objects.all()
    serializer_class = serializers.OrderDetailSerializer
    filter_class = OrderDetailFilter
    search_fields = ('^order', '^product', '^payment')
    ordering_fields = ('order',)
