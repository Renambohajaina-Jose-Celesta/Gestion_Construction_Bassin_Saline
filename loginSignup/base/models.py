from django.db import models

class Projet(models.Model):
    Id_projet = models.AutoField(primary_key=True)  # Clé primaire auto-incrémentée
    Nom_projet = models.CharField(max_length=50)
    Lieu = models.CharField(max_length=30)
    Date_debut = models.DateField(max_length=19)
    Date_fin = models.DateField(max_length=19)

class Volumes(models.Model):
    Id_volume = models.AutoField(primary_key=True)  # Clé primaire auto-incrémentée
    Volume_disponible = models.IntegerField(null=True, blank=True)
    Unite = models.CharField(max_length=15, null=True, blank=True)

class BassinSalins(models.Model):
    Id_bassin = models.AutoField(primary_key=True)  # Clé primaire auto-incrémentée
    Id_projet = models.ForeignKey(Projet, on_delete=models.CASCADE, null=True, blank=True)  # Clé étrangère vers Projet
    Id_volume = models.ForeignKey(Volumes, on_delete=models.CASCADE, null=True, blank=True)  # Clé étrangère vers Volumes
    Surface_bassin = models.IntegerField(null=True, blank=True)
    Capacite = models.IntegerField(null=True, blank=True)
    Date_construction = models.CharField(max_length=19, null=True, blank=True)

class Fournisseurs(models.Model):
    Id_fournisseur = models.AutoField(primary_key=True)  # Clé primaire auto-incrémentée
    Nom_fournisseur = models.CharField(max_length=30)
    Adr_fournisseur = models.CharField(max_length=37)
    Tel_fournisseur = models.BigIntegerField(null=True, blank=True)

class Materiaux(models.Model):
    Id_materiau = models.AutoField(primary_key=True)  # Clé primaire auto-incrémentée
    Nom_materiau = models.CharField(max_length=50)
    Unite = models.CharField(max_length=50)
    Quantite_stock = models.IntegerField(null=True, blank=True)