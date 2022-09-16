from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def _create(self, username, first_name, last_name, email, password, is_staff, is_admin, is_superuser, **extra_fields):
        if not username:
            raise ValueError("User Must have a Username")
        if not email:
            raise ValueError("User Must Have an Email Adress")
        
        extra_fields.setdefault('is_active', True)

        email = self.normalize_email(email)
        user = self.model(username = username, email = email)

        user.first_name = first_name
        user.last_name = last_name

        user.is_staff = is_staff
        user.is_admin = is_admin
        user.is_superuser = is_superuser

        user.set_password(password)

        user.save()

        return user
    
    def create_user(self, username, first_name, last_name, email, password, is_staff = True, is_admin = False, is_superuser = False, **extra_fields):
        return self._create(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = password,
            is_staff = is_staff,
            is_admin = is_admin,
            is_superuser = is_superuser,
            **extra_fields
        )

    def create_superuser(self, username, first_name, last_name, email, password, is_staff = True, is_admin = True, is_superuser = True, **extra_fields):
        return self._create(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = password,
            is_staff = is_staff,
            is_admin = is_admin,
            is_superuser = is_superuser,
            **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):

    username        = models.CharField(max_length=255, unique=True, blank=False, null=False)
    first_name      = models.CharField(max_length=255, blank=True, null=True)
    last_name       = models.CharField(max_length=255, blank=True, null=True)
    email           = models.EmailField(unique=True)
    password        = models.CharField(max_length=255)
    
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created_at      = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
    
    
