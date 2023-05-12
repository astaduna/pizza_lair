from django.shortcuts import render, redirect
from user.models import Profile
from user.forms.checkout import CheckoutProfileInfo, CheckoutPaymentForm, CheckoutPlaceForm
from django.contrib.auth.decorators import login_required
# from django.urls import reverse
from cart.models import Product
from order.forms.order import OrderForm



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

def place(request):
    form = CheckoutPlaceForm()
    return render(request, 'checkout/checkout_place.html',
                  {'form':form})

def payment(request):
    form = CheckoutPaymentForm()
    return render(request, 'checkout/checkout_2.html',
                  {'form': form})



@login_required
def summary(request):
    profile = Profile.objects.filter(user=request.user).first()

    cart_items = []
    total_price = 0
    cart = request.session.get('cart', [])
    for prod_id in cart:
        prod = Product.objects.get(id=prod_id)
        cart_items.append(prod)
        total_price += int(prod.price)

    context = {
        'profile': profile,
        'cart_items': cart_items,
        'total_price': total_price,
    }

    return render(request, 'checkout/order_summary.html', context)


@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('confirm-order', pk=post.pk)
    else:
        form = OrderForm()

    return render(request, 'checkout/confirm_order.html', {'form': form})



