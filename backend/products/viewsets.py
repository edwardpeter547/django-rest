# from api.mixins import IsStaffEditorPermissionMixin
# from products.models import Product
# from products.serializers import ProductSerializer
# from rest_framework import mixins, viewsets


# # Note. if you are implementing a viewset and you have a permission mixins
# # ensure your permission mixin comes before inheriting the modelviewset
# class ProductViewSet(IsStaffEditorPermissionMixin, viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = "pk"


# class ProductGenericViewSet(
#     mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
# ):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = "pk"


# product_list_view = ProductGenericViewSet.as_view({"get": "list"})
# product_detail_view = ProductGenericViewSet.as_view({"get": "retrieve"})
