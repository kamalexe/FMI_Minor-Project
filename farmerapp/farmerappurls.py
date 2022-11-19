from django.urls import path
from . import views

urlpatterns = [
    path('', views.farmerhome, name='farmerhome'),
    path('logout', views.logout, name='logout'),
    path('uploadProd', views.uploadProd, name='uploadProd'),
    path('prodlist', views.prodlist, name='prodlist'),
    path('removeprod/<str:id>', views.removeprod, name='removeprod'),
    path('sold', views.sold, name='sold'),
    path('updateStatus', views.updateStatus, name='updateStatus'),
    path('currentprice', views.currentprice, name='currentprice'),
    path('changepasword/', views.changepasword, name='changepasword'),
    path('changepwd/', views.changepwd, name='changepwd'),
    path('downProdList/', views.downProdList, name='downProdList'),
    path('downSoldProdList/', views.downSoldProdList, name='downSoldProdList'),
]