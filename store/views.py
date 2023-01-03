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
    category = Category.objects.filter(slug=slug,status = 0)
    if(category):
        products = Product.objects.filter(slug = slug)
        category_name = Category.objects.filter(slug=slug).first()
        context = {'products': products,'category_name': category_name}
        return render(request, 'store/products/index.html',context)
    else:
        messages.warning(request,'category not found')
        return redirect('collections')