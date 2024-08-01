from django.db import models
from django.contrib.auth import get_user_model
from users.models import UserAccount
# Create your models here.

class Course(models.Model):
    instructor = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    details = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)