from django import forms
from .models import Fournisseurs, Materiaux, Projet

class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields = ['Nom_projet', 'Description', 'Date_debut', 'Date_fin', 'Dure']

class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseurs
        fields = ['Nom_fournisseur', 'Adr_fournisseur', 'Tel_fournisseur']

class MateriauForm(forms.ModelForm):
    class Meta:
        model = Materiaux
        fields = ['Nom_materiau', 'Unite', 'Quantite_stock', 'Id_projet']