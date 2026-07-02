from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse , HttpResponseRedirect
from .models import Product , Description , Business

# Create your views here.


def index(request):
    productList = Product.objects.all()
    context = {"productList": productList}
    template = loader.get_template("main/index.html")
    return HttpResponse(template.render(context,request))