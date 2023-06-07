from rest_framework import routers

from products.views import ProductViewSet, CategoryViewSet


router = routers.DefaultRouter()


router.register(r'product', ProductViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = [
    *router.urls
]