from django.contrib import admin
from django.urls import path
from .views import helloworld, hellostudent, increment, reset, decrement

urlpatterns = [
    path('helloworld/', helloworld),
    path('hellostudent/', hellostudent),
    path('increment/', increment),
    path('reset/', reset),
    path('decrement/', decrement)
]
