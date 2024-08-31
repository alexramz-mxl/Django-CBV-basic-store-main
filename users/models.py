from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class MembershipCard(models.Model):
    MEMBERSHIP_TYPES = [
        ('Standard', 'Standard'),
        ('Premium', 'Premium'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    membership_number = models.CharField(max_length=20, unique=True)
    profile_photo = models.ImageField(upload_to='profile_photos/')
    membership_type = models.CharField(max_length=10, choices=MEMBERSHIP_TYPES)
    benefits = models.TextField()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.membership_type})'