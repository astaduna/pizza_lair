from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('clear/', views.clear_cart, name='clear_cart'),
    path('update_cart/<int:product_id>/', views.update_cart, name='update_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
]
