from django.db import models
class Product(models.Model):
    item=models.CharField(max_length=100)
    image=models.CharField(max_length=500)
    price=models.IntegerField(max_length=10)
    def __str__(self):
        return self.item