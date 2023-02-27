from django.shortcuts import render,redirect
import django
from.models import product_collection,comment_box

# Create your views here.

def details(request):
    id=request.GET['id']
    pro=product_collection.objects.get(id=id)
    van=product_collection.objects.filter(id=id)
    return render(request,"about.html", {'key1':pro,'van':van})

def comment(request):
        name=request.POST['user']
        id=request.POST['pro']
        message=request.POST['msg']
        cmt=comment_box.objects.create(name=name,msg=message,fkey_id=id)
        cmt.save();
        return redirect("/")