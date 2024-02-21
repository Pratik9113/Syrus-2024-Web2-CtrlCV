# from django.urls import path
# from products.views import get_products
# # from pratikwebsite import views
# urlpatterns = [
#     path('<slug/>',get_products, name = "get_products"),
# ]
from django.urls import path
from products.views import get_product

urlpatterns = [
   
    path('<slug>/' , get_product , name="get_product"),
]