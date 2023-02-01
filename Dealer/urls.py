from django.urls import path
from .views import dashboard,dealerRegister

urlpatterns=[
    path('dashboard/',dashboard,name='dashboard'),
    path('dealerregister',dealerRegister,name='dealerRegister')
    ]
    
