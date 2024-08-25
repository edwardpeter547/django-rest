from django.urls import path, include
from api import views

app_name = "api"

urlpatterns = [
    path("", view=views.api_home, name="api-home"),
    path("products/", include("products.urls")),
]
