from django.db import models

# Create your models here.
class User(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    pwd=models.CharField(max_length=200)
    userType=models.CharField(max_length=100)

    def __str__(self):
        return self.name

