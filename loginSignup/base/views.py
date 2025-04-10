from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import BassinSalins, Fournisseurs, Materiaux, Projet, Volumes


@login_required
def home(request):
 return render(request, "home.html", {})


def authView(request):
 if request.method == "POST":
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
   form.save()
   return redirect("base:login")
 else:
  form = UserCreationForm()
 return render(request, "registration/signup.html", {"form": form})

def projets(request):
    projets_list = Projet.objects.all()
    return render(request, 'projets.html', {'projets': projets_list})

def bassins(request):
    bassins_list = BassinSalins.objects.all()
    return render(request, 'bassins.html', {'bassins': bassins_list})

def fournisseurs(request):
    fournisseurs_list = Fournisseurs.objects.all()
    return render(request, 'fournisseurs.html', {'fournisseurs': fournisseurs_list})

def materiaux(request):
    materiaux_list = Materiaux.objects.all()
    return render(request, 'materiaux.html', {'materiaux': materiaux_list})

def volumes(request):
    volumes_list = Volumes.objects.all()
    return render(request, 'volumes.html', {'volumes': volumes_list})