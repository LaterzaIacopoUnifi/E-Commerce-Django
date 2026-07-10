from django.contrib import admin
from .models import Product, Description, Business, NormalUser

# Register your models here.


admin.site.register(Product)
admin.site.register(Description)
admin.site.register(Business)
admin.site.register(NormalUser)

