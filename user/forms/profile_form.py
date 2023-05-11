
from user.models import Profile
from django import forms


class ProfileForm(forms.ModelForm):
    COUNTRY_CHOICES = (
        ('ISK', 'Ísland'),
        ('DEN', 'Danmörk'),
        ('ENG', 'England'),
    )
    country = forms.ChoiceField(choices=COUNTRY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        exclude = ['id', 'user', 'house_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'zip': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_image': forms.TextInput(attrs={'class': 'form-control'})
        }

