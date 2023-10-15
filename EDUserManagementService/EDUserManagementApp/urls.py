from django.urls import path

from . import views
from .views import GetUserById

urlpatterns = [
    path('user/<int:pk>/', GetUserById.as_view(), name='get-user-by-id'),
    path("", views.index, name="index"),
]