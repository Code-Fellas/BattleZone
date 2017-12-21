from django.db import models
from django.core.validators import validate_email
import uuid
# Create your models here.


class Users(models.Model):
    first_name = models.CharField(max_length=255, default=None)
    last_name = models.CharField(max_length=255, default=None)
    username = models.CharField(max_length=100, default=None)
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

    class Meta:
        db_table = 'users'


# Model to store Details about an Access Token.
class Tokens(models.Model):
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    last_request_on = models.DateTimeField(auto_now=True)
    is_valid = models.BooleanField(default=True)

    class Meta:
        db_table = 'tokens'

    def create_token(self):
        self.access_token = uuid.uuid4()
