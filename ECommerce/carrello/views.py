from django.shortcuts import render , redirect, get_object_or_404
from .models import Cart, CartItem
from django.template import loader
from django.http import HttpResponse , HttpResponseRedirect
from main.models import Product , NormalUser

# Create your views here.


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart_check = Cart.objects.filter(user=request.user).exists()

    if cart_check:
        cart = Cart.objects.get(user=request.user)
    else:
        cart = Cart.objects.create(user=request.user)

    cart_item_check = CartItem.objects.filter(cart=cart, product=product).exists()

    if cart_item_check:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item = CartItem.objects.create(cart=cart, product=product)


    return redirect('main:index')


def page_cart(request):
    if request.session.pop('just_logged_in', False):
        messaggio = "Benvenuto! Sei appena entrato nel sito."
        print(f"Un nuovo utente ha appena effettuato l'accesso!")
    else:
        messaggio = "Bentornato."
        print(f"L'utente {NormalUser.username} ha appena effettuato l'accesso!")

    cartUser = Cart.objects.get(user=request.user)
    items = CartItem.objects.filter(cart=cartUser).select_related('product')
    return render(request , 'carrello/carrello_page.html' , {'items' : items})
