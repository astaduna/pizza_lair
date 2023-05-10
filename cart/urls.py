
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='cart-index'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart')
]