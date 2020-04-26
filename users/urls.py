from django.urls import path, include
from .api import RegisterAPI, LoginAPI, ProfileViewSet
from knox import views as knox_views

urlpatterns = [
    path('auth', include('knox.urls')),
    path('register', RegisterAPI.as_view()),
    path('login', LoginAPI.as_view()),
    path('profile', ProfileViewSet.as_view()),
    path('profile/<int:pk>', ProfileViewSet.as_view())
]   