from django.shortcuts import render,redirect
from .models import Products

# def add_product_page(request):
#       return render(request,'add_product.html')

# def add_product(request):
#       name = request.POST['name']
#       price = request.POST['price']
#       qty = request.POST['qty']
#       product = Products(name=name,price=price,quantity=qty)
#       product.save()
#       return redirect('add_product_page')


def add_product(request):
      if request.method=='POST':
            name = request.POST['name']
            price = request.POST['price']
            qty = request.POST['qty']
            product = Products(name=name,price=price,quantity=qty)
            product.save()
            return redirect('add_product')  
      else:
            return render(request,'add_product.html')


      
def product_list(request):
      products = Products.objects.all()
      return render(request,'product_list.html',{'products':products})

def update_product_page(request,i):
      global product
      product = Products.objects.get(id=i)
      return render(request,'update_product.html',{'product':product})

def update_product(request):
      name = request.POST['name']
      price = request.POST['price']
      qty = request.POST['qty']
      product.name = name 
      product.price = price 
      product.quantity = qty 
      product.save()
      return redirect('product_list')
      

def delete_product(request,i):
      product = Products.objects.get(id=i)
      product.delete()
      return redirect('product_list')