from rest_framework import serializers
from products.models import Product
from rest_framework.validators import UniqueValidator

def validate_title(value):
        qs = Product.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"The title {value} already exists")
        return value


unique_title_validator = UniqueValidator(queryset=Product.objects.all(), lookup="iexact")