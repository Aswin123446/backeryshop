from django.shortcuts import render
from product.models import product_collection

# Create your views here.
def index(request):
        pro=product_collection.objects.all()
        return render(request,"index.html",{"pro":pro})
 