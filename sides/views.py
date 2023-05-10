from django.shortcuts import render, get_object_or_404
from .models import Side


def index(request):
    context = {'sides': Side.objects.all().order_by('id')}
    return render(request, 'sides/side_menu.html', context)

def get_sides_by_id(request, id):
    return render(request, 'sides/sides_detail.html', {
        'side': get_object_or_404(Side, pk=id)
    })