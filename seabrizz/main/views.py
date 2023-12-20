import os

from django.shortcuts import render, redirect, get_object_or_404
from .models import SeaFood
from .forms import SeaFoodForm
from django.views.generic import DeleteView, UpdateView
from cart.forms import CartAddProductForm

def index(request):
    prod_item = SeaFood.objects.order_by('id')
    return render(request, 'main/index.html', {'prods': prod_item})

def about(request):
    return render(request, 'main/about.html')

def shedule(request):
    return render(request, 'main/shedule.html')

def add(request):
    error = ""
    if request.method == "POST":
        form = SeaFoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = "Неверная форма"

    form = SeaFoodForm()
    context = {'form': form, 'error': error}
    return render(request, 'main/form.html', context)

class Delete(DeleteView):
    model = SeaFood
    success_url = '/'
    template_name = 'main/sea-del.html'

class Update(UpdateView):
    model = SeaFood
    template_name = 'main/form.html'
    form_class = SeaFoodForm
    success_url = '/'

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'main/index.html')

