from django import forms
from .models import Fournisseurs, Materiaux, Projet, Volumes, BassinSalins

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

class VolumeForm(forms.ModelForm):
    class Meta:
        model = Volumes
        fields = ['Volume_disponible', 'date_mesure']

class BassinSalinsForm(forms.ModelForm):
    class Meta:
        model = BassinSalins
        fields = ['Id_projet', 'Id_volume', 'Surface_bassin', 'Capacite', 'Date_construction', 'Nb_bassin', 'Sel_produit']