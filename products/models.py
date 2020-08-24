from django.db import models

# Create your models here.
class product(models.Model):
    name =models.CharField(max_length=30)
    price=models.FloatField(max_length=20)
    image=models.CharField(max_length=8000)

