from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    image = models.CharField(max_length=254, default='')
    

    def __str__(self):
        return self.name



# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.CharField(max_length=254, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name
