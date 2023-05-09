from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='pizza-index'),
    path('type/<int:type_id>', views.get_pizza_by_type, name='pizza-by-type'),
    path('<int:id>', views.get_pizza_by_id, name='pizza-details')

]