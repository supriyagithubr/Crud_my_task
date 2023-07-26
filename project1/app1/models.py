from django.db import models

# Create your models here.
class Order(models.Model):
    o_id = models.IntegerField()
    name = models.CharField(max_length=60)
    o_price = models.FloatField()
    o_date = models.DateTimeField()
    product = models.CharField(max_length=60)
    #phone = models.IntegerField()
    add = models.CharField(max_length=60)


    def __str__(self):
         return f'{self.id}----{self.o_id}----{self.name}---{self.o_price}---{self.o_date}---{self.product}---{self.add}'


