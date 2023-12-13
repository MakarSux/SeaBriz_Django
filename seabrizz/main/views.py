from django.shortcuts import render
from .models import SeaFood

def index(request):
    return render(request, 'main/index.html')
# Create your views here.
