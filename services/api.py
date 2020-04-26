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

    # all products
    def get(self, request):
        serilaizer = ProductsSerializer(Products.objects.all(), many=True)
        return Response(serilaizer.data)


# CRUD Products
class ProductsViewSet(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classess = [permissions.IsAuthenticated]

    def get(self, response, pk):
        if response.query_params.get('id'):
            product = Products.objects.filter(
                user_id=pk, id=response.query_params.__getitem__('id'))
            serilaizer = ProductsSerializer(product, many=True)
            return Response(serilaizer.data)

        product = Products.objects.filter(user_id=pk)
        serilaizer = ProductsSerializer(product, many=True)

        return Response(serilaizer.data)

    def post(self, request, pk):
        serializer = ProductsSerializer(
            context={'request': request}, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request, pk):
        toUpdateProduct = Products.objects.filter(
            user_id=pk, id=request.query_params.__getitem__('id')).first()
        serializer = ProductsSerializer(toUpdateProduct,
                                        context={'request': request}, data=request.data)
        if serializer.is_valid():
            id = request.query_params.get('id')
            serializer.save()
            return Response({'message': f'updated{id} post'})
        return Response(serializer.errors)

    def delete(self, request, pk):
        id = request.query_params.__getitem__('id')
        toDeleteProduct = toUpdateProduct = Products.objects.filter(
            user_id=pk, id=id).first()
        toDeleteProduct.delete()
        return Response({'massage': f'successfully deleted {id}'})
