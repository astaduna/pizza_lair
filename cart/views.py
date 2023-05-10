from django.shortcuts import render, redirect
from .models import Cart
from .models import Product

# Create your views here.

def index(request):
    context = {'Product': Product.objects.all()}
    return render(request, 'cart/cart.html', context)

def add_to_cart_pizza(request):
    product_id = request.GET.get('prod_id')
    product_name = Product.objects.get(id=product_id)
    product = Product.objects.filter(id=product_id)
    for p in product:
        price = p.price
        Cart(product=product_name, price=price).save()
        return redirect('pizza/pizza_menu.html')

def add_to_cart_side(request):
    product_id = request.GET.get('prod_id')
    product_name = Product.objects.get(id=product_id)
    product = Product.objects.filter(id=product_id)
    for p in product:
        price = p.price
        Cart(product=product_name, price=price).save()
        return redirect('sides/side_menu.html')

def add_to_cart_drink(request):
    product_id = request.GET.get('prod_id')
    product_name = Product.objects.get(id=product_id)
    product = Product.objects.filter(id=product_id)
    for p in product:
        price = p.price
        Cart(product=product_name, price=price).save()
        return redirect('drinks/drink_menu.html')


def add_to_cart_sauce(request):
    product_id = request.GET.get('prod_id')
    product_name = Product.objects.get(id=product_id)
    product = Product.objects.filter(id=product_id)
    for p in product:
        price = p.price
        Cart(product=product_name, price=price).save()
        return redirect('sauces/sauce_menu.html')


def add_to_cart_offer(request):
    product_id = request.GET.get('prod_id')
    product_name = Product.objects.get(id=product_id)
    product = Product.objects.filter(id=product_id)
    for p in product:
        price = p.price
        Cart(product=product_name, price=price).save()
        return redirect('offers/offer_menu.html')


def show_cart(request):
    return render(request, 'cart/cart.html')