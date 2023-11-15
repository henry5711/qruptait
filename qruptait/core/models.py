from django.db import models

# Create your models here.
class TypeUser(models.Model):
    name=models.CharField(max_length=255, unique=True)
    

class User(models.Model):
    ci=models.IntegerField(unique=True)
    name1=models.CharField(max_length=254)
    name2=models.CharField(max_length=255)
    
    lastname1=models.CharField(max_length=255)
    lastname2=models.CharField(max_length=255)
    user=models.ForeignKey(TypeUser,on_delete=models.CASCADE)
    

class Asistence(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   asistence=models.DateTimeField()