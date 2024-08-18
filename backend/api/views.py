from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    Django-rest framework API View
    """
    product_data = Product.objects.all().order_by("?").first()
    data = {}
    if product_data:
        data = model_to_dict(product_data, fields=["id", "title", "content", "price"])
    return Response(data)
