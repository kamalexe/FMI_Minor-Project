from django.db import models
from datetime import datetime

class LoginInfo(models.Model):
    userid = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=20)
    usertype = models.CharField(max_length=50, default="admin")
    def __str__(self):
        return self.userid


# Create your models here.
class FarmerInfo(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    address = models.TextField()
    contactno = models.CharField(max_length=15)
    aadharno = models.CharField(max_length=12, primary_key=True)
    regdate = models.DateTimeField(default=datetime.now, blank=True)
    #     Login Update
    userid = models.CharField(max_length=50, default="", unique=True)
    password = models.CharField(max_length=20, default="")
    usertype = models.CharField(max_length=20, default="farmer")

    def __str__(self):
        return self.aadharno


class MerchantInfo(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    firmname = models.CharField(max_length=100)
    firmaddress = models.TextField()
    contactno = models.CharField(max_length=15)
    aadharno = models.CharField(max_length=12, primary_key=True)
    panno = models.CharField(max_length=10)
    gstno = models.CharField(max_length=15)
    regdate = models.DateTimeField(default=datetime.now, blank=True)

    userid = models.CharField(max_length=50, default="", unique=True)
    password = models.CharField(max_length=20, default="")
    usertype = models.CharField(max_length=20, default="merchant")

    def __str__(self):
        return self.aadharno


class Enquiry(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    address = models.TextField()
    contactno = models.CharField(max_length=15)
    emailaddress = models.EmailField(max_length=50)
    enquirytext = models.TextField()
    enquirydate = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.enquirydate
