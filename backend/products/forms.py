from django import forms
from products.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["id", "title", "content", "price", "sale_price"]
