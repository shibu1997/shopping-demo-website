from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name= "Home" ),
    path("about/", views.about, name= "AboutUs" ),
    path("contact/", views.contact, name= "ContactUS" ),
    path("tracker", views.tracker, name= "Tracker" ),
    path("search/", views.search, name= "Search" ),
    path("products/<int:myid>", views.productview, name= "ProductView" ),
    path("checkout/", views.checkout, name= "Checkout" ),
    
    
]