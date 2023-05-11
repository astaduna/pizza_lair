from django.shortcuts import render, get_object_or_404
from offers.models import Offer

def index(request):
    context = {'offers': Offer.objects.all().order_by('id')}
    return render(request, 'offers/offer_menu.html', context)


def get_offer_by_id(request, id):
    return render(request, 'offers/offer_detail.html', {
        'offer': get_object_or_404(Offer, pk=id)
    })