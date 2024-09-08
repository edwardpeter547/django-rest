from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.conf import settings
import random

# Create your models here.

User = settings.AUTH_USER_MODEL

TAGS_MODEL_VALUES = ["electronics", "cars", "boats", "movies", "cameras"]

# define a product queryset class
class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)

    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs).distinct()
        return qs


class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(model=self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query=query)


class Product(models.Model):

    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    public = models.BooleanField(default=True)

    objects = ProductManager()

    def is_public(self):
        return self.public

    @property
    def body(self):
        return self.content

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    def get_discount(self):
        return "122.20"

    def get_item_url(self):
        return reverse("api:products:detail", args=[self.pk])
    
    def get_tags_list(self):
        return [random.choice(TAGS_MODEL_VALUES)]

    def __str__(self):
        return f"{self.title}(title={self.title}, price={self.price})"
