from django.urls import path
from products import views

app_name = "products"


urlpatterns = [
    path("", views.product_list_api_view, name="list-products"),
    path("<int:pk>/", views.ProductDetailApiView.as_view(), name="product-detail"),
    path("create/", views.ProductCreateApiView.as_view(), name="create-product"),
]
