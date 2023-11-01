from django.db import models

# Create your models here.
class TypeUser(models.Model):
    name=models.CharField(max_length=255, unique=True)