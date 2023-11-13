from rest_framework import serializers
from .models import CustomUser

class CustomUserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class CustomUserPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'phn', 'address']

    def create(self, validated_data):
        ## Custom validation would go here
        return CustomUser.objects.create(**validated_data)

class CustomUserPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'