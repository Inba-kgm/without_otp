from django.shortcuts import render,redirect,get_object_or_404
from farmer.models import *
from user.models import *
from .models import *
import json
import datetime

# Create your views here.
def index(request):
    myname=request.session.get('myname')
    delivered=acceptedorder.objects.filter(transporter_name=myname,status='Delivered')
    delivered_list=list(delivered.values())

    shipped=acceptedorder.objects.filter(transporter_name=myname,status='Shipped')

    context={'delivered_json':json.dumps(delivered_list),'delivered_count':delivered.count,'shipped_count':shipped.count,'myname':myname}
    return render(request,'transporter/index.html',context)

def history(request):
    myname=request.session.get('myname')
    objs=acceptedorder.objects.filter(transporter_name=myname,status='Shipped')
    objs_list=list(objs.values())

    myname=request.session.get('myname')
    delivered=acceptedorder.objects.filter(transporter_name=myname,status='Delivered')
    delivered_list=list(delivered.values())

    shipped=acceptedorder.objects.filter(transporter_name=myname,status='Shipped')

    context={'delivered_json':json.dumps(delivered_list),'delivered_count':delivered.count,'shipped_count':shipped.count,'myname':myname}


    context={'objs_json':json.dumps(objs_list),'objs_count':objs.count,'delivered_count':delivered.count,'shipped_count':shipped.count}
    return render(request,'transporter/history.html',context)

def transdelivered(request):
    myname=request.session.get('myname')
    objs=acceptedorder.objects.filter(transporter_name=myname,status='Delivered')
    objs_list=list(objs.values())


    myname=request.session.get('myname')
    delivered=acceptedorder.objects.filter(transporter_name=myname,status='Delivered')
    delivered_list=list(delivered.values())

    shipped=acceptedorder.objects.filter(transporter_name=myname,status='Shipped')

    context={'delivered_json':json.dumps(delivered_list),'delivered_count':delivered.count,'shipped_count':shipped.count,'myname':myname}


    context={'objs_json':json.dumps(objs_list),'objs_count':objs.count,'delivered_count':delivered.count,'shipped_count':shipped.count}
    return render(request,'transporter/delivered.html',context)

def profile(request):
    myname=request.session.get('myname')
    context={'myname':myname}
    return render(request,'transporter/profile.html',context)

def search(request):
  myname=request.session.get('myname')
  objs=acceptcart.objects.filter(status='Accepted')
  objs_list=list(objs.values())
  context={'objs_json':json.dumps(objs_list),'objs_count':objs.count,'myname':myname}
  return render(request,'transporter/search.html',context)
  
def accepted(request):
	if request.method=='POST':
		accept_obj_id=request.POST.get('objid')
		acceptcartobj=acceptcart.objects.get(id=accept_obj_id)
		acceptcartobj.status='Shipped'
		acceptcartobj.save()
		dest=acceptcartobj.to
		customer_name=acceptcartobj.customer_name
		fro=acceptcartobj.fromm
		addid=acceptcartobj.add_caartid
		name=acceptcartobj.product_name
		img1=acceptcartobj.image_1
		quant=acceptcartobj.quantity
		amt=acceptcartobj.price_per_kg
		phone_no=acceptcartobj.phone
		stat='Shipped'
		transportername=request.session.get('myname')
		acceptedorder.objects.create(accept_cart_id=accept_obj_id,status=stat,customer_name=customer_name,fromm=fro,to=dest,product_name=name,image_1=img1,quantity=quant,price_per_kg=amt,phone=phone_no,transporter_name=transportername)
		acceptobj=get_object_or_404(acceptedorder,accept_cart_id=accept_obj_id)
		acceptedobj=get_object_or_404(addcart,id=addid)
		acceptedobj.acceptedcartid=acceptobj.id
		acceptedobj.status='Shipped'
		acceptedobj.save()		
		return render(request,'transporter/search.html')

def delacc(request):
     obj_id=request.POST.get('objid')
     acceptedcartobj=get_object_or_404(acceptedorder,id=obj_id)
     acceptedcartobj.status='Delivered'
     acceptedcartobj.save()
     acceptcartid=acceptedcartobj.accept_cart_id
     acceptcartobj=get_object_or_404(acceptcart,id=acceptcartid)
     acceptcartobj.status='Delivered'
     acceptcartobj.save()
     addcartid=acceptcartobj.add_caartid
     addcartobj=get_object_or_404(addcart,id=addcartid)
     addcartobj.status="Delivered"
     addcartobj.save()
     return render(request,'transporter/delivered.html')
