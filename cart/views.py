from django.shortcuts import render

from .models import Product

# Create your views here.

def index(request):
    context = {'Product': Product.objects.all()}
    return render(request, 'cart/cart.html', context)


