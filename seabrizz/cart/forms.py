from django import forms

from main.models import SeaFood
from django.forms import TypedChoiceField

PRODUCT_QUANTITY_CHOISES = [(i, str(i)) for i in SeaFood.objects.all()]

class CartAddProdForm(forms.Form):
    quantity = forms.TypedChoiceField(
        empty_value=PRODUCT_QUANTITY_CHOISES,
        coerce=int,
    )
    update = forms.BooleanField(
        required = False,
        initial=False,
        widget=forms.HiddenInput
    )