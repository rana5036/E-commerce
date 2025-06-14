from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
from .models import Product,Categories
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import requests
# Create your views here.

def showland(request):

    if 'cart_count' not in request.session:
        request.session['cart_count']=0
    template=loader.get_template('landpage.html')
   
    categories=Categories.objects.all()

    data={
        'catgories':categories,
        'cart_count':request.session['cart_count']
    }
    return HttpResponse(template.render(data,request))

def list_product(request,id):
     if 'cart_count' not in request.session:
        request.session['cart_count']=0
     template=loader.get_template('list_products.html')
     products=Product.objects.filter(Categories_id=id)
     data={
          'product':products,
          'cart_count':request.session['cart_count']
     }
     return HttpResponse(template.render(data,request))


def product_details(request,id):
    if 'cart_count' not in request.session:
        request.session['cart_count']=0
    products=Product.objects.select_related('Categories').get(id=id)
  
    data={
          'cart_count':request.session['cart_count'],
          'products':products
     }
    template=loader.get_template('productdetails.html')

    return HttpResponse(template.render(data,request))

def add_to_cart(reauest):
    reauest.session['cart_count']=reauest.session.get('cart_count',0)+1
    reauest.session.modified=True
    return JsonResponse({'cart_count': reauest.session['cart_count']})
@csrf_exempt
@login_required
def checkout(request):
     if 'cart_count' not in request.session:
        request.session['cart_count']=0
     data={
          'cart_count':request.session['cart_count'],
     }
     template=loader.get_template('checkout.html')
     return HttpResponse(template.render(data,request))


def get_api(request):
     api_url='https://fakestoreapi.com/products'
     response=requests.get(api_url)
     if response.status_code==200:
         data=response.json()
     else: 
         data={"error":f"error:{response.status_code}"}
     print(data)
     return render(request,'get_api.html',{'api_data':data})




