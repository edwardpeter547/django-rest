from urllib import response

from django.forms import model_to_dict
from django.http import Http404
from django.shortcuts import get_object_or_404
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework import authentication, generics, mixins, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_detail_api_view = ProductDetailApiView.as_view()


class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]
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
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content", None)
        if not content:
            content = title
        serializer.save(content=content)


product_list_create_api_view = ProductListCreateApiView.as_view()


# using class based views

# class ProductMixinView(
#     generics.GenericAPIView,
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.CreateModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
# ):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = "pk"

#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         print("this is the pk", pk)
#         if pk is not None:
#             return self.retrieve(request, *args, **kwargs)
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         print(args, kwargs)
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

#     def perform_destroy(self, instance):
#         print(type(instance), instance)
#         instance.delete()

#     def perform_update(self, serializer):
#         title = serializer.validated_data.get("title")
#         content = serializer.validated_data.get("content", None)
#         if not content:
#             content = title

#         serializer.save(content=content)

#     def perform_create(self, serializer):
#         title = serializer.validated_data.get("title")
#         content = serializer.validated_data.get("content", None)
#         if not content:
#             content = title
#         serializer.save(content=content)


# using function based view approach

# @api_view(["POST", "GET"])
# def list_create_view(request, *args, **kwargs):
#     method = request.method

#     if method == "GET":
#         pk = kwargs.get("pk", None)
#         if pk is not None:
#             queryset = get_object_or_404(Product, pk=pk)
#             data = ProductSerializer(queryset, many=False).data
#             return Response(data)
#         queryset = Product.objects.all()
#         data = ProductSerializer(queryset, many=True).data
#         return Response(data)

#     if method == "POST":
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             title = serializer.validated_data.get("title")
#             content = serializer.validated_data.get("content")
#             if not content:
#                 content = title
#             serializer.save(content=content)
#             return Response(serializer.data)
#         return Response(
#             {"invalid": "invalid data, cannot save!"},
#             status=status.HTTP_400_BAD_REQUEST,
#         )


# @api_view(["DELETE", "PUT"])
# def update_delete_view(request, *args, **kwargs):

#     method = request.method

#     if method == "DELETE":
#         pk = kwargs.get("pk", None)
#         if pk is not None:
#             obj = get_object_or_404(Product, pk=pk)
#             print(obj, type(obj))
#             # obj.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         return Response(status=status.HTTP_400_BAD_REQUEST)

#     else:

#         pk = kwargs.get("pk", None)
#         request_data = request.data
#         if pk is not None:
#             data = get_object_or_404(Product, pk=pk)
#             if "title" not in request_data.keys():
#                 request_data["title"] = data.title

#             serializer = ProductSerializer(data=request_data, many=False)
#             if serializer.is_valid():
#                 serializer.update(
#                     instance=data, validated_data=serializer.validated_data
#                 )
#                 return Response(
#                     serializer.data,
#                     status=status.HTTP_200_OK,
#                 )
#             return Response(
#                 {"update": "invalid data"}, status=status.HTTP_400_BAD_REQUEST
#             )
#         return Response({"update": "invalid data"}, status=status.HTTP_400_BAD_REQUEST)
