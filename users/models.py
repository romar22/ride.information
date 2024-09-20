from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    ADMIN = 'admin'
    DRIVER = 'driver'
    RIDER = 'rider'
    ROLES = (
        (ADMIN, 'Admin'),
        (DRIVER, 'Driver'),
        (RIDER, 'Rider')
    )

    user_id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=10, choices=ROLES, default=ADMIN)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=20)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("first_name", "last_name")

    def __str__(self):
        return f"{self.email}"