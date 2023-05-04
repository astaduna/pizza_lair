from django.shortcuts import render


def index(request):
    return render(request, 'drinks/drinks_menu.html')