from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminhome, name='adminhome'),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('enquiries/', views.enquiries, name='enquiries'),
    path('booking/', views.booking, name='booking'),
    path('purchase/', views.purchase, name='purchase'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('logout/', views.logout, name='logout'),
    path('book/<str:ano>', views.book, name='book'),
    path('pbook/', views.pbook, name='pbook'),
    path('viewbook/<str:ano>', views.viewbook, name='viewbook'),
    path('deleteenq/<str:id>', views.deleteenq, name='deleteenq'),
    path('addnews/', views.addnews, name='addnews'),
    path('deletenews/<str:id>', views.deletenews, name='deletenews'),
    path('changepwd/', views.changepwd, name='changepwd'),
    path('pay/<str:ano>', views.pay, name='pay'),
    path('paid/', views.paid, name='paid'),
    path('sellingitems/', views.sellingitems, name='sellingitems'),
    path('solditem/', views.solditem, name='solditem'),
    path('downAllProdList/', views.downAllProdList, name='downAllProdList'),

]
