from django.db import models

# Create your models here.
class Product(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=50,null=False,unique=True)
	
class Cart(models.Model):
    id=models.AutoField(primary_key=True)
    person=models.CharField(max_length=50,null=False)
    productid=models.ForeignKey(Product,on_delete=models.CASCADE)
    qty=models.IntegerField()
