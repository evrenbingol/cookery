from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserAccountManager(BaseUserManager):

  def create_user(self, email, password=None, **kwargs):
    if not email:
        raise ValueError('Users must have an email address')
    
    now = timezone.now()
    email = self.normalize_email(email).lower()

    user = self.model(
        email=email,
        last_login=now,
        date_joined=now, 
        **kwargs
    )
    user.set_password(password)
    user.save(using=self._db)
    return user


  def create_superuser(self, email, password, **extra_fields):
    user=self.create_user(email, password, **extra_fields)
    user.is_staff=True
    user.is_superuser=True
    user.save(using=self._db)
    return user



class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    
    

    is_teacher = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    

    USERNAME_FIELD = 'email'
   

    objects = UserAccountManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)
