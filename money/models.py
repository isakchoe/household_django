from django.db import models
from django.conf import settings
from django.db.models.fields import DateTimeField

# Create your models here.
class FinancialMemo(models.Model):
    
    # 사용자, 사용금액, 메모글   
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    revenue = models.IntegerField()
    expense = models.IntegerField()
    comment = models.TextField(max_length = 30)
    is_deleted = models.BooleanField(default = False)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True) 
    