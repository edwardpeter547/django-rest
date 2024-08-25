from django.urls import path
from products import views

app_name = "products"


urlpatterns = [
    path("", views.list_create_view, name="create-products"),
    path("<int:pk>/", views.list_create_view, name="product-detail"),
    path("list/", views.list_create_view, name="list"),
]
