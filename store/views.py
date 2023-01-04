from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'store/index.html')

def collections(request):
    categories = Category.objects.filter(status=0)
    context = {'categories': categories}
    return render(request, 'store/collections.html',context)

def collectionsView(request,slug):
    if(Category.objects.filter(slug=slug,status = 0)):
        products = Product.objects.filter(slug = slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products': products,'category': category}
        return render(request, 'store/products/index.html',context)
    else:
        messages.warning(request,'category not found')
        return redirect('collections')
    
def productDetails(request, cat_slug,pro_slug):
    if(Category.objects.filter(slug=cat_slug,status=0)):
        if(Product.objects.filter(slug=pro_slug,status=0)):
            products = Product.objects.filter(slug=pro_slug,status=0).first()
            context = {'products': products}
        else:
            messages.warning(request,'product not found')
            return redirect('collections')
    else:
        messages.warning(request,'category not found')
        return redirect('collections')
    return render(request, 'store/products/detail.html',context)