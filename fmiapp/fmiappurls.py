import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('farmerreg/', views.farmerreg, name='farmerreg'),
    path('merchentreg/', views.merchentreg, name='merchentreg'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('freg/', views.freg, name='freg'),
    path('mreg/', views.mreg, name='mreg'),
    path('validate/', views.validate, name='validate'),
    path('saveenq/', views.saveenq, name='saveenq'),
]
