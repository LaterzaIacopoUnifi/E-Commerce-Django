from django.urls import path
from . import views

app_name = 'carrello'
urlpatterns = [
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.page_cart, name ='page_cart'),
    path('pagamento/', views.payment, name ='payment'),
]