from django.urls import path  
from .import views

urlpatterns = [
    # path('add_product_page',views.add_product_page,name='add_product_page'),
    path('add_product',views.add_product,name='add_product'),
    path('product_list',views.product_list,name='product_list'),
    path('update_product_page/<int:i>',views.update_product_page,name='update_product_page'),
    path('update_product',views.update_product,name='update_product'),
    path('delete_product/<int:i>',views.delete_product,name='delete_product')
]
