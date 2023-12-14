import os

from django.shortcuts import render, redirect
from .models import SeaFood
from .forms import SeaFoodForm
from django.views.generic import DeleteView, UpdateView

def index(request):
    prod_item = SeaFood.objects.order_by('id')
    return render(request, 'main/index.html', {'prods': prod_item})


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
    return render(request, 'main/form.html')

class Delete(DeleteView):
    model = SeaFood
    success_url = '/'
    template_name = 'main/sea-del.html'

class Update(UpdateView):
    model = SeaFood
    template_name = 'main/form.html'
    form_class = SeaFoodForm
    success_url = '/'

