from django.urls import path
from .import views

urlpatterns = [
    path('', views.profile, name='checkout'),
    path('payment/', views.payment, name='payment'),
    path('order_summary/', views.summary, name='order-summary'),
    path('order_confirmed/', views.create_order, name='confirm-order'),
]