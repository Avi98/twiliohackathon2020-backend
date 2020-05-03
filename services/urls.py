from django.urls import path, include
from .api import ServiceViewSet, ProductsViewSet, CommentsViewSet
from knox import views as knox_views

urlpatterns = [
    path('auth', include('knox.urls')),
    path('products', ServiceViewSet.as_view()),
    path('product/<int:pk>', ProductsViewSet.as_view()),
    path('comments', CommentsViewSet.as_view()),
]   