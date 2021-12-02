
from rest_framework import serializers
from .models import FinancialMemo


class FinancialMemoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FinancialMemo
        fields = ('id', 'revenue', 'expense',  'comment', 'is_deleted', 'created_at', 'updated_at')