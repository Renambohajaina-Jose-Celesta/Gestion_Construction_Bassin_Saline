# Generated by Django 5.2 on 2025-04-10 11:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fournisseurs',
            fields=[
                ('Id_fournisseur', models.AutoField(primary_key=True, serialize=False)),
                ('Nom_fournisseur', models.CharField(blank=True, max_length=30, null=True)),
                ('Adr_fournisseur', models.CharField(blank=True, max_length=37, null=True)),
                ('Tel_fournisseur', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Materiaux',
            fields=[
                ('Id_materiau', models.AutoField(primary_key=True, serialize=False)),
                ('Nom_materiau', models.CharField(blank=True, max_length=50, null=True)),
                ('Unite', models.CharField(blank=True, max_length=50, null=True)),
                ('Quantite_stock', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('Id_projet', models.AutoField(primary_key=True, serialize=False)),
                ('Nom_projet', models.CharField(max_length=50)),
                ('Lieu', models.CharField(max_length=30)),
                ('Date_debut', models.CharField(max_length=19)),
                ('Date_fin', models.CharField(max_length=19)),
            ],
        ),
        migrations.CreateModel(
            name='Volumes',
            fields=[
                ('Id_volume', models.AutoField(primary_key=True, serialize=False)),
                ('Volume_disponible', models.IntegerField(blank=True, null=True)),
                ('Unite', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BassinSalins',
            fields=[
                ('Id_bassin', models.AutoField(primary_key=True, serialize=False)),
                ('Surface_bassin', models.IntegerField(blank=True, null=True)),
                ('Capacite', models.IntegerField(blank=True, null=True)),
                ('Date_construction', models.CharField(blank=True, max_length=19, null=True)),
                ('Id_projet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.projet')),
                ('Id_volume', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.volumes')),
            ],
        ),
    ]
