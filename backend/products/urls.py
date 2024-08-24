from django.urls import path
from products import views

app_name = "products"


urlpatterns = [
    path("", views.ProductCreateApiView.as_view(), name="create-product"),
    path("<int:pk>/", views.product_create_api_view, name="product-detail"),
]
