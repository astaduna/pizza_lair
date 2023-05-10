from django.shortcuts import render, redirect
from .models import Cart
from .models import Product

# Create your views here.

def index(request):
    context = {'Product': Product.objects.all().order_by('id')}
    return render(request, 'cart/cart.html', context)

def add_to_cart(request):
    product_id = request.GET.get('prod_id')
    product_name = Product.objects.get(id=product_id)
    product = Product.objects.filter(id=product_id)
    for p in product:
        price = p.price
        Cart(product=product_name, price=price).save()
        return redirect('pizza/pizza_menu.html')
