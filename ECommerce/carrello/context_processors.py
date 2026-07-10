from django.db.models import Sum
from .models import CartItem , Cart

#TODO ricontrollarlo
def cart_count(request):
    if request.user.is_authenticated:
        count = CartItem.objects.filter(cart__user=request.user).aggregate(Sum('quantity'))['quantity__sum']
    else:
        count = 0
    return {'cart_count': count}