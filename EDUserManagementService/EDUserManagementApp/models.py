from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Additional fields for the User model
    date_of_birth = models.DateField(null=True, blank=True)
    phn = models.CharField(max_length=20, null=True, blank=True)  # Personal Health Number
    address = models.CharField(max_length=255, null=True, blank=True)

    # Add other fields relevant to your personal health application here

    # Specify related_name for the groups and user_permissions fields
    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name="Groups",
        blank=True,
        related_name="custom_user_set"  # Use a custom related_name
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name="User permissions",
        blank=True,
        related_name="custom_user_set"  # Use a custom related_name
    )
