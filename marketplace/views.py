# marketplace/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages

from .models import Product
from .forms import ProductForm, InquiryForm

# def product_list(request):
#     q = request.GET.get('q','')
#     products = Product.objects.all().order_by('-created_at')
#     if q:
#         products = products.filter(
#             Q(name__icontains=q) |
#             Q(description__icontains=q) |
#             Q(location__icontains=q)
#         )
#     return render(request, 'marketplace/product_list.html', {'products': products, 'q': q})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = InquiryForm()
    return render(request, 'marketplace/product_detail.html', {'product': product, 'form': form})

@login_required
def add_product(request):
    # Only farmers should add products
    if getattr(request.user, 'user_type', None) != 'farmer':
        messages.error(request, 'Only farmers can add products.')
        return redirect('product_list')

    if request.method == 'POST':
        print(request.POST)
        form = ProductForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            p = form.save(commit=False)
            p.seller = request.user
            p.save()
            messages.success(request, 'Product added.')
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'marketplace/add_product.html', {'form': form})

@login_required
def send_inquiry(request, pk):
    product = get_object_or_404(Product, pk=pk)
    # Only wholesalers may send inquiries
    if getattr(request.user, 'user_type', None) != 'wholesaler':
        messages.error(request, 'Only wholesalers can send inquiries.')
        return redirect('product_detail', pk=pk)

    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inq = form.save(commit=False)
            inq.product = product
            inq.buyer = request.user
            inq.save()
            messages.success(request, 'Inquiry sent to farmer.')
            return redirect('product_detail', pk=pk)
    return redirect('product_detail', pk=pk)

@login_required
def farmer_dashboard(request):
    if request.user.user_type != 'farmer':
        return redirect('/')

    products = Product.objects.filter(farmer=request.user)
    total_stock = sum(p.quantity for p in products)
    total_sold = sum(p.sold_quantity for p in products)

    return render(request, 'marketplace/farmer_dashboard.html', {
        'products': products,
        'total_stock': total_stock,
        'total_sold': total_sold,
    })

@login_required
def farmer_dashboard(request):
    if request.user.user_type != 'farmer':
        return redirect('/')

    products = Product.objects.filter(farmer=request.user)
    total_stock = sum(p.quantity for p in products)
    total_sold = sum(p.sold_quantity for p in products)

    return render(request, 'marketplace/farmer_dashboard.html', {
        'products': products,
        'total_stock': total_stock,
        'total_sold': total_sold,
    })

from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'marketplace/product_list.html', {'products': products})

