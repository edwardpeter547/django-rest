from posixpath import basename

from products.viewsets import ProductGenericViewSet, ProductViewSet, product_list_view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("products", ProductGenericViewSet, basename="products")

print(router.urls)
urlpatterns = router.urls
