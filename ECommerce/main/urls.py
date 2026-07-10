from django.urls import path
from . import views

app_name = "main"
urlpatterns= [

    path("", views.index, name="index"),
    path("registration/", views.register, name="reg"),
    path("login/", views.login_, name="login"),
    path("logout/", views.logout_, name="logout"),

]