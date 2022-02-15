from django.shortcuts import render
# from rest_framework import generics, permissions
# from .serializers import UserCreateSerializer
# from .models import User
# from expense_tracker.permissions import IsOwnerOrReadOnly

# # Create your views here.
# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserCreateSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         """
#         This view should return a list of all the purchases
#         for the currently authenticated user.
#         """
#         user = self.request.user
#         return User.objects.filter(username=user)