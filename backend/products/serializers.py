from django.conf import settings
from products.models import Product
from rest_framework import serializers
from rest_framework.reverse import reverse

all_fields = [
    "id",
    "url",
    "item_url",
    "edit_url",
    "email",
    "title",
    "content",
    "price",
    "my_discount",
]


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    item_url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.HyperlinkedIdentityField(
        view_name="api:products:update", lookup_field="pk"
    )
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Product
        fields = all_fields

    def get_url(self, obj):

        request = self.context.get("request", None)
        if request is None:
            return None
        return reverse("api:products:detail", kwargs={"pk": obj.pk}, request=request)

    def get_item_url(self, obj):
        request = self.context.get("request", None)
        if request is not None:
            return f"http://{request.get_host()}{obj.get_item_url()}"
        return None

    def get_my_discount(self, obj):
        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()

    def create(self, validated_data):
        # email = validated_data.pop("email", None)
        instance = super().create(validated_data)
        # print(instance)
        return instance
    
    def update(self, instance, validated_data):
        email = validated_data.pop("email", None)
        print(f"This is the email = {email}")
        instance = super().update(instance, validated_data)
        return instance
