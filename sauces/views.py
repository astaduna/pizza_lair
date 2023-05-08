from django.shortcuts import render
from sauces.models import Sauce

def index(request):
    context = {'sauces': Sauce.objects.all().order_by('id')}
    return render(request, 'sauces/sauce_menu.html', context)