from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    godine = forms.IntegerField(min_value=1, label="Godine")
    visina = forms.FloatField(min_value=50, label="Visina (cm)")
    tezina = forms.FloatField(min_value=20, label="Težina (kg)")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "godine", "visina", "tezina")

    def save(self, commit=True):
        user = super().save(commit=True)
        godine = self.cleaned_data.get('godine')
        visina = self.cleaned_data.get('visina')
        tezina = self.cleaned_data.get('tezina')
        KorisnickiProfil.objects.create(korisnik=user, godine=godine, visina=visina, tezina=tezina)
        return user


class FitnessCiljForm(forms.ModelForm):
    class Meta:
        model = FitnessCilj
        fields = ['naziv_cilja', 'trenutna_vrijednost', 'ciljna_vrijednost', 'rok']
        widgets = {
            'rok': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['naziv_cilja'].widget = forms.Select(choices=FitnessCilj.FITNESS_CILJ)
        
class VjezbeForm(forms.Form):
    naziv_vjezbe = forms.ModelChoiceField(
        queryset=Vjezba.objects.all(),
        empty_label="Odaberi vježbu",
        widget=forms.Select(attrs={'class': 'form-control'})
    )