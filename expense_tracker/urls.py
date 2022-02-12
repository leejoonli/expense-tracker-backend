from django.urls import path
from . import views
# from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('expenses/', views.ExpenseList.as_view(), name='expense_list'),
    path('expenses/<int:pk>', views.ExpenseDetail.as_view(), name='expense_detail'),
]
