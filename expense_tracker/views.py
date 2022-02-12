from rest_framework import generics
from .serializers import ExpenseSerializer
from .models import Expense
from rest_framework import permissions
from expense_tracker.permissions import IsOwnerOrReadOnly

class ExpenseList(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # overwrite create method
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsOwnerOrReadOnly]
