from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.models import SeaFood
from . cart import Cart
from . forms import CartAddProdForm

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(SeaFood, id=product_id) #скорее всего где-то здесь затык =(
    form = CartAddProdForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product = product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request,  product_id):
    cart = Cart(request)
    product = get_object_or_404(SeaFood, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')
# Create your views here.

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProdForm(
            initial={
                'quantity': item['quantity'],
                'update': True})
    return render(request, 'cart/detail.html', {'cart':cart})