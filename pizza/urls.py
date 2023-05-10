from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='pizza-index'),
    path('pizza/type/<int:type_id>/', views.get_pizza_by_type, name='pizza_type'),
    path('<int:id>', views.get_pizza_by_id, name='pizza-details')
]
