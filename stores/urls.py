# api-small-business/stores/urls.py
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register('<The URL prefix>', <The viewset class>, '<The URL name>')
router.register('city', views.CityViewSet, 'city')
router.register('district', views.DistrictViewSet, 'district')
router.register('point-of-sale', views.PointOfSaleViewSet, 'point-of-sale')
router.register('seller', views.SellerViewSet, 'seller')
router.register('product', views.ProductViewSet, 'product')
router.register('customer', views.CustomerViewSet, 'customer')
router.register('order', views.OrderViewSet, 'order')
router.register('order-detail', views.OrderDetailViewSet, 'order-detail')

urlpatterns = router.urls
