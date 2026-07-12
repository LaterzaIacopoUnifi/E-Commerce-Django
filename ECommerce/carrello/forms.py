from django import forms
from .models import Order

class CheckoutForm(forms.Form):
    PAY = (
        ('card', 'Carta di Credito'),
        ('paypal', 'PayPal'),
        ('cash', 'Contanti'),
    )
    shipping_address = forms.CharField(max_length=100, label="Indirizzo di spedizione")
    payment_method = forms.ChoiceField(choices=PAY, widget=forms.RadioSelect)

    class Meta :
        model = Order
        fields = (
            "Shipping Address" ,
            "Payment Method" ,
        )