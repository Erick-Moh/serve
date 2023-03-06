import re
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


def validate_phone(value: str) -> None:
    '''
    ensures the correct number formats
    for kenya
    '''
    if not re.compile(r'^0(7|1)\d{8}$|^\+?254(7|1)\d{8}$')\
        .match(value):
        raise ValidationError('Invalid phone number!', params={'value': value})
    

class CustomUser(AbstractUser):
    '''
    creating a customized user model
    to adding phone number and 
    email
    '''
    phone_number = models.CharField(max_length=50, validators=[validate_phone,], unique=True)
    email = models.EmailField(unique=True)
