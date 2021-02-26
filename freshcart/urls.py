from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index' ),
    path('cart/',views.cart,name='cart' ),
    path('addcart/',views.addcart,name='addcart' ),

]