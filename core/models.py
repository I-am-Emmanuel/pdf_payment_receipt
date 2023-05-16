from django.db import models
from  django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth.models import AbstractUser
import uuid
from . managers import UserModelManager
# Create your models here.

class UserModel(AbstractUser):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    
    username=None
    
    password = models.CharField(max_length=250, validators = [MinLengthValidator(7, message='Your password is too short! Minimum of 8 length is required')])
    
    def __str__(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserModelManager()



    
    