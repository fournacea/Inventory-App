from django.shortcuts import render, redirect

from .forms import ProductForm
from .models import Product

# Home view
def home_view(request):
    return render(request, 'InventoryApp/home.html', {})


# Create view
def product_create_view(request):
    form = ProductForm()
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        
        if form.is_valid():
            form.save()
        return redirect('product-list')
    
    # GET request
    return render(request, 'InventoryApp/product-form.html', {'form': form})
    

# Delete view
def product_delete_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    
    if request.method == "POST":
        product.delete()
        return redirect('product-list')

    # GET request
    return render(request, 'InventoryApp/product-confirm-delete.html', {'product': product})


# Read view
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'InventoryApp/product-list.html', {'products': products})


# Update view
def product_update_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    
    if request.method == "POST":
        form =ProductForm(request.POST, instance=product)
        
        if form.is_valid():
            form.save()
            
        return redirect('product-list')
    
    # GET request
    form =ProductForm(instance=product)
    
    return render(request, 'InventoryApp/product-form.html', {'form': form})
