from django.shortcuts import render
from .models import Side


def index(request):
    context = {'sides': Side.objects.all().order_by('id')}
    return render(request, 'sides/side_menu.html', context)

