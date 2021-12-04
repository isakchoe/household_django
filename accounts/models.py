from django.db import models
from django.contrib.auth.models import AbstractUser

# user 모델  커스텀  
class User(AbstractUser):
    name = models.CharField(max_length = 50)