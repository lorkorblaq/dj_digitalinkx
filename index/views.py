
# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import s_and_t_serializer
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.forms import UserCreationForm
from .utils import cookieCart
from django.views.generic import ListView, DetailView
# Create your views here.
def home(request):
    items = s_and_t.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, 
        ordered=False)
        items = order.orderitem_set.all()
        cartItems= order.get_cart_items
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total':0}
        cartItems=order['get_cart_items']
    items= s_and_t.objects.all()
    context = {
    'items': items,
    'cartItems':cartItems
    }
    return render(request, "home-page.html", context)

class s_and_t_views(viewsets.ModelViewSet):
    serializer_class = s_and_t_serializer
    queryset= s_and_t.objects.all

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
         'List':'/task-list/',
         'Detail View': '/task-detail/<str:p>/',
         'Create':'/task-create/',
         'Update':'/task-update/<str:pk>/',
         'Delete':'/task-delete/<str:pk>/',
    }


def s_and_tlist(request):
    s_and_t = s_and_t.objects.all()
    serializer = s_and_t_serializer(s_and_t, many=True)
    return Response(serializer.data)

def registerPage(request):
    form=UserCreationForm
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was Created for"+user)
            return redirect('loginPage')
    context= {'form':form}
    return render(request, "account/signup.html", context)

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "username or password is incorrect")
            
    context = {}
    return render(request, "account/login.html", context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, ordered=False)
        items = order.orderitem_set.all()
        cartItems= order.get_cart_items
    else:
        cookieData=cookieCart(request)
        cartItems=cookieData['cartItems']
        order=cookieData['order']
        items=cookieData['items']
    context = {'items': items, 'order':order, 'cartItems':cartItems}
    return render(request, "cart.html", context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, 
        ordered=False)
        items = order.orderitem_set.all()
        cartItems= order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_total':0}
        cartItems=order['get_cart_items']
        
    context = {'items': items, 'order':order,'cartItems':cartItems}
    return render(request, "checkout-page.html", context)

def updateitem(request):
    # print(request.data)
    data=json.loads(request.body)
    productId=data['productId']
    action = data['action']
    print("Action:", action)    
    print("Product:", productId)
    customer = request.user.customer    
    product= s_and_t.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, ordered=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, S_and_t=product)
    if action=='add':
        orderItem.quantity = (orderItem.quantity +1)
    elif action=='remove':
        orderItem.quantity=(orderItem.quantity -1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)
  

def services(request):
    items = s_and_t.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, 
        ordered=False)
        items = order.orderitem_set.all()
        cartItems= order.get_cart_items
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total':0}
        cartItems=order['get_cart_items']
    items= s_and_t.objects.all()
    context = {
    'items': items,
    'cartItems':cartItems
    }
    return render(request, "services.html", context)

def tools(request):
    items = s_and_t.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, 
        ordered=False)
        items = order.orderitem_set.all()
        cartItems= order.get_cart_items
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total':0}
        cartItems=order['get_cart_items']
    items= s_and_t.objects.all()
    context = {
    'items': items,
    'cartItems':cartItems
    }
    return render(request, "tools.html", context)



def blogger(request):
    items = s_and_t.objects.all()
    blogs= Blog.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, 
        ordered=False)
        items = order.orderitem_set.all()
        cartItems= order.get_cart_items
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total':0}
        cartItems=order['get_cart_items']

    context = {
    'items': items,
    'cartItems': cartItems,
    'blogs': blogs
    }
    return render(request, "blog.html", context)

class Bloghome(ListView):
    model=Blog
    template_name= "bloghome.html"

class Blogdetail(DetailView):
    model=Blog
    template_name= "blogdetail.html"