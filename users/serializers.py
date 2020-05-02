from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        depth = 1


class UserRegistration(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        depth = 1

    def create(self, validate_date):
        user = User.objects.create_user(
            validate_date['username'], validate_date['email'], validate_date['password'])
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentails')

# profile


class ProfileSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(source='profile.id')
    user_id = serializers.IntegerField(source='user.id')
    user = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())
    profile = Profile
    # depth=2

    class Meta:
        model = Profile
        fields = ('id', 'user', 'image', 'first_name', 'last_name',
                  'description', 'mobile', 'current_location', 'user_id')
        read_only_fields = ('user', 'user_id')

        # def create(self, validated_data):
        #     # user_id = validated_data.pop('user_id')
        #     user = User.objects.filter(user_id=user_id).first()
        #     user_profile = profile.objects.get(pk=validated_data.get('id'))
        #     print('user_profile', user_profile)
        #     user_profile.image = validated_data.get('image'),
        #     user_profile.first_name = validated_data.get(
        #         'first_name'),
        #     user_profile.last_name = validated_data.get(
        #         'last_name'),
        #     user_profile.description = validated_data.get(
        #         'description'),
        #     user_profile.mobile = validated_data.get(
        #         'mobile'),
        #     user_profile.current_location = validated_data.get(
        #         'current_location'),
        #     user_profile.user_id = validated_data.get('user_id')
        #     return user_profile.save()

        def update(self, instance, validate_date):
            instance.image = validate_date.get('image', instance.image)
            instance.first_name = validate_date.get(
                'first_name', instance.first_name)
            instance.last_name = validate_date.get(
                'last_name', instance.last_name)
            instance.description = validate_date.get(
                'description', instance.description)
            instance.current_location = validate_date.get(
                'current_location', instance.current_location)
            instance.save()
            return instance
