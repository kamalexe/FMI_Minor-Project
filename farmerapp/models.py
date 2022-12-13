from django.db import models
from fmiapp.models import FarmerInfo,MerchantInfo
from merchantapp.models import orderDetail
from datetime import datetime

# Create your models here.
class Profile(models.Model):
    farmerName = models.OneToOneField(FarmerInfo,on_delete = models.CASCADE, default="")

class FarmerSellProduct(models.Model):
    farmerName = models.ForeignKey(FarmerInfo,on_delete = models.CASCADE, related_name="farmers", default="")
    productName = models.CharField(max_length=100, default="")
    qty = models.CharField(max_length=100, default="")
    price = models.CharField(max_length=100, default="")
    description = models.TextField(max_length=100, default="")
    prodImage = models.ImageField(upload_to='images/')
    likes = models.ManyToManyField(MerchantInfo, related_name='FarmerSellProduct')

    def total_likes(self):
        return self.likes.count()
        
    def __str__(self):
        return self.productName

class Tracker(models.Model):
    orderId = models.ForeignKey(orderDetail,on_delete = models.CASCADE)
    orderStatus = models.CharField(max_length=100, default="Your Order has been placed")
    updateDate = models.DateTimeField(default=datetime.now(), blank=True)
    def __str__(self):
        return str(self.orderId)