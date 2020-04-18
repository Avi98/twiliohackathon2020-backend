from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ('id', 'username', 'email')

class UserRegistration(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validate_date):
        user = User.objects.create_user(validate_date['username'], validate_date['email'], validate_date['password'])
        return user 

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentails')

#profile

class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id')
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    profile=Profile
    # depth=2
    class Meta:
        model = Profile
        fields= ('user','image', 'first_name', 'last_name', 'description','mobile', 'current_location','user_id')
        read_only_fields=('user','user_id')

        def create(self,validated_data):
            user_id = validated_data.pop('user_id')
            user = User.objects.create(user_id=user_id)
            profile = Profile.objects.create(**validated_data)
            return profile
