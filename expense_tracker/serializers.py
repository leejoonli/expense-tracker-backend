from rest_framework import serializers
from .models import Expense

class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    expense = serializers.HyperlinkedRelatedField(view_name='expense_detail', read_only=True)

    expense_url = serializers.ModelSerializer.serializer_url_field(view_name='expense_detail')

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
       model = Expense
       fields = ('id', 'name', 'amount', 'category', 'date', 'expense_url', 'expense', 'owner')
