from django.urls import path
from . import views

urlpatterns = [
    path('', views.merchanthome, name='merchanthome'),
    path('viewProd/<str:id>', views.viewProd, name='viewProd'),
    path('viewProd/placeorder/<str:id>', views.placeorder, name='placeorder'),
    path('purchaseCustomerDetail', views.purchaseCustomerDetail, name='purchaseCustomerDetail'),
    path('purchasedprod', views.purchasedprod, name='purchasedprod'),
    path('logout', views.logout, name='logout'),
    path('trackOrder', views.trackOrder, name='trackOrder'),
    path('viewProd/like_post/<str:id>', views.LikeView, name='LikeView'),
]
