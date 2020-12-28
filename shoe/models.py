from django.db import models

# Create your models here.
class Shoe(models.Model):
   shoe_id = models.AutoField(auto_created=True, primary_key=True)
   description = models.CharField(max_length=100)
   image = models.FileField(upload_to="img/shoe/")

   class Meta:
       db_table = "shoe"
