from django.urls import path
from . import views

app_name = "main"
urlpatterns= [

    path("", views.index, name="index"),
    path("registration/", views.register, name="reg"),
    path("login/", views.login_, name="login"),
    path("logout/", views.logout_, name="logout"),
    path("orders/", views.list_orders, name="list_orders"),
    path('search/', views.search_products, name="search_products"),
    path("product/<int:product_id>", views.product_detail, name="product_detail"),
    path("orders/<int:order_id>", views.view_order, name="view_order"),
    path("orders/delete/<int:order_id>", views.delete_order, name="delete_order"),
    path("delete/<int:product_id>", views.delete_product, name="delete_product"),


]