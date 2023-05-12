from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product
from django.urls import reverse


def add_to_cart(request, product_id):
    if 'cart' not in request.session:
        request.session['cart'] = {}
    key = str(product_id)
    if key in request.session['cart']:
        request.session['cart'][key] += 1
    else:
        request.session['cart'][key] = 1
    request.session.modified = True
    messages.success(request, 'Product added to cart')
    print(request.session['cart'])

    return redirect(reverse('view_cart'))



def view_cart(request):
    cart_items = []
    total_price = 0
    if 'cart' in request.session:
        for item_id, quantity in request.session['cart'].items():
            item = Product.objects.get(id=item_id)
            cart_items.append({'product': item, 'quantity': quantity})
            total_price += item.price * quantity
    context = {'cart_items': cart_items, 'total_price': total_price}
    return render(request, 'cart/cart.html', context)



def remove_from_cart(request, product_id):
    if 'cart' in request.session:
        key = str(product_id)
        if key in request.session['cart']:
            if request.session['cart'][key] == 1:
                del request.session['cart'][key]
            else:
                request.session['cart'][key] -= 1
            request.session.modified = True
            messages.success(request, 'Product removed from cart')
    return redirect(reverse('view_cart'))


def clear_cart(request):
    if 'cart' in request.session:
        del request.session['cart']
        messages.success(request, 'Cart cleared!')
    return redirect(reverse('view_cart'))