from typing_extensions import ReadOnly
from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    lego = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "content",
            "price",
            "sale_price",
            "my_discount",
            "lego",
        ]

    def get_my_discount(self, obj):
        return obj.get_discount()

    def get_lego(self, obj):
        return "Peter"
