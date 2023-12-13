import os

from django.shortcuts import render
from .models import SeaFood

def index(request):
    prod_item = SeaFood.objects.order_by('id')
    return render(request, 'main/index.html', {'prods': prod_item})

