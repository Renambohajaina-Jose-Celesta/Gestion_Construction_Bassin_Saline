# Generated by Django 5.2 on 2025-04-13 07:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_projet_date_debut_alter_projet_date_fin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materiaux',
            name='Id_projet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.projet'),
        ),
    ]
