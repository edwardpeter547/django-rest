from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer


class SearchListView(generics.ListAPIView):
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