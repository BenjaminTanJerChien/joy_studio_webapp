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
    base_body_weight_kg = models.FloatField(default=0)
    base_body_fat_p = models.FloatField(default=0)
    base_visceral_fat = models.FloatField(default=0)
    base_bone_mass_kg = models.FloatField(default=0)
    base_bmr = models.FloatField(default=0)
    base_metabolic_age = models.FloatField(default=0)
    base_muscle_mass_kg = models.FloatField(default=0)
    base_physique_rating = models.FloatField(default=0) 
    base_water = models.FloatField(default=0)
    base_body_fat_kg = models.FloatField(default=0)
    base_muscle_mass_p = models.FloatField(default=0)

    current_body_weight_kg = models.FloatField(default=0)
    current_body_fat_p = models.FloatField(default=0)
    current_visceral_fat = models.FloatField(default=0)
    current_bone_mass_kg = models.FloatField(default=0)
    current_bmr = models.FloatField(default=0)
    current_metabolic_age = models.FloatField(default=0)
    current_muscle_mass_kg = models.FloatField(default=0)
    current_physique_rating = models.FloatField(default=0) 
    current_water = models.FloatField(default=0)
    current_body_fat_kg = models.FloatField(default=0)
    current_muscle_mass_p = models.FloatField(default=0)


    def __str___(self):
        return self.user.username
