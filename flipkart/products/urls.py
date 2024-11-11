from django.urls import path  
from .import views

urlpatterns = [
    path('add_product_page',views.add_product_page,name='add_product_page'),
    path('add_product',views.add_product,name='add_product'),
    path('product_list',views.product_list,name='product_list')
]
