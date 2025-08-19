from django.shortcuts import render,redirect,get_object_or_404
from farmer.models import *
import json
from farmer.models import *
from .models import *
from transporter.models import *
from datetime import datetime
# Create your views here.
rtemp=0

def userorders(request):
    myname=request.session.get('myname')
    objs=addcart.objects.filter(customer_name=myname)
    objs_list=list(objs.values())
    context={'objs_json':json.dumps(objs_list),'objs_count':objs.count,'myname':myname}
    return render(request,'user/allorders.html',context)


def recent(request):
    myname=request.session.get('myname')
    objs=addcart.objects.filter(customer_name=myname,status='New')
    objs_list=list(objs.values())
    context={'objs_json':json.dumps(objs_list),'objs_count':objs.count,'myname':myname}
    return render(request,'user/userorders.html',context)


def accepts(request):
    myname=request.session.get('myname')
    objs=addcart.objects.filter(customer_name=myname,status="Accepted")
    objs_list=list(objs.values())
    context={'objs_json':json.dumps(objs_list),'objs_count':objs.count,'myname':myname}
    return render(request,'user/accepted.html',context)


def shipped(request):
    myname=request.session.get('myname')
    objs=addcart.objects.filter(customer_name=myname,status='Shipped')
    objs_list=list(objs.values())
    context={'objs_json':json.dumps(objs_list),'objs_count':objs.count,'myname':myname}
    return render(request,'user/shipped.html',context)


def delivered(request):
    myname=request.session.get('myname')
    objs=addcart.objects.filter(customer_name=myname,status='Delivered')
    objs_list=list(objs.values())
    context={'objs_json':json.dumps(objs_list),'objs_count':objs.count,'myname':myname}
    return render(request,'user/delivered.html',context)


def cancelled(request):
    myname=request.session.get('myname')
    objs=addcart.objects.filter(customer_name=myname,status='Cancelled')
    objs_list=list(objs.values())
    context={'objs_json':json.dumps(objs_list),'objs_count':objs.count,'myname':myname}
    return render(request,'user/cancelled.html',context)


def userhome(request):
    myname=request.session.get('myname')
    products=farmerproduct.objects.all()
    products_list=list(products.values())
    context={'products_json':json.dumps(products_list),'products_count':products.count,'myname':myname}
    return render(request,'user/userhome.html',context)


def userprofile(request):
    myname=request.session.get('myname')
    context={'myname':myname}
    return render(request,'user/userprofile.html',context)


def userproducts(request):
    myname=request.session.get('myname')
    products=farmerproduct.objects.all()
    products_lst=list(products.values())
    context={'products_json':json.dumps(products_lst),'products_count':products.count,'myname':myname}
    return render(request,'user/userproducts.html',context)

def addtocart(request):
    productname=request.POST.get('prdnm')
    amount=request.POST.get('amnt')
    image=request.POST.get('image')
    fro=request.POST.get('from')
    description=request.POST.get('description')
    farmername=request.POST.get('farmername')

    sample={
        'productname':productname,
        'amount':amount,
        'image':image,
        'fro':fro,
        'description':description,
        'farmername':farmername,
    }
    return render(request,'user/usercart.html',sample)

def addcarts(request):
    myname=request.session.get('myname')
    dest=request.POST.get('destination')
    name=request.POST.get('productname')
    img1=request.POST.get('image1')
    datee=datetime.now().date()
    amt=request.POST.get('amount')
    quant=request.POST.get('quantity')
    fro=request.POST.get('fro')
    phone_no=request.POST.get('phone')
    description=request.POST.get('description')
    farmer=request.POST.get('farmername')
    tot=int(amt)*int(quant)
    addcart.objects.create(total=tot,farmer_name=farmer,customer_name=myname,created_at=datee,fromm=fro,destination=dest,product_name=name,image_1=img1,quantity=quant,price_per_kg=amt,note=description,phone=phone_no)
    return redirect('/user/userhome/')

def delacc(request):
    obj_id=request.POST.get('objid')
    addcartobj=get_object_or_404(addcart,id=obj_id)
    addcartobj.status='Delivered'
    obj_id=addcartobj.acceptcartid
    addcartobj.save()
    acceptcartobj=get_object_or_404(acceptcart,id=obj_id)
    acceptcartobj.status="Delivered"
    obj_id=addcartobj.acceptedcartid
    acceptcartobj.save()
    acceptedcartobj=get_object_or_404(acceptedorder,id=obj_id)
    acceptedcartobj.status='Delivered'
    acceptedcartobj.save()
    return redirect('/user/userdelivered/')
    