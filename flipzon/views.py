from django.shortcuts import render, HttpResponse
from.models import Product, Contact, Order
from math import ceil
# Create your views here.

def home(request):
    
    allProds = []
    catprods = Product.objects.values('category')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
        params= {'allProds': allProds}
    return render(request, 'flipzon/index.html', params)


def about(request):
    return render(request, 'flipzon/about.html')

def contact(request):
    if request.method== "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone= request.POST.get('phone', '')
        query= request.POST.get('query', '')
        contact=Contact(name=name, email=email, phone= phone, query=query) 
        contact.save()
        
    return render(request, 'flipzon/contact.html')

def checkout(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state =request.POST.get('state', '')
        pincode=request.POST.get('pincode', '')
        phone= request.POST.get('phone', '')   
        order = Order(name=name, email=email, address= address, city= city, state= state, pincode= pincode, phone= phone) 
        order.save()
    return render(request, 'flipzon/checkout.html')

def search(request):
    return render(request, 'flipzon/search.html')
    

def tracker(request):
    return render(request, 'flipzon/tracker.html')

def productview(request, myid):
    product = Product.objects.filter(product_id = myid)

    return render(request, 'flipzon/productview.html', {'product': product[0]} )

