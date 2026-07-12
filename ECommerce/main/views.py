from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.http import HttpResponse , HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from .models import NormalUser , Product , Description , Business
from carrello.models import Order, OrderItem
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserForm


# Create your views here.

def index(request):
    if request.session.pop('just_logged_in', False):
        messaggio = "Benvenuto! Sei appena entrato nel sito."
        print(f"Un nuovo utente ha appena effettuato l'accesso!")
    else:
        messaggio = "Bentornato."
        print(f"L'utente {request.user.username} ha appena effettuato l'accesso!")

    query = request.GET.get('q', '')
    productList = Product.objects.all()
    placeholder_text = "Cerca un prodotto..."
    context = {
        "productList": productList,
        "query" : query ,
        "placeholder" : placeholder_text
    }
    template = loader.get_template("main/index.html")
    return HttpResponse(template.render(context,request))


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect("main:index")
    else:
        form = UserForm()
    return render(request, 'main/reg.html', {'form': form})


def login_(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("main:index")
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

def logout_(request):
    logout(request)
    return redirect("main:index")

def list_orders(request):
    orders = Order.objects.filter(user=request.user)
    context = {
        "orders": orders,
    }
    return render(request, 'main/orders.html', context)

def view_order(request, order_id):
    order = get_object_or_404(Order, user=request.user, id=order_id)
    productList = OrderItem.objects.filter(order=order)
    context = {
        "order": order,
        "productList" : productList,
    }
    return render(request, 'main/order_detail.html', context)

def search_products(request):
    query = request.GET.get('q', '')
    results = Product.objects.all()

    if query:
        productList = results.filter(name__icontains=query)
        context = {
            "productList": productList,
            "query": query,
            "placeholder" : query
        }
        template = loader.get_template("main/index.html")
        return HttpResponse(template.render(context, request))


    return redirect('main:index')


@login_required
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order.delete()

    return redirect('main:list_orders')

