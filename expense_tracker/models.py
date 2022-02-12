from django.db import models

# Create your models here.
class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    category = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=False)
    owner = models.ForeignKey('users.User', related_name='expenses', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
