from rest_framework import serializers
from django.contrib.auth.models import User


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['password'])
        return user


class updateProfileSerializer(serializers.Serializer):
    username  = serializers.CharField(max_length=100,required=False)
    first_name = serializers.CharField(max_length=100, required=False)
    last_name = serializers.CharField(max_length=100, required=False)
    business_name = serializers.CharField(max_length=100, required=False)
    gst = serializers.CharField(max_length=100, required=False)
    email = serializers.CharField(max_length=100, required=False)
    mobile = serializers.CharField(max_length=100, required=False,allow_null=True,allow_blank=True)
    password = serializers.CharField(max_length=100, required=False)


class RegProfileSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100,required=False)
    password = serializers.CharField(max_length=100, required=False)
