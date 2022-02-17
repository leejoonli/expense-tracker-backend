from django.db import models
from django.contrib.auth.models import AbstractUser

# Had an error with migrating user model
# Probably had to do with previous migration not having a user model
# https://stackoverflow.com/questions/42794212/migrating-from-django-user-model-to-a-custom-user-model
# followed along this stackoverflow answer and resolved the problem

# Create your models here.
class User(AbstractUser):
    email = models.EmailField( verbose_name='email', max_length=255, unique=True)
    avatar = models.CharField(max_length=500)
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email