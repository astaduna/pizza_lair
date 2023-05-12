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
    cart = request.session.get('cart', {})
    for prod_id in cart:
        prod = Product.objects.get(id=prod_id)
        cart_items.append(prod)
        total_price += int(prod.price)

    context = {
        'profile': profile,
        'cart_items': cart_items,
        'total_price': total_price,
    }


@login_required
def create_order_payed(request):
    order = Order()
    order.user = request.user
    order.is_paid = True
    order.save()
    my_products = []
    print("asdfdsfasdf")
    print(request.session['cart'])
    for id in request.session['cart']:
        print(id)
        item = Product.objects.filter(pk=id).first()
        my_products.append(item)
        order_item = OrderItem()
        order_item.order = order
        order_item.product = item
        order_item.save()
    request.session['cart'] = {}





    return render(request, 'checkout/order_summary.html', {"items": my_products})

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
    request.session['cart'] = {}



    return render(request, 'checkout/order_summary.html', {})
