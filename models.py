from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User,AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()



from random import choice

class Profile_Reg(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address = models.CharField(_('Address'), max_length=50, blank=True, null=True)
    city = models.CharField(_('City'), max_length=40, blank=True, null=True)
    post = models.CharField(_('ZIP'), max_length=40, blank=True, null=True)
    token = models.CharField(_('Token'), max_length=15, unique=True, db_index=True, null=True)
    subscribed = models.CharField(_('Subscribed or not'), max_length=2, blank=True, null=True)

    def set_token(self):

                self.token = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(15)])

    def save(self, *args, **kwargs):
        super(Profile_Reg, self).save(*args, **kwargs)
        self.set_token()
