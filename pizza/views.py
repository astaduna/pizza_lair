from django.shortcuts import render
from pizza.models import Pizza


def index(request):
    context = {'pizzas': Pizza.objects.all().order_by('id')}
    return render(request, 'pizza/pizza_menu.html', context)