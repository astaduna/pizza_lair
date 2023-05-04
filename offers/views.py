from django.shortcuts import render

def index(request):
    return render(request, 'offers/offer_menu.html')