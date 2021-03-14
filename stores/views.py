# api-small-business/stores/views.py
from rest_framework import viewsets
from . import serializers
from . import models


class CityViewSet(viewsets.ModelViewSet):
    """ 
    This class inherit from ModelViewSet and enable viewing and editing cities.
    """
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer
    
    
class DistrictViewSet(viewsets.ModelViewSet):
    """ 
    This class inherit from ModelViewSet and enable viewing and editing districts.
    """
    queryset = models.District.objects.all()
    serializer_class = serializers.DistrictSerializer
    
    
class PointOfSaleViewSet(viewsets.ModelViewSet):
    """ 
    This class inherit from ModelViewSet and enable viewing and editing points of sale.
    """
    queryset = models.PointOfSale.objects.all()
    serializer_class = serializers.PointOfSaleSerializer
    
    
class SellerViewSet(viewsets.ModelViewSet):
    """ 
    This class inherit from ModelViewSet and enable viewing and editing sellers.
    """
    queryset = models.Seller.objects.all()
    serializer_class = serializers.SellerSerializer
    
    
class ProductViewSet(viewsets.ModelViewSet):
    """ 
    This class inherit from ModelViewSet and enable viewing and editing products.
    """
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    
    
class CustomerViewSet(viewsets.ModelViewSet):
    """ 
    This class inherit from ModelViewSet and enable viewing and editing customers.
    """
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    
    
class OrderViewSet(viewsets.ModelViewSet):
    """ 
    This class inherit from ModelViewSet and enable viewing and editing orders.
    """
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    
    
class OrderDetailViewSet(viewsets.ModelViewSet):
    """ 
    This class inherit from ModelViewSet and enable viewing and editing order details.
    """
    queryset = models.OrderDetail.objects.all()
    serializer_class = serializers.OrderDetailSerializer
