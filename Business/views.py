from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django import forms
from main.models import Business , Product , Description, NormalUser

from .forms import AddProductForm, AddBusinessForm , ChoiceBusinessForm
from django.template import loader
from django.http import HttpResponse , HttpResponseRedirect


# Create your views here.





@login_required
def business_page(request):
    my_business = request.user.owned_businesses.all()
    all_business = Business.objects.all()
    form_add_product = AddProductForm()
    form_add_business = AddBusinessForm()
    form_choice_business = ChoiceBusinessForm()
    possible_owners = NormalUser.objects.all()

    context = {
        "formP": form_add_product,
        "formB": form_add_business,
        "all_business":all_business,
        "my_business": my_business ,
        "possible_owners" : possible_owners,
        "formC": form_choice_business
    }
    return render(request, 'Business/business_page.html', context)


@login_required
def add_product(request):
    my_business = request.user.owned_businesses.all()

    if request.method == 'POST':

        form_add_product = AddProductForm(request.POST)
        business_id = request.POST.get('business_id')
        business_scelta = my_business.filter(id=business_id).first()
        if form_add_product.is_valid() and business_scelta:
            text_description = form_add_product.cleaned_data['descrizione']
            new_product = Product.objects.create(name=form_add_product.cleaned_data['nome'],
                                                 cost=form_add_product.cleaned_data['costo'],
                                                 business=business_scelta)
            Description.objects.create(product=new_product,
                                       description=text_description,
                                       vote=0)
            print(f"L'oggetto {new_product.name} è appena stato aggiunto!")
    return redirect('business:business_page')

@login_required
def add_business(request):

    if request.method == 'POST':

        form_add_business = AddBusinessForm(request.POST)
        owner_id = request.POST.get('owner_id')
        owner_scelta = NormalUser.objects.filter(id=owner_id).first()
        if form_add_business.is_valid():
            Business.objects.create(
                name=form_add_business.cleaned_data['nome'],
                description=form_add_business.cleaned_data['descrizione'],
                owner=owner_scelta,
            )
        else:
            print("qualcosa è andato storto")

    return redirect('business:business_page')


@login_required
def choice_business(request):

    if request.method == 'POST':

        form_choice_business = ChoiceBusinessForm(request.POST)
        business_id = request.POST.get('business_id')
        if form_choice_business.is_valid():
            form_choice_business.save(request.user,business_id)
        else:
            print("qualcosa è andato storto")

    return redirect('business:business_page')