from django import forms
from .models import CartDetails


class CartForm(forms.ModelForm):
    class Meta:
        model = CartDetails
        fields = ['price_ht','movie_name']





