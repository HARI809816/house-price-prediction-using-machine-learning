from django.urls import path
from .views import *

urlpatterns=[
    path('home/',HomePage),
    path('predict/', predict_price, name='predict_price'), 
]