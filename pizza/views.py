from django.shortcuts import render, get_object_or_404
from pizza.models import Pizza
from django.http import JsonResponse


def index(request):
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

        } for x in Pizza.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': pizzas})

    context = {'pizzas': Pizza.objects.all().order_by('id')}
    return render(request, 'pizza/pizza_menu.html', context)


def get_pizza_by_id(request, id):
    return render(request, 'pizza/pizza_detail.html', {
        'pizza': get_object_or_404(Pizza, pk=id)
    })
