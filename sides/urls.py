from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='sides-index'),
    path('<int:id>', views.get_sides_by_id, name='sides-details'),

]