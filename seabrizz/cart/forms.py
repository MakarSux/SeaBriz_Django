from django.forms import forms

PRODUCT_QUANTITY_CHOISES = [(i, str(i)) for i in range(1, 21)]

class CartAddProdForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choises=PRODUCT_QUANTITY_CHOISES,
        coerce=int,
    )
    update = forms.BooleanField(
        required = False,
        initial=False,
        widget=forms.HiddenInput
    )