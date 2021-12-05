from django.db import models
from django.contrib.auth.models import AbstractUser

# user 모델  커스텀  
class User(AbstractUser):
    # email 로그인을 위한 user 모델 커스텀 
    username = None
    email = models.EmailField(('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email