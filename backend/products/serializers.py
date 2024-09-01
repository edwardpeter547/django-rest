from dataclasses import fields

from products.models import Product
from pyexpat import model
from rest_framework import serializers
from typing_extensions import ReadOnly

all_fields = ["id", "title", "content", "price", "my_discount"]


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        # all_fields.extend(["sale_price", "my_discount"])
        fields = all_fields

    def get_my_discount(self, obj):
        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
