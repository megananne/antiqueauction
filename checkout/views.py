def cart(request):
    """A view that displays the index page"""
    return render(request, "cart.html")
    
def checkout(request):
    """A view that displays the index page"""
    return render(request, "checkout.html")