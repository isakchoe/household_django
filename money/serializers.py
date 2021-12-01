
from rest_framework import serializers
from .models import FinancialMemo


class FinancialMemoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FinancialMemo
        fields = ('id', 'money', 'comment', 'is_deleted')