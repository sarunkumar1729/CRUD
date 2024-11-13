from django.db import models

class Products(models.Model):
      name = models.CharField(max_length=50)
      price = models.IntegerField()
      quantity = models.IntegerField()
      image = models.ImageField(upload_to='images/')
      
