from django.shortcuts import render,redirect
from .models import Products

def add_product_page(request):
      return render(request,'add_product.html')

def add_product(request):
      name = request.POST['name']
      price = request.POST['price']
      qty = request.POST['qty']
      product = Products(name=name,price=price,quantity=qty)
      product.save()
      return redirect('add_product_page')
      
def product_list(request):
      products = Products.objects.all()
      return render(request,'product_list.html',{'products':products})