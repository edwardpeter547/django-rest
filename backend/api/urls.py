from api import views
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

app_name = "api"

urlpatterns = [
    path("", view=views.api_home, name="api-home"),
    path("products/", include("products.urls")),
    path("search/", include("search.urls")),
    path("auth/", obtain_auth_token),
]
