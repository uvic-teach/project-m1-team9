from django.urls import path

from . import views
from .views import GetUserById, UpdateUserById, CreateUser

urlpatterns = [
    path("", views.index, name="index"),
    path('user/<int:pk>/', GetUserById.as_view(), name='get-user-by-id'),
    path('user/<int:pk>/update/', UpdateUserById.as_view(), name='update-user-by-id'),
    path('user/create/', CreateUser.as_view(), name='create-user'),
]