from django.db import models

# Create your models here.
class allData(models.Model):
    Name=models.CharField(null=True, max_length=50)
    count=models.AutoField(primary_key=True)
    commend=models.TextField(null=True)
    number =models.BigIntegerField(null=True)
    avg=models.DecimalField(null=True, max_digits=5, decimal_places=2)
    set=models.BooleanField(null=True)
    date=models.DateField(null=True, auto_now=False, auto_now_add=False)
    time=models.TimeField(null=True, auto_now=False, auto_now_add=False)
    during=models.DurationField(null=True)
    email=models.EmailField(null=True, max_length=254)
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 
    
class order(models.Model):
    name=models.CharField(null=True, max_length=50)
    orderQty=models.IntegerField(null=True)
    sellQty=models.IntegerField(null=True)
        
