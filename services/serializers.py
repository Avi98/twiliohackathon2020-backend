from rest_framework import serializers
from .models import Products


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('user', 'sup_price', 'selling_price', 'margin', 'name',
             'manufacture', 'description', 'onSale', 'image1', 'image2', 'image3',)

