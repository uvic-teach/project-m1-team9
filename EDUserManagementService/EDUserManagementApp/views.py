from django.http import HttpResponse
from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer

class GetUserById(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'pk'  # This tells Django to use 'pk' as the lookup field

    # Optionally, you can add authentication and permission classes here

def index(request):
    return HttpResponse("Hello, world. You're at the EDUserManagementApp index.")