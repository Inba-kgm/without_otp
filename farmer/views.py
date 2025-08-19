from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from login.models import cracc
from user.models import *
from transporter.models import*
from farmer.models import *
import json

def home(request):
    myname=request.session.get('myname')
    context={'myname':myname}
    return render(request, 'farmer/farmhome.html',context)

def farmhome(request):
    myname=request.session.get('myname')
    new_counts=addcart.objects.filter(farmer_name=myname,status='New')

    accepted_counts=addcart.objects.filter(farmer_name=myname,status='Accepted')

    cancelled_counts=addcart.objects.filter(farmer_name=myname,status='Cancelled')
    
    myname = request.session.get('myname')
    objs=farmerproduct.objects.filter(farmer_name=myname)
    objs_list=list(objs.values())

    context={'objs_json':json.dumps(objs_list),'objs_count':objs.count,'myname':myname,'new_count':new_counts.count,'accepted_count':accepted_counts.count,'cancelled_count':cancelled_counts.count}
    return render(request, 'farmer/farmhome.html',context)

def farmprofile(request):
    myname=request.session.get('myname')
    mypass=request.session.get('mypass')
    try:
        crobj=farmmprofile.objects.get(username=myname,password=mypass)
        em=crobj.email
        phone=crobj.phone
        datee=crobj.date
        loc=crobj.location
        farmname=crobj.farmname
        img_1=crobj.img_1
        
    except:
        crobj=cracc.objects.get(username=myname,password=mypass)
        em=crobj.email
        phone=crobj.phone_no
        datee=crobj.date
        loc=''
        farmname=''

    new_counts=addcart.objects.filter(farmer_name=myname,status='New')
    accepted_counts=addcart.objects.filter(farmer_name=myname,status='Accepted')
    count_counts=addcart.objects.filter(farmer_name=myname)
    delivered_counts=addcart.objects.filter(farmer_name=myname,status='Delivered')
    
    myname = request.session.get('myname')
    objs=farmerproduct.objects.filter(farmer_name=myname)
    objs_list=list(objs.values())

    context={'objs_json':json.dumps(objs_list),'objs_count':objs.count,'myname':myname,'new_count':new_counts.count,'accepted_count':accepted_counts.count,'delivered_count':delivered_counts.count,'count_count':count_counts.count,'email':em,'phone':phone,'date':datee,'location':loc,'farmname':farmname,'img_1':img_1}
    return render(request, 'farmer/farmprofile.html',context)

def farmupload(request):
    myname = request.session.get('myname')
    return render(request, 'farmer/farmupload.html', {'myname': myname})

def farmorders(request):
    myname=request.session.get('myname')
    objs=addcart.objects.filter(farmer_name=myname,status='New')
    objs_list=list(objs.values())

    myname=request.session.get('myname')
    new_counts=addcart.objects.filter(farmer_name=myname,status='New')

    accepted_counts=addcart.objects.filter(farmer_name=myname,status='Accepted')

    cancelled_counts=addcart.objects.filter(farmer_name=myname,status='Cancelled')
    
    context={'objs_json':json.dumps(objs_list),'objs_count':objs.count,'new_count':new_counts.count,'accepted_count':accepted_counts.count,'cancelled_count':cancelled_counts.count,'myname':myname}
    return render(request, 'farmer/farmorders.html',context)

def allorders(request):
    myname=request.session.get('myname')
    objs=addcart.objects.filter(farmer_name=myname)
    objs_list=list(objs.values())

    myname=request.session.get('myname')
    new_counts=addcart.objects.filter(farmer_name=myname,status='New')

    accepted_counts=addcart.objects.filter(farmer_name=myname,status='Accepted')

    cancelled_counts=addcart.objects.filter(farmer_name=myname,status='Cancelled')
    
    context={'objs_json':json.dumps(objs_list),'objs_count':objs.count,'new_count':new_counts.count,'accepted_count':accepted_counts.count,'cancelled_count':cancelled_counts.count,'myname':myname}
    return render(request, 'farmer/allorders.html',context)

def publish(request):
    if request.method == 'POST':
        try:
            
            myname = request.session.get('myname')
            mypass = request.session.get('mypass')
            dest=request.POST.get('destination')
            request.session['myaddress']=dest
            
            # Create product instance first
            product = farmerproduct(
                
                farmer_name=myname,
                password=mypass,
                image_1=request.FILES.get('image-1'),
                product_name=request.POST.get('product-name'),
                category=request.POST.get('category'),
                amount=request.POST.get('amount'),
                address=request.POST.get('destination'),
                per_unit=request.POST.get('per-unit'),
                available_quantity=request.POST.get('available-quantity'),
                description=request.POST.get('description')
            )
            # Save the product - files will go to media/products/
            product.save()
            # farmerproduct.objects.create(username=myname,
            #     password=mypass,
            #     image_1=request.POST.get('image-1'),
            #     product_name=request.POST.get('product-name'),
            #     category=request.POST.get('category'),
            #     amount=request.POST.get('amount'),
            #     per_unit=request.POST.get('per-unit'),
            #     available_quantity=request.POST.get('available-quantity'),
            #     description=request.POST.get('description'))
            
            # Update upload count
            mylogobj = cracc.objects.get(username=myname, password=mypass)
            mylogobj.no_of_uploads += 1
            mylogobj.save()
            
            return redirect('farmhome')
            
        except Exception as e:
            return render(request, 'farmer/farmupload.html', {
                'error': f"Upload failed: {str(e)}",
                'myname': request.session.get('myname')
            })
    
    return redirect('farmupload')
    
def acceptcarts(request):
	if request.method=='POST':
            obj_id=request.POST.get('objid')
            addcartobj=addcart.objects.get(id=obj_id)
            dest=addcartobj.destination
            customer_name=addcartobj.customer_name
            datee=addcartobj.created_at
            fro=addcartobj.fromm
            name=addcartobj.product_name
            img1=addcartobj.image_1
            quant=addcartobj.quantity
            amt=addcartobj.price_per_kg
            tot=addcartobj.total
            description=addcartobj.note
            phone_no=addcartobj.phone
            stat='Accepted'
            acceptcart.objects.create(total=tot,add_caartid=obj_id,status=stat,customer_name=customer_name,created_at=datee,fromm=fro,to=dest,product_name=name,image_1=img1,quantity=quant,price_per_kg=amt,note=description,phone=phone_no)
            addcartobj=get_object_or_404(addcart,id=obj_id)
            addcartobj.status='Accepted'
            addcartobj.save()
            acceptcartidobj=get_object_or_404(acceptcart,add_caartid=obj_id)
            addcartobj.acceptcartid=acceptcartidobj.id
            addcartobj.save()
            return redirect('/farmer/farmorders/')    

def removes(request):
    obj_id=request.POST.get('obj_id')
    obj=get_object_or_404(farmerproduct,id=obj_id)
    obj.delete()
    return redirect('/farmer/farmhome/')
    

def pending(request):
    myname=request.session.get('myname')
    objs=addcart.objects.filter(farmer_name=myname,status='Accepted')
    objs_list=list(objs.values())

    myname=request.session.get('myname')
    new_counts=addcart.objects.filter(farmer_name=myname,status='New')

    accepted_counts=addcart.objects.filter(farmer_name=myname,status='Accepted')

    cancelled_counts=addcart.objects.filter(farmer_name=myname,status='Cancelled')
    
    context={'objs_json':json.dumps(objs_list),'objs_count':objs.count,'new_count':new_counts.count,'accepted_count':accepted_counts.count,'cancelled_count':cancelled_counts.count}
    return render(request,'farmer/pending.html',context)
  

def shipped(request):

    myname=request.session.get('myname')

    myname=request.session.get('myname')
    objs=addcart.objects.filter(farmer_name=myname,status='Shipped')
    objs_list=list(objs.values())

    new_counts=addcart.objects.filter(farmer_name=myname,status='New')

    accepted_counts=addcart.objects.filter(farmer_name=myname,status='Accepted')

    cancelled_counts=addcart.objects.filter(farmer_name=myname,status='Cancelled')
    
    context={'objs_json':json.dumps(objs_list),'objs_count':objs.count,'new_count':new_counts.count,'accepted_count':accepted_counts.count,'cancelled_count':cancelled_counts.count}
    return render(request,'farmer/shipped.html',context)
  
def cancelled(request):
    myname=request.session.get('myname')
    objs=addcart.objects.filter(farmer_name=myname,status='Cancelled')
    objs_list=list(objs.values())

    myname=request.session.get('myname')
    new_counts=addcart.objects.filter(farmer_name=myname,status='New')

    accepted_counts=addcart.objects.filter(farmer_name=myname,status='Accepted')

    cancelled_counts=addcart.objects.filter(farmer_name=myname,status='Cancelled')
    
    context={'objs_json':json.dumps(objs_list),'objs_count':objs.count,'new_count':new_counts.count,'accepted_count':accepted_counts.count,'cancelled_count':cancelled_counts.count}
    return render(request,'farmer/cancelled.html',context)


def delivered(request):

    myname=request.session.get('myname')

    objs=addcart.objects.filter(farmer_name=myname,status='Delivered')
    objs_list=list(objs.values())

    new_counts=addcart.objects.filter(farmer_name=myname,status='New')

    accepted_counts=addcart.objects.filter(farmer_name=myname,status='Accepted')

    cancelled_counts=addcart.objects.filter(farmer_name=myname,status='Cancelled')

    context={'objs_json':json.dumps(objs_list),'objs_count':objs.count,'new_count':new_counts.count,'accepted_count':accepted_counts.count,'cancelled_count':cancelled_counts.count}
    
    return render(request,'farmer/delivered.html',context)
  
def removeorder(request):
    obj_id=request.POST.get('objid')
    obj=get_object_or_404(addcart,id=obj_id)
    obj.status='Cancelled'
    obj.save()
    return redirect('/farmer/farmhome/')

def editprofile(request):
    myname=request.session.get('myname')
    mypass=request.session.get('mypass')
    obj=farmmprofile.objects.get(username=myname,password=mypass)
    img_1=obj.img_1
    email=obj.email
    phone=obj.phone
    farmname=obj.farmname
    location=obj.location
    context={'img_1':img_1,'myname':myname,'email':email,'phone':phone,'farmname':farmname,'location':location}
    return render(request,'farmer/editfarmprofile.html',context)

def changeinfo(request):
    name=request.POST.get('myname')
    email=request.POST.get('email')
    phone=request.POST.get('phone')
    farmname=request.POST.get('farmname')
    location=request.POST.get('location')
    myname=request.session.get('myname')
    mypass=request.session.get('mypass')
    farmmobj=farmmprofile.objects.get(username=myname,password=mypass)
    farmmobj.username=name
    farmmobj.email=email
    farmmobj.phone=phone
    farmmobj.farmname=farmname
    farmmobj.location=location
    farmmobj.save()
    entryobj=cracc.objects.get(username=myname,password=mypass)
    entryobj.username=name
    entryobj.save()
    return redirect('/farmer/farmprofile/')
    
