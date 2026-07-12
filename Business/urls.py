from django.urls import path
from . import views

app_name = "Business"
urlpatterns= [

    path("", views.business_page, name="business_page"),
    path("addP/", views.add_product, name="add_product"),
    path("addB/", views.add_business, name="add_business"),
    path("choiceB/", views.choice_business, name="choice_business"),
    path("business/<int:business_id>", views.business_listproduct, name="business_listproduct"),

]

