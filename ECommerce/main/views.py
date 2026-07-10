from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.http import HttpResponse , HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from .models import NormalUser , Product , Description , Business
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from .forms import UserForm


# Create your views here.


def index(request):
    if request.session.pop('just_logged_in', False):
        messaggio = "Benvenuto! Sei appena entrato nel sito."
        print(f"Un nuovo utente ha appena effettuato l'accesso!")
    else:
        messaggio = "Bentornato."
        print(f"L'utente {NormalUser.username} ha appena effettuato l'accesso!")

    productList = Product.objects.all()
    context = {"productList": productList}
    template = loader.get_template("main/index.html")
    return HttpResponse(template.render(context,request))


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect("main:index")
    else:
        form = UserForm()
    return render(request, 'main/reg.html', {'form': form})


def login_(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("main:index")
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

def logout_(request):
    logout(request)
    return redirect("main:index")


# def vote(request,question_id):
#     user = get_object_or_404(NormalUser, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST["choice"])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(
#             request,
#             "polls/detail.html",
#             {
#                 "question": question,
#                 "error_message": "You didn't select a choice.",
#             },
#         )
#     else:
#         selected_choice.votes = F("votes") + 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))