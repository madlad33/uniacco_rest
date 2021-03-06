from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,\
                                PermissionsMixin
from django.conf import settings
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError("Please provide an email")
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password):
        """Creates a new superuser"""
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    """Custom user model that supports email instead of username"""
    email = models.EmailField(max_length=255,blank=False,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'

class UserLoginHistory(models.Model):
    """Model for the user ip addresses history"""
    ip = models.GenericIPAddressField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,)
    def __str__(self):
        return str(self.user)


class UserDetails(models.Model):
    university = models.CharField(max_length=255)
    year_of_study = models.DateField()
    course = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    def __str__(self):
        return self.university

class UserDetailAnother(models.Model):
    university = models.CharField(max_length=255)
    year_of_study = models.DateField()
    course = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.university