from django.db import models

from datetime import timedelta

class Projet(models.Model):
    Id_projet = models.AutoField(primary_key=True)
    Nom_projet = models.CharField(max_length=50)
    Description = models.CharField(max_length=100, null=True)
    Date_debut = models.DateField()
    Date_fin = models.DateField()
    Dure = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.Date_debut and self.Date_fin:
            self.Dure = (self.Date_fin - self.Date_debut).days
        super().save(*args, **kwargs)


class Volumes(models.Model):
    Id_volume = models.AutoField(primary_key=True)
    Volume_disponible = models.IntegerField(null=True, blank=True)  # en litres
    date_mesure = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.Volume_disponible} litres"


class BassinSalins(models.Model):
    Id_bassin = models.AutoField(primary_key=True)
    Id_projet = models.ForeignKey('Projet', on_delete=models.CASCADE, null=True, blank=True)
    Id_volume = models.ForeignKey('Volumes', on_delete=models.CASCADE, null=True, blank=True)
    Surface_bassin = models.IntegerField(null=True, blank=True)
    Capacite = models.IntegerField(null=True, blank=True)
    Date_construction = models.DateField(null=True, blank=True)
    Nb_bassin = models.IntegerField(null=True, blank=True)
    Sel_produit = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Bassin {self.Id_bassin}"


class Fournisseurs(models.Model):
    Id_fournisseur = models.AutoField(primary_key=True)
    Nom_fournisseur = models.CharField(max_length=30, default='Non spécifiée')
    Adr_fournisseur = models.CharField(max_length=37, default='Non spécifiée')  # Valeur par défaut ajoutée
    Tel_fournisseur = models.BigIntegerField(null=True, blank=True)

class Materiaux(models.Model):
    Id_materiau = models.AutoField(primary_key=True)  # Clé primaire auto-incrémentée
    Id_projet = models.ForeignKey(Projet, on_delete=models.SET_NULL, null=True, blank=True)
    Nom_materiau = models.CharField(max_length=50, default='Non spécifiée')
    Unite = models.CharField(max_length=50, default='Non spécifiée')
    Quantite_stock = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.Nom_materiau