from django.urls import path
from products import views

app_name = "products"


urlpatterns = [
    path("", views.ProductMixinView.as_view(), name="products"),
    path("<int:pk>/", views.ProductMixinView.as_view(), name="product-detail"),
]
