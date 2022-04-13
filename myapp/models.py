from email.policy import default
from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User



class Title(models.Model):
    name = models.CharField(max_length=100, default="Genric Title")
    href = models.CharField(max_length=500, default='#')
    
class Post(models.Model):
    title = models.CharField(max_length=100, default="Title")
    body = models.CharField(max_length=100000, default="Body text here")
    created = models.DateTimeField(default=datetime.now, blank=True)

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField()
    gender = models.CharField(
        max_length=6, 
        choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')]
        )
    def __str___(self):
        return self.user.username
