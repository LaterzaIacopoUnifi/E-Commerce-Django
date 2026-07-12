from django import forms
from django.db.models import Model
from main.models import Product, Description , Business , NormalUser



class AddProductForm(forms.Form):
    nome = forms.CharField(max_length=100, label="Nome del Prodotto")
    costo = forms.DecimalField(max_digits=10, decimal_places=2, label="Prezzo (€)")

    descrizione = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), label="Descrizione del Prodotto")

    def save(self, business_instance):
        new_product = Product.objects.create(
            name=self.cleaned_data['nome'],
            cost=self.cleaned_data['costo'],
            business=business_instance
        )

        Description.objects.create(
            product=new_product,
            description=self.cleaned_data['descrizione'],
            vote=0
        )

        return new_product


class AddBusinessForm(forms.Form):
    nome = forms.CharField(max_length=200, label="Nome Azienda")
    descrizione = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), label="Descrizione del Prodotto")

    def save(self, owner_instance):
        new_business = Business.objects.create(
            name=self.cleaned_data['nome'],
            description=self.cleaned_data['descrizione'],
            owner = owner_instance
        )

        return new_business


class ChoiceBusinessForm(forms.Form):

    def save(self,user , new_business):
        business_obj = Business.objects.filter(id=new_business).first()
        if business_obj:
            user.business = business_obj
            user.save()

        return user