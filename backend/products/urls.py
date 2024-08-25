from django.urls import path
from products import views

app_name = "products"


urlpatterns = [
    path("", views.product_list_create_api_view, name="list-create-products"),
    path("<int:pk>/", views.ProductDetailApiView.as_view(), name="product-detail"),
]
