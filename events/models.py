from django.db import models
from products.models import Product
from django.contrib.auth.models import User


class Event(models.Model):
    type=       models.CharField(max_length=20,choices=(('add','add'),('buy','buy'),('sell','sell')))
    date=       models.DateTimeField(auto_now=True,auto_now_add=False)
    product=    models.ForeignKey(Product,on_delete=models.CASCADE)
    source=     models.ForeignKey(User,related_name='source',on_delete=models.CASCADE)
    destination=models.ForeignKey(User,related_name='destination',on_delete=models.CASCADE,default=None,null=True)



    def __str__(self):
        return self.type
