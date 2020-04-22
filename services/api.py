from .models import Products
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from knox.auth import TokenAuthentication
from .serializers import ProductsSerializer
from rest_framework.response import Response

# Create your views here.
class ServiceViewSet(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classess = [permissions.IsAuthenticated]

    def get(self, request):
        products = Products()
        productList = []
        for products in Products.objects.all():
            productList.append({
                "name":products.name,
                "sup_price": products.sup_price,
                "selling_price": products.selling_price,
                "manufacture": products.manufacture,
                "description": products.description,
                "onSale": products.onSale,
                "user_id": products.user_id,
                "user_name":products.name
                })
        return Response(productList)

