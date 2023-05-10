from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='cart-index'),
    path('add_to_cart', views.add_to_cart_pizza, name='add_to_cart'),
    path('add_to_cart', views.add_to_cart_drink, name='add_to_cart'),
    path('add_to_cart', views.add_to_cart_offer, name='add_to_cart'),
    path('add_to_cart', views.add_to_cart_sauce, name='add_to_cart'),
    path('add_to_cart', views.add_to_cart_side, name='add_to_cart')
    path('cart', views.show_cart(), name='cart')
]