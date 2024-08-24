import json

from yaml import serialize
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    Django-rest framework API View
    """
    request_data = request.data
    serializer = ProductSerializer(data=request_data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        return Response(serializer.data)
    
