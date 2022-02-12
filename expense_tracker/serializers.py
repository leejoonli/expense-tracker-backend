from rest_framework import serializers
from .models import Expense

class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    expense = serializers.HyperlinkedRelatedField(view_name='expense_detail', read_only=True)
    
    class Meta:
       model = Expense
       fields = ('id', 'name', 'amount', 'category', 'date', 'expense')
