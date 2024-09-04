from django.urls import path
from products import views

app_name = "products"


urlpatterns = [
    path("", views.product_list_create_api_view, name="list"),
    path("<int:pk>/", views.product_detail_api_view, name="detail"),
    path("update/<int:pk>/", views.ProductUpdateApiView.as_view(), name="update"),
]
