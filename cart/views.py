from django.shortcuts import render, redirect
from pizza.models import Pizza
from django.contrib import messages



# Create your views here.
def index(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request):
    if request.method == "POST":
        pizza_id = request.POST.get("pizza_id")
        pizza_size = request.POST.get("pizza_size")
        if pizza_id and pizza_size:
            pizza = Pizza.objects.get(id=pizza_id)
            if pizza_size == "small":
                price = pizza.small_price
            elif pizza_size == "medium":
                price = pizza.medium_price
            elif pizza_size == "large":
                price = pizza.large_price
            else:
                price = 0
            cart_item = {
                "pizza": pizza,
                "size": pizza_size,
                "price": price
            }
            cart = request.session.get("cart", {})
            cart[pizza_id] = cart_item
            request.session["cart"] = cart
            messages.success(request, f"{pizza.name} ({pizza_size}) added to cart.")
            return redirect("cart-index")
    messages.error(request, "Error adding pizza to cart.")
    return redirect("home")