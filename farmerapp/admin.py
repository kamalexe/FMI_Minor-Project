from django.contrib import admin
from .models import FarmerSellProduct,Profile,Tracker
# Register your models here.
admin.site.register(Profile)
admin.site.register(FarmerSellProduct)
admin.site.register(Tracker)