from django.db import models
from django.conf import settings

# Create your models here.
class FinancialMemo(models.Model):
    
    # 사용자, 사용금액, 메모글   
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    money = models.IntegerField()
    comment = models.TextField(max_length = 30)
    is_deleted = False
    