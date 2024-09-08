from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer
from search import client
from rest_framework.response import Response


class SearchListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        user = None
        query = request.GET.get('q', None)
        tags = request.GET.get("tags", None)
        public = str(request.GET.get("public")) != "0"
        kwargs["public"] = public
        if request.user.is_authenticated:
            user = request.user.username
            kwargs["user"] = user
        if tags:
            kwargs['tags'] = tags
        if not query:
            return Response('', status=400)
        results = client.perform_search(query, **kwargs)
        return Response(results)


class SearchListOldView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        search_item = self.request.GET.get('q')
        results = Product.objects.none()
        if search_item is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(search_item, user=user)
        return results