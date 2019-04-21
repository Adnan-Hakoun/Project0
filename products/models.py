from django.db import models
from makers.models import Maker



class Product(models.Model):
    title=    models.CharField(max_length=120)
    price=    models.DecimalField(decimal_places=2,max_digits=1000)
    maker=    models.ForeignKey(Maker,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
