from django.db import models

class BassinSalins(models.Model):
    Id_bassin = models.IntegerField(null=True, blank=True)
    Id_projet = models.IntegerField(null=True, blank=True)
    Id_volume = models.IntegerField(null=True, blank=True)
    Surface_bassin = models.IntegerField(null=True, blank=True)
    Capacite = models.IntegerField(null=True, blank=True)
    Date_construction = models.CharField(max_length=19, null=True, blank=True)

class Fournisseurs(models.Model):
    Id_fournisseur = models.IntegerField(null=True, blank=True)
    Nom_fournisseur = models.CharField(max_length=30, null=True, blank=True)
    Adr_fournisseur = models.CharField(max_length=37, null=True, blank=True)
    Tel_fournisseur = models.BigIntegerField(null=True, blank=True)

class Materiaux(models.Model):
    Id_materiau = models.IntegerField(null=True, blank=True)
    Nom_materiau = models.CharField(max_length=50, null=True, blank=True)
    Unite = models.CharField(max_length=50, null=True, blank=True)
    Quantite_stock = models.IntegerField(null=True, blank=True)

class Projet(models.Model):
    Id_projet = models.IntegerField(null=True, blank=True)
    Nom_projet = models.CharField(max_length=50, null=True, blank=True)
    Lieu = models.CharField(max_length=30, null=True, blank=True)
    Date_debut = models.CharField(max_length=19, null=True, blank=True)
    Date_fin = models.CharField(max_length=19, null=True, blank=True)

class Volumes(models.Model):
    Id_volume = models.IntegerField(null=True, blank=True)
    Volume_disponible = models.IntegerField(null=True, blank=True)
    Unite = models.CharField(max_length=15, null=True, blank=True)
