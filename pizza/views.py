from django.shortcuts import render, get_object_or_404
from pizza.models import Pizza


def index(request):
    context = {'pizzas': Pizza.objects.all().order_by('id')}
    return render(request, 'pizza/pizza_menu.html', context)



def get_pizza_by_id(request, id):
    return render(request, 'pizza/pizza_detail.html', {
        'pizza': get_object_or_404(Pizza, pk=id)
    })
