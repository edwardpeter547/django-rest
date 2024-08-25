from rest_framework import generics, mixins
from products.models import Product
from products.serializers import ProductSerializer


class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content", None)
        if not content:
            content = title
        serializer.save(content=content)


product_list_create_api_view = ProductListCreateApiView.as_view()
