from django.db import models
from django.db.models import Sum
from main.models import NormalUser , Product
from django.shortcuts import get_object_or_404

# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField(NormalUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrello di {self.user.username}"



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    @property
    def total_price(self):
        return self.quantity * self.product.cost



class Order(models.Model):
    PAY = (
        ('card', 'Carta di Credito'),
        ('paypal', 'PayPal'),
        ('cash', 'Contanti'),
    )
    user = models.ForeignKey(NormalUser, on_delete=models.CASCADE)
    shipping_address = models.TextField(max_length=100,default="")
    payment_method = models.CharField(max_length=20, choices=PAY)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ordine di {self.user.username} fatto il {self.created_at}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    @property
    def total_items_count(self):
        total = self.items.aggregate(Sum('quantity'))['quantity__sum']
        return total if total else 0

