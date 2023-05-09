from django.shortcuts import render
from drinks.models import Drink


def index(request):
    context = {'drinks': Drink.objects.all().order_by('id')}
    return render(request, 'drinks/drinks_menu.html', context)
