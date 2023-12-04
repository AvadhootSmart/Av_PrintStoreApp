from django.contrib import admin
from django.urls import path, include
from Shop import views

urlpatterns = [
    path("",views.Home, name="Home"),
    path("checkout/",views.checkout, name="checkout"),
]
