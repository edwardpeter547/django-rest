from django.conf import settings
from products.models import Product
from rest_framework import serializers
from rest_framework.reverse import reverse
from products.validators import validate_title, unique_title_validator
from api.serializers import UserPublicSerializer

all_fields = [
    "id",
    "url",
    "owner",
    # "user",
    # "my_user",
    # "item_url",
    # "edit_url",
    # "name",
    # "email",
    "title",
    "content",
    "price",
    "my_discount",
]


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source="user", read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    title = serializers.CharField(validators=[unique_title_validator])
    # email = serializers.EmailField(write_only=True)
    # my_user = serializers.SerializerMethodField(read_only=True)
    # item_url = serializers.SerializerMethodField(read_only=True)
    # edit_url = serializers.HyperlinkedIdentityField(
    #     view_name="api:products:update", lookup_field="pk"
    # )
    # name = serializers.CharField(source="title", read_only=True)

    class Meta:
        model = Product
        fields = all_fields

    def get_url(self, obj):
        request = self.context.get("request", None)
        if request is None:
            return None
        return reverse("api:products:detail", kwargs={"pk": obj.pk}, request=request)
    
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

    # def get_my_user(self, obj):
    #     return {
    #         "username": obj.user.username,
    #         "email": obj.user.email,
    #     }

    # def get_item_url(self, obj):
    #     request = self.context.get("request", None)
    #     if request is not None:
    #         return f"http://{request.get_host()}{obj.get_item_url()}"
    #     return None

    # validate title
    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"The title {value} already exists")
    #     return value

    # suppose you want to validate based on the user
    # in this special cases we want to write our validators
    # inline in the serializer as demostrated below because of
    # having access to the context and using the request object.

    # def validate_title(self, value):
    #     request = self.context.get("request", None)
    #     if request is not None:
    #         user = request.user
    #     qs = Product.objects.filter(user=user, title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"The title {value} already exists")
    #     return value
