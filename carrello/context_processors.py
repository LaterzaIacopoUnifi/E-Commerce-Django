from django.db.models import Sum
from .models import CartItem, Cart, Order, OrderItem



def cart_count(request):
    if request.user.is_authenticated:
        count = CartItem.objects.filter(cart__user=request.user).aggregate(Sum('quantity'))['quantity__sum']
    else:
        count = 0
    return {'cart_count': count}


def order_count(request):
    if request.user.is_authenticated:
        count = Order.objects.filter(user=request.user).count()
    else:
        count = 0
    return {'order_count': count}

def orderitem_count(request):
    if request.user.is_authenticated:
        count = OrderItem.objects.filter(order__user=request.user).count()
    else:
        count = 0
    return {'orderitem_count': count}
