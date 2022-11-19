from django.db import models

# Create your models here.
class orderDetail(models.Model):
    email = models.CharField(max_length=100, default="")
    track_update = models.CharField(max_length=600, default="Your Order has been placed")
    customer = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=150, default="")
    panno = models.CharField(max_length=10, default="")
    gstno = models.CharField(max_length=15, default="")
    productid = models.CharField(max_length=150, default="")
    product = models.CharField(max_length=150, default="")
    qty = models.CharField(max_length=10, default="")
    price = models.CharField(max_length=12, default="")
    city = models.CharField(max_length=30, default="")
    state = models.CharField(max_length=30, default="")
    zip = models.CharField(max_length=10, default="")
    merchantName = models.CharField(max_length=10, default="")
    merchantId = models.CharField(max_length=10, default="")
    farmerName = models.CharField(max_length=10, default="")
    farmerId = models.CharField(max_length=10, default="")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product
