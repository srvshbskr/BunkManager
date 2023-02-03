from django.db import models
from django.contrib.auth.models import AbstractUser

class Student(models.Model):

    def __str__(self):
        pass
    
    register_no = models.IntegerField()
