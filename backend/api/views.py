from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    Django-rest framework API View
    """
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(
        #     product_data, fields=["id", "title", "content", "price", "sale_price"]
        # )
        data = ProductSerializer(instance).data
    return Response(data)
