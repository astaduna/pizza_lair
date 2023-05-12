from django.shortcuts import render, redirect
from order.models import Order, OrderItem
from user.models import Profile
from user.forms.checkout import CheckoutProfileInfo, CheckoutPaymentForm
from django.contrib.auth.decorators import login_required
from cart.models import Product
from django.shortcuts import render




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
        if payment.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.save()
        return render(redirect('confirm-payed-order'))
    return render(request, 'checkout/checkout_2.html',
                  {'form': payment})


@login_required
def summary(request):
    profile = Profile.objects.filter(user=request.user).first()
    cart_items = []
    total_price = 0
    for prod_id, quantity in request.session['cart'].items():
        prod = Product.objects.get(id=prod_id)
        price = quantity * int(prod.price)
        cart_items.append({'product': prod, 'quantity': quantity, 'price': price})
        total_price += price

    context = {
        'profile': profile,
        'items': cart_items,
        'total_price': total_price,
    }
    print(context)
    return render(request, 'checkout/order_summary.html', context)

@login_required
def create_order_paid(request):
    order = Order()
    order.user = request.user
    order.is_paid = True
    order.save()
    order_items = []
    total_price = 0
    for prod_id, quantity in request.session['cart'].items():
        prod = Product.objects.get(id=prod_id)
        price = quantity * int(prod.price)
        total_price += price
        order_item = OrderItem()
        order_item.order = order
        order_item.product = prod
        order_item.quantity = quantity
        order_item.price = prod.price
        order_item.save()
        order_items.append({'product': prod, 'quantity': quantity, 'price': price})
    order.total_price = total_price
    order.save()
    request.session['cart'] = {}
    return render(request, 'checkout/order_summary.html', {"items": order_items, "total_price": total_price})



def create_order_unpaid(request):
    order = Order()
    order.user = request.user
    order.is_paid = False
    order.save()
    order_items = []
    total_price = 0
    for prod_id, quantity in request.session['cart'].items():
        prod = Product.objects.get(id=prod_id)
        price = quantity * int(prod.price)
        total_price += price
        order_item = OrderItem()
        order_item.order = order
        order_item.product = prod
        order_item.quantity = quantity
        order_item.price = prod.price
        order_item.save()
        order_items.append({'product': prod, 'quantity': quantity, 'price': price})
    order.total_price = total_price
    order.save()
    request.session['cart'] = {}
    return render(request, 'checkout/order_summary.html', {"items": order_items, "total_price": total_price})

