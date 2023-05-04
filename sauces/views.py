from django.shortcuts import render


def index(request):
    return render(request, 'sauces/sauce_menu.html')