from django.urls import path
from .import views

urlpatterns = [
    path('', views.profile, name='checkout'),
    path('payment/', views.payment, name='payment'),
    path('order_summary/', views.summary, name='confirm-order'),
    path('order_confirmed/unpaid/', views.create_order_unpaid, name='confirm-unpaid-order'),
    path('order_confirmed/paid/', views.create_order_paid, name='confirm-paid-order'),

]
