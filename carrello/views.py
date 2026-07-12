from django.shortcuts import render , redirect, get_object_or_404
from .models import Cart, CartItem , Order , OrderItem
from django.template import loader
from django.http import HttpResponse , HttpResponseRedirect
from main.models import Product , NormalUser
from .forms import CheckoutForm

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
        print(f"L'utente {request.user.username} ha appena effettuato l'accesso!")

    cart_check = Cart.objects.filter(user=request.user).exists()
    if cart_check:
        cartUser = Cart.objects.get(user=request.user)
    else:
        cartUser = Cart.objects.create(user=request.user)

    items = CartItem.objects.filter(cart=cartUser).select_related('product')
    total_price = sum(item.total_price for item in items)
    context = {
        "items": items,
        "total_price": total_price
    }
    return render(request , 'carrello/carrello_page.html' , context)


def payment(request):
    cart = Cart.objects.get(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    total = sum(item.total_price for item in items)
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(user=request.user, total_amount=total)

            for item in items:
                OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)

            items.delete()

            return render(request, 'carrello/pagamento_effettuato.html')
    else:
        form = CheckoutForm()

    context = {
        "items": items,
        "total": total,
        "form": form
    }
    return render(request, 'carrello/pagamento.html', context)


