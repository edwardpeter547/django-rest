from api import views
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

app_name = "api"

urlpatterns = [
    path("", view=views.api_home, name="api-home"),
    path("products/", include("products.urls")),
    path("search/", include("search.urls")),
    path("auth/", obtain_auth_token),
    path("token/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token-verify"),
]
