from .models import SeaFood
from django.forms import ModelForm, TextInput, Textarea, FileInput


class SeaFoodForm(ModelForm):
    class Meta:
        model = SeaFood
        fields = ["name", "proiz", "price", "descr", "quantity", "photo"]
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование',
            }),
            'proiz': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Производиьтель',
            }),
            'price': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена',
            }),
            'descr': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание',
            }),
            'quantity': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество',
            }),
            'photo': FileInput(attrs={
                'class': 'photo_cntrl',
            })
        }