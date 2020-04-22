from django.urls import path, include
from .api import ServiceViewSet
from knox import views as knox_views

urlpatterns = [
    path('auth', include('knox.urls')),
    path('productsList', ServiceViewSet.as_view()),
   
]   