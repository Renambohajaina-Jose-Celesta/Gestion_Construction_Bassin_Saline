# Generated by Django 5.2 on 2025-04-11 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projet',
            name='Date_debut',
            field=models.DateField(max_length=19),
        ),
        migrations.AlterField(
            model_name='projet',
            name='Date_fin',
            field=models.DateField(max_length=19),
        ),
    ]
