from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import FournisseurForm, MateriauForm, ProjetForm

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
        else:
            # Vous pouvez gérer les erreurs ici si nécessaire
            return render(request, 'pages/projets.html', {'form': form, 'projets': Projet.objects.all()})
    return redirect('base:projets')

@login_required
def projet_edit(request, pk):
    projet = get_object_or_404(Projet, pk=pk)
    if request.method == "POST":
        form = ProjetForm(request.POST, instance=projet)
        if form.is_valid():
            form.save()
            return redirect('base:projets')
    else:
        form = ProjetForm(instance=projet)
    
    return render(request, 'pages/projets.html', {'form': form, 'projets': Projet.objects.all()})

@login_required
def delete_projet(request, pk):
    projet = get_object_or_404(Projet, pk=pk)
    if request.method == 'POST':
        projet.delete()
        return redirect('base:projets')
 

def bassins(request):
    bassins_list = BassinSalins.objects.all()
    return render(request, 'pages/bassins.html', {'bassins': bassins_list})

def fournisseurs(request):
    fournisseurs = Fournisseurs.objects.all()
    paginator = Paginator(fournisseurs, 10)  # Affiche 10 fournisseurs par page
    page_number = request.GET.get('page')
    fournisseurs = paginator.get_page(page_number)
    return render(request, 'pages/fournisseurs.html', {'fournisseurs': fournisseurs})

def fournisseur_add(request):
    if request.method == "POST":
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Fournisseur ajouté avec succès.")
            return redirect('base:fournisseurs')
    return redirect('base:fournisseurs')

def fournisseur_edit(request, pk):
    fournisseur = get_object_or_404(Fournisseurs, pk=pk)
    if request.method == "POST":
        form = FournisseurForm(request.POST, instance=fournisseur)
        if form.is_valid():
            form.save()
            messages.success(request, "✏️ Fournisseur modifié avec succès.")
            return redirect('base:fournisseurs')
    return redirect('base:fournisseurs')

def fournisseur_delete(request, pk):
    fournisseur = get_object_or_404(Fournisseurs, pk=pk)
    if request.method == "POST":
        fournisseur.delete()
        messages.success(request, "🗑️ Fournisseur supprimé avec succès.")
        return redirect('base:fournisseurs')
    return redirect('base:fournisseurs')

def materiaux(request):
    materiaux_list = Materiaux.objects.all()
    paginator = Paginator(materiaux_list, 10)  # Affiche 10 matériaux par page
    page_number = request.GET.get('page')
    materiaux = paginator.get_page(page_number)
    return render(request, 'pages/materiaux.html', {'materiaux': materiaux})

def materiau_add(request):
    if request.method == "POST":
        form = MateriauForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base:materiaux')
    else:
        form = MateriauForm()
    return render(request, 'pages/materiaux.html', {'form': form})

def materiau_edit(request, pk):
    materiau = get_object_or_404(Materiaux, pk=pk)
    if request.method == "POST":
        form = MateriauForm(request.POST, instance=materiau)
        if form.is_valid():
            form.save()
            return redirect('base:materiaux')
    else:
        form = MateriauForm(instance=materiau)
    return render(request, 'pages/materiaux.html', {'form': form, 'materiau': materiau})

def materiau_delete(request, pk):
    materiau = get_object_or_404(Materiaux, pk=pk)
    if request.method == "POST":
        materiau.delete()
        return redirect('base:materiaux_list')
    return render(request, 'pages/materiaux.html', {'materiau': materiau})

def volumes(request):
    volumes_list = Volumes.objects.all()
    return render(request, 'pages/volumes_eaux.html', {'volumes': volumes_list})