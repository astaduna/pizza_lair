
from user.models import Profile
from django import forms


class CheckoutProfileInfo(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user', 'profile_image', 'country']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'zip': forms.TextInput(attrs={'class': 'form-control'}),
        }
