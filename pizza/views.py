from django.shortcuts import render


def index(request):
    return render(request, 'pizza/pizza_menu.html')