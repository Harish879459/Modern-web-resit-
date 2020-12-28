from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(auto_created=True, primary_key=True)
    username = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default='')
    contact = models.CharField(max_length=100)

    class Meta:
        db_table = "customer"
