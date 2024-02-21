
# Create your views here.
from django.shortcuts import render
from products.models import Product
# Create your views here.
def index(request):
    
    # context = {'products' : Product.objects.all()}
   # return render(request, 'home/index.html', context )
    return render(request, 'home/index.html' )

def about(request):
    
    return render(request, 'home/about.html')

def game1(request):
    
    return render(request, 'home/game1.html')

def game2(request):
    
    return render(request, 'home/game2.html')