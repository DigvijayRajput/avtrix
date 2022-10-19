from rest_framework.routers import DefaultRouter
from product.views import ProductViewset

router = DefaultRouter()

router.register(r'product', ProductViewset, basename='product')
