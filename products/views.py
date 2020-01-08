from django.shortcuts import render
from .models import Product, Category

def index(request):
    """A view that displays the index page"""
    products= Product.objects.all()
    return render(request, "products.html", {"products": products})
    
def products(request):
    """A view that displays the index page"""
    products= Product.objects.all()
    return render(request, "products.html", {"products": products})
    

def get_toys(request):
    """A view that displays the index page"""
    catagory = get_object_or_404(Category, name="Toys")
    products = Product.objects.filter(category=catagory)
    return render(request, "products.html", {"products": products, "catagory":catagory})
    
def get_art(request):
    """A view that displays the index page"""
    catagory = get_object_or_404(Category, name="Art")
    products = Product.objects.filter(category=catagory)
    return render(request, "products.html", {"products": products, "catagory":catagory})
    
def get_products(request):
    """A view that displays the index page"""
    catagory = get_object_or_404(Category, name="All Antiques")
    products = Product.objects.filter(category=catagory)
    return render(request, "products.html", {"products": products, "catagory":catagory})

def get_clocks(request):
    """A view that displays the index page"""
    catagory = get_object_or_404(Category, name="Clocks")
    products = Product.objects.filter(category=catagory)
    return render(request, "products.html", {"products": products, "catagory":catagory})
    
def get_classic_cars(request):
    """A view that displays the index page"""
    catagory = get_object_or_404(Category, name="Classic Cars")
    products = Product.objects.filter(category=catagory)
    return render(request, "products.html", {"products": products, "catagory":catagory})
    
def get_furniture(request):
    """A view that displays the index page"""
    catagory = get_object_or_404(Category, name="Furniture")
    products = Product.objects.filter(category=catagory)
    return render(request, "products.html", {"products": products, "catagory":catagory})
    
def get_jewellery(request):
    """A view that displays the index page"""
    catagory = get_object_or_404(Category, name="Jewellery")
    products = Product.objects.filter(category=catagory)
    return render(request, "products.html", {"products": products, "catagory":catagory})
    
def catagory_id(request, pk):
    """A view that displays the index page"""
    catagory = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(category=catagory)
    return render(request, "products.html", {"products": products, "catagory":catagory})