from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .forms import ProjetForm

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

@login_required
def projets(request):
    projets_list = Projet.objects.all()
    return render(request, 'pages/projets.html', {'projets': projets_list})

@login_required
def projet_add(request):
    if request.method == "POST":
        form = ProjetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base:projets')
    return redirect('base:projets')  # Redirection même si le formulaire n'est pas valide

@login_required
def projet_edit(request, pk):
    projet = get_object_or_404(Projet, pk=pk)
    if request.method == "POST":
        form = ProjetForm(request.POST, instance=projet)
        if form.is_valid():
            form.save()
            return redirect('projets')

@login_required
def projet_delete(request, pk):
    projet = get_object_or_404(Projet, pk=pk)
    if request.method == "POST":
        projet.delete()
        return redirect('base:projets')
    return render('base:projets')

def bassins(request):
    bassins_list = BassinSalins.objects.all()
    return render(request, 'pages/bassins.html', {'bassins': bassins_list})

def fournisseurs(request):
    fournisseurs_list = Fournisseurs.objects.all()
    return render(request, 'pages/fournisseurs.html', {'fournisseurs': fournisseurs_list})

def materiaux(request):
    materiaux_list = Materiaux.objects.all()
    return render(request, 'pages/materiaux.html', {'materiaux': materiaux_list})

def volumes(request):
    volumes_list = Volumes.objects.all()
    return render(request, 'pages/volumes_eaux.html', {'volumes': volumes_list})