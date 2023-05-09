from django.shortcuts import render, get_object_or_404
from pizza.models import Pizza, PizzaType
from django.http import JsonResponse


def index(request):
    order_by = request.GET.get('order_by', 'name')

    if order_by == 'name':
        pizzas = Pizza.objects.all().order_by('name')
    elif order_by == 'high_price':
        pizzas = Pizza.objects.all().order_by('-large_price')
    elif order_by == 'low_price':
        pizzas = Pizza.objects.all().order_by('large_price')
    else:
        pizzas = Pizza.objects.all().order_by('id')

    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        pizzas = [{
            'id': x.id,
            'name': x.name,
            'toppings': x.toppings,
            'descriptions': x.descriptions,
            'small_price': x.small_price,
            'medium_price': x.medium_price,
            'large_price': x.large_price,
            'firstImage': x.pizzaimage_set.first().image

        } for x in pizzas.filter(name__icontains=search_filter)]
        return JsonResponse({'data': pizzas})

    context = {
        'pizzas': pizzas,
        'order_by': order_by
    }
    return render(request, 'pizza/pizza_menu.html', context)
def get_pizza_by_id(request, id):
    return render(request, 'pizza/pizza_detail.html', {
        'pizza': get_object_or_404(Pizza, pk=id)
    })


def get_pizza_by_type(request, type_id):
    if type_id:
        pizzas = Pizza.objects.filter(type__id=type_id)
    else:
        pizzas = Pizza.objects.all()
    context = {
        'pizzas': pizzas,
        'pizza_types': PizzaType.objects.all(),
    }
    return render(request, 'pizza/pizza_menu.html', context)
