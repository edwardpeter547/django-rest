from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework import status


class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):

        if serializer.is_valid():
            instance = serializer.save()
            print(instance)


class ProductDeleteApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        print(instance)
        return super().perform_destroy(instance)


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


@api_view(["POST", "GET"])
def list_create_view(request, *args, **kwargs):
    method = request.method

    if method == "GET":
        pk = kwargs.get("pk", None)
        if pk is not None:
            queryset = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(queryset, many=False).data
            return Response(data)
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)

    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content")
            if not content:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response(
            {"invalid": "invalid data, cannot save!"},
            status=status.HTTP_400_BAD_REQUEST,
        )
