from django.shortcuts import render, redirect
from user.models import Profile
from user.forms.payment import CheckoutProfileInfo


# Create your views here.
def index(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = CheckoutProfileInfo(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('/')

    return render(request, 'checkout/checkout.html', {
        'form': CheckoutProfileInfo(instance=profile)
    })
