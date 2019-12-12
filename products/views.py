from django.shortcuts import render
from .models import Product

def index(request):
    """A view that displays the index page"""
    products= Product.objects.all()
    return render(request, "products.html", {"products": products})
    
def products(request):
    """A view that displays the index page"""
    products= Product.objects.all()
    return render(request, "products.html", {"products": products})
    

    