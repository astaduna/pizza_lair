from django.urls import path
from .import views

urlpatterns = [
    path('', views.profile, name='checkout'),
    path('phase_2/', views.payment, name='payment')
]