from django.db import models
from shoe.models import Shoe
from customer.models import Customer
# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(auto_created=True, primary_key=True)
    shoe=models.ForeignKey(Shoe,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    time=models.CharField(max_length=20)
    date=models.CharField(max_length=10)
    class Meta:
        db_table = "order"
