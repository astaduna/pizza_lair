from django.forms import ModelForm, widgets
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

class CheckoutPlaceForm(forms.Form):
    Checkout_Places= (
        ('KEF', 'Keflavík'),
        ('RVK', 'Reykjavík'),
        ('HFJ', 'Hafnarfjörður'),
    )
    staðir = forms.ChoiceField(choices=Checkout_Places, widget=forms.Select(attrs={'class': 'form-control'}))


class CheckoutPaymentForm(forms.Form):
    nafn_af_korthafandi = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    kortanúmer = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                                    'placeholder': '1234-1234-1234-1234',
                                                                    'pattern': '[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}',
                                                                    'maxlength': 19,
                                                                    'title': '1234-1234-1234-1234'}))
    cvc = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'pattern': '[0-9]{3}',
                                                           'maxlength': 3,
                                                           'title': '3 digit number',
                                                           'label': 'CVC'}))
    gildistími = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                                    'pattern': '(?:0[5-9]|1[0-2])/[2-9]{1}[0-9]{1}',
                                                                    'maxlength': 5,
                                                                    'title': 'mm/yy',
                                                                    'placeholder': 'mm/yy'}))




