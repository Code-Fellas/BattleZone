from django.db import models
from django.core.validators import validate_email

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=255, default=None)
    last_name = models.CharField(max_length=255, default=None)
    email = models.CharField(max_length=255, validators=[validate_email])
    mobile_number = models.CharField(max_length=11)
    password = models.CharField(max_length=255, default=None)
    sex = models.CharField(max_length=10)
    current_year = models.IntegerField(default=0)
    current_university = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
