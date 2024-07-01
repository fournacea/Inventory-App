from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128)
    sku =  models.CharField(max_length=64, unique=True)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name
    