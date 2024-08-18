from django.http import JsonResponse
from products.models import Product
from django.forms.models import model_to_dict


def api_home(request, *args, **kwargs):
    product_data = Product.objects.all().order_by("?").first()
    data = {}
    if product_data:
        data = model_to_dict(product_data, fields=["id", "title", "content", "price"])
    return JsonResponse(data)
