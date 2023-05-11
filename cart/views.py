from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product

def index(request):
    context = {'Product': Product.objects.all().order_by('id')}
    return render(request, 'cart/cart.html', context)


def add_to_cart(request, product_id):
    if 'cart' not in request.session:
        request.session['cart'] = []
    request.session['cart'].append(product_id)
    request.session.modified = True
    messages.success(request, 'Product added to cart')

    # Fetch the product that was just added to the cart
    product = Product.objects.get(id=product_id)

    # Fetch all items in the cart
    cart_items = []
    for item_id in request.session['cart']:
        item = Product.objects.get(id=item_id)
        cart_items.append(item)

    context = {'cartitems': cart_items, 'added_product': product}
    return render(request, 'cart/cart.html', context)
def view_cart(request):
    cart = request.session.get('cart', [])
    products_in_cart = []
    for prod_id in cart:
        prod = Product.objects.get(id=prod_id)
        products_in_cart.append(prod)
    context = {'cartitems': products_in_cart}
    return render(request, 'cart/cart.html', context)


def remove_from_cart(request, product_id):
    if 'cart' not in request.session:
        return redirect('view_cart')
    try:
        request.session['cart'].remove(product_id)
        messages.success(request, 'Product removed from cart')
    except ValueError:
        pass
    return redirect('view_cart')


def clear_cart(request):
    if 'cart' in request.session:
        del request.session['cart']
        messages.success(request, 'Cart cleared!')
    return redirect('view_cart')