from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from konverdev import views

urlpatterns = [
    path('product/', views.products),
    path('product_edit/', views.product_edit),
    path('wagon/', views.wagon),
]
