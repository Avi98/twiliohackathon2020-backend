from rest_framework import generics
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, UserRegistration, LoginSerializer,  ProfileSerializer
from .models import Profile
from django.contrib.auth.models import User
from rest_framework import viewsets
from knox.auth import TokenAuthentication
from django.shortcuts import get_object_or_404
# registration


class RegisterAPI(generics.GenericAPIView):
    serializer_class = UserRegistration
    print('api')

    def post(self, request, *args, **kwargs):
        print('Post ')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        _, token = AuthToken.objects.create(user)
        return Response({
            "user": UserSerializer(user,
                                   context=self.get_serializer_context()).data,
            'token': token
        })

# Login API


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        _, token = AuthToken.objects.create(user)
        print()
        return Response({
            "user": UserSerializer(user,
                                   context=self.get_serializer_context()).data,
            'token': token,
            # 'profile': ProfileSerializer(User.objects.all().filter(username='Avinash').first().profile).data
        })


# create and update profile api
class ProfileViewSet(APIView):
    # to find if isAuthenticate then
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]

    def get(self,  request):
        serializer = ProfileSerializer(request.user.profile)
        return Response({
            'profile': serializer.data
        })

    def post(self, request):
        serializer = ProfileSerializer(
            context={'request': request}, data=request.data)
        if serializer.is_valid():
            serializer.create(validated_data=request.data)
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request):
        profile = Profile.objects.filter(
            user_id=request.data.get('user_id')).first()
        serializer = ProfileSerializer(
            profile, context={'request': request}, data=request.data)
        if serializer.is_valid():
            serializer.update(instance=profile, validated_data=request.data)
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request):

        profile = Profile.objects.filter(
            user_id=request.data.get('user_id')).first()
        profile.delete()
        id = request.data.get('user_id')
        return Response({'massage': f'successfully deleted {id}'})
