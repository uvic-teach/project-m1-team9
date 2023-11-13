from django.http import HttpResponse
from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserGetSerializer, CustomUserPatchSerializer, CustomUserPutSerializer

class GetUserById(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserGetSerializer
    lookup_field = 'pk'  # This tells Django to use 'pk' as the lookup field

    # Optionally, you can add authentication and permission classes here

class GetUserByPhn(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserGetSerializer
    lookup_field = 'phn'  # This tells Django to use 'phn' as the lookup field

    # Optionally, you can add authentication and permission classes here

class UpdateUserById(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserPatchSerializer

class CreateUser(generics.CreateAPIView):
    serializer_class = CustomUserPutSerializer

    # Optionally, you can add authentication and permission classes here

def index(request):
    return HttpResponse("Hello, world. You're at the EDUserManagementApp index.")