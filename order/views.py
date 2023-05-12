from django.shortcuts import render, redirect
from order.models import Order, OrderItem
from user.models import Profile
from user.forms.checkout import CheckoutProfileInfo, CheckoutPaymentForm
from django.contrib.auth.decorators import login_required
from cart.models import Product




# Create your views here.
def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = CheckoutProfileInfo(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('checkout')

    return render(request, 'checkout/checkout.html', {
        'form': CheckoutProfileInfo(instance=profile)
    })


def payment(request):
    payment = CheckoutPaymentForm()
    if request.method == 'POST':
        return redirect('confirm-payed-order')
    else:
        return render(request, 'checkout/checkout_2.html', {'form': payment})


@login_required
def summary(request):
    profile = Profile.objects.filter(user=request.user).first()

    cart_items = []
    cart_total_price = 0
    cart = request.session.get('cart', {})
    for prod_id, quantity in cart.items():
        prod = Product.objects.get(id=prod_id)
        item_total_price = quantity * int(prod.price)
        cart_total_price += item_total_price
        cart_items.append({'product': prod, 'quantity': quantity, 'item_total_price': item_total_price})

    context = {
        'profile': profile,
        'cart_items': cart_items,
        'cart_total_price': cart_total_price,
    }
    request.session['cart'] = {}

    return render(request, 'checkout/confirmed.html', context=context)


def create_order_unpayed(request):
    order = Order()
    order.user = request.user
    order.is_paid = False
    order.save()
    for id in request.session['cart']:
        item = Product.objects.filter(pk=id).first()
        order_item = OrderItem()
        order_item.order = order
        order_item.product = item
        order_item.save()

    return render(request, 'checkout/order_summary.html', {})

def create_order_payed(request):
    order = Order()
    order.user = request.user
    order.is_paid = True
    order.save()
    for id in request.session['cart']:
        item = Product.objects.filter(pk=id).first()
        order_item = OrderItem()
        order_item.order = order
        order_item.product = item
        order_item.save()


    return render(request, 'checkout/order_summary.html', {})
