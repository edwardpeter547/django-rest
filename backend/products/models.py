from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    def get_discount(self):
        return "122.20"

    def get_item_url(self):
        return reverse("api:products:detail", args=[self.pk])

    def __str__(self):
        return f"{self.title}(title={self.title}, price={self.price})"
