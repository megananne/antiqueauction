from django.shortcuts import render

# Create your views here.

def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")
    
def about(request):
    """A view that displays the about page"""
    return render(request, "about.html")

def terms(request):
    """A view that displays the about page"""
    return render(request, "terms.html")

def support(request):
    """A view that displays the about page"""
    return render(request, "support.html")

def reviews(request):
    """A view that displays the about page"""
    return render(request, "reviews.html")
