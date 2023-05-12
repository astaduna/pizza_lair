from django.urls import path
from .import views

urlpatterns = [
    path('', views.profile, name='checkout'),
    path('payment/', views.payment, name='payment'),
    path('order_summary/', views.summary, name='order-summary'),
    path('order_confirmed/unpayed/', views.create_order_unpayed, name='confirm-unpayed-order'),
    path('order_confirmed/payed/', views.create_order_payed, name='confirm-payed-order'),

]