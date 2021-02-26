from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import Product,Cart
# Create your views here.
def index(request):
    
    if request.method=='POST':
        request.session['user']=request.POST.get('user')
        allvegi=Cart.objects.filter(person=request.session['user'])
        
        to=0
        po=0
        ma=0
        sp=0
        for vegi in allvegi:
            if vegi.productid.id==1:
                to=vegi.qty
                
        
            if vegi.productid.id==2:
                po=vegi.qty
    
            if vegi.productid.id==3:
                sp=vegi.qty
        
                
            if vegi.productid.id==4:
                ma=vegi.qty
        
            
        
        return render(request,'index.html',{'data':'hello sanket bye some today','ma':ma,'to':to,'po':po,'sp':sp})
    return render(request,'index.html')
def cart(request):
    val = request.GET.get('val', None)
    key=request.GET.get('key',None)
    c=Cart.objects.filter(person=request.session['user'])
    di={
        'to':'Tomato',
        'po':'Potato',
        'ma':'Mashroom',
        'sp':'Spinach'
    }
    some=[]
    for k in c:
        some.append(k.productid.name)
        if k.productid.name==di[key]:
            k.qty= val
            k.save()
            
    if not di[key] in some:
        prod=Product.objects.filter(name=di[key]).first()
        print(prod)
        addtoc=Cart(person=request.session['user'],productid=prod,qty=1)
        addtoc.save()
            
    data = {'data':'hello'}
    return JsonResponse(data)
def addcart(request):
    data=Cart.objects.filter(person=request.session['user'])
    return render(request,'cart.html',{'data':data})
    