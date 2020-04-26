from rest_framework import serializers
from .models import Products
from django.contrib.auth.models import User


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id','user', 'sup_price', 'selling_price', 'margin', 'name',
             'manufacture', 'description', 'onSale', 'image1', 'image2', 'image3',)
        def create(self, validate_data):
            print('success')
            user_id = validate_data.pop('user')
            user = User.objects.filter(id= user_id)
            return Products.objects.create(user=user, **validate_data)

