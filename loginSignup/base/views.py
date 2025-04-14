from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from requests import Response
from .forms import BassinSalinsForm, FournisseurForm, MateriauForm, ProjetForm, VolumeForm

from .models import BassinSalins, Fournisseurs, Materiaux, Projet, Volumes
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm


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

def logout(request):
    auth_logout(request)
    return redirect('base:home')


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


@login_required
def bassins(request):
    # Récupérer tous les bassins
    bassins_list = BassinSalins.objects.all().order_by('Id_bassin')  # Tri par ID croissant
    
    # Pagination - 10 bassins par page
    paginator = Paginator(bassins_list, 10)
    page_number = request.GET.get('page')
    bassins_page = paginator.get_page(page_number)
    
    # Récupérer les projets et volumes pour les formulaires
    projets = Projet.objects.all()
    volumes = Volumes.objects.all()
    
    return render(request, 'pages/bassins.html', {
        'bassins': bassins_page,  # Notez que nous passons l'objet page, pas la liste complète
        'projets': projets,
        'volumes': volumes,
    })

@login_required
def bassin_add(request):
    if request.method == "POST":
        form = BassinSalinsForm(request.POST)
        if form.is_valid():
            bassin = form.save(commit=False)

            # Récupérer les objets liés
            projet = bassin.Id_projet
            volume = bassin.Id_volume

            # Obtenir la valeur Volume_disponible à partir de l'objet lié
            volume_total = volume.Volume_disponible or 0
            capacite = bassin.Capacite or 1  # éviter division par 0

            # Calcul Nb_bassin (équivalent IIf(Int(volume/capacité) <= 0, 1, Int(...)))
            try:
                calc_bassin = int(volume_total / capacite)
            except ZeroDivisionError:
                calc_bassin = 0

            nb_bassin = 1 if calc_bassin <= 0 else calc_bassin

            # Calcul Sel_produit = ((5×8×capacité×35)/1000) × nb_bassin
            sel_produit = ((5 * 8 * capacite * 35) / 1000) * nb_bassin

            # Affecter les valeurs
            bassin.Nb_bassin = nb_bassin
            bassin.Sel_produit = sel_produit

            # Sauvegarder le bassin
            bassin.save()

            messages.success(request, "Bassin ajouté avec succès.")
            return redirect('base:bassins')
        else:
            projets = Projet.objects.all()
            volumes = Volumes.objects.all()
            bassins_list = BassinSalins.objects.all()

            return render(request, 'pages/bassins.html', {
                'form': form,
                'projets': projets,
                'volumes': volumes,
                'bassins': bassins_list,
                'form_errors': form.errors,
            })

    return redirect('base:bassins')


@login_required
def bassin_edit(request, pk):
    bassin = get_object_or_404(BassinSalins, pk=pk)
    if request.method == "POST":
        form = BassinSalinsForm(request.POST, instance=bassin)
        if form.is_valid():
            # Sauvegarder les modifications du bassin
            bassin = form.save(commit=False)

            # Récupérer les objets liés
            projet = bassin.Id_projet
            volume = bassin.Id_volume

            # Obtenir la valeur Volume_disponible à partir de l'objet lié
            volume_total = volume.Volume_disponible or 0
            capacite = bassin.Capacite or 1  # éviter division par 0

            # Calcul Nb_bassin (équivalent IIf(Int(volume/capacité) <= 0, 1, Int(...)))
            try:
                calc_bassin = int(volume_total / capacite)
            except ZeroDivisionError:
                calc_bassin = 0

            nb_bassin = 1 if calc_bassin <= 0 else calc_bassin

            # Calcul Sel_produit = ((5×8×capacité×35)/1000) × nb_bassin
            sel_produit = ((5 * 8 * capacite * 35) / 1000) * nb_bassin

            # Affecter les nouvelles valeurs calculées
            bassin.Nb_bassin = nb_bassin
            bassin.Sel_produit = sel_produit

            # Sauvegarder le bassin mis à jour
            bassin.save()

            messages.success(request, "Bassin modifié avec succès.")
            return redirect('base:bassins')
        else:
            projets = Projet.objects.all()
            volumes = Volumes.objects.all()
            bassins_list = BassinSalins.objects.all()

            return render(request, 'pages/bassins.html', {
                'form': form,
                'projets': projets,
                'volumes': volumes,
                'bassins': bassins_list,
                'form_errors': form.errors,
            })
    else:
        form = BassinSalinsForm(instance=bassin)

    projets = Projet.objects.all()
    volumes = Volumes.objects.all()

    return render(request, 'pages/bassins.html', {
        'form': form,
        'projets': projets,
        'volumes': volumes,
        'bassins': BassinSalins.objects.all(),
    })

@login_required
def bassin_delete(request, pk):
    bassin = get_object_or_404(BassinSalins, pk=pk)
    if request.method == "POST":
        bassin.delete()
        messages.success(request, "Bassin supprimé avec succès.")
        return redirect('base:bassins')
    return render(request, 'pages/bassins.html', {'bassin': bassin})



@login_required
def fournisseurs(request):
    fournisseurs = Fournisseurs.objects.all()
    paginator = Paginator(fournisseurs, 10)  # Affiche 10 fournisseurs par page
    page_number = request.GET.get('page')
    fournisseurs = paginator.get_page(page_number)
    return render(request, 'pages/fournisseurs.html', {'fournisseurs': fournisseurs})


@login_required
def fournisseur_add(request):
    if request.method == "POST":
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Fournisseur ajouté avec succès.")
            return redirect('base:fournisseurs')
    return redirect('base:fournisseurs')



@login_required
def fournisseur_edit(request, pk):
    fournisseur = get_object_or_404(Fournisseurs, pk=pk)
    if request.method == "POST":
        form = FournisseurForm(request.POST, instance=fournisseur)
        if form.is_valid():
            form.save()
            messages.success(request, "✏️ Fournisseur modifié avec succès.")
            return redirect('base:fournisseurs')
    return redirect('base:fournisseurs')


@login_required
def fournisseur_delete(request, pk):
    fournisseur = get_object_or_404(Fournisseurs, pk=pk)
    if request.method == "POST":
        fournisseur.delete()
        messages.success(request, "🗑️ Fournisseur supprimé avec succès.")
        return redirect('base:fournisseurs')
    return redirect('base:fournisseurs')


@login_required
def materiaux(request):
    materiaux_list = Materiaux.objects.all()
    paginator = Paginator(materiaux_list, 10)  # Affiche 10 matériaux par page
    page_number = request.GET.get('page')
    materiaux = paginator.get_page(page_number)
    
    projets = Projet.objects.all()
    
    return render(request, 'pages/materiaux.html', {
        'materiaux': materiaux,
        'projets': projets
    })


@login_required
def materiau_add(request):
    if request.method == "POST":
        # Affichez les données du formulaire dans la console pour le débogage
        print(request.POST)  # Ajoutez cette ligne pour voir les données envoyées

        nom = request.POST.get('Nom_materiau')
        unite = request.POST.get('Unite')
        quantite = request.POST.get('Quantite_stock') or None
        id_projet = request.POST.get('Id_projet')  # Assurez-vous que c'est bien 'Id_projet'

        # Vérifiez si l'ID du projet est fourni
        if id_projet:
            try:
                projet = Projet.objects.get(Id_projet=id_projet)  # Utilisez 'Id_projet' pour la recherche
            except Projet.DoesNotExist:
                projet = None
                messages.error(request, "Le projet sélectionné n'existe pas.")
                return redirect('base:materiaux')
        else:
            projet = None
            messages.error(request, "Veuillez sélectionner un projet.")
            return redirect('base:materiaux')

        # Créez le matériau
        Materiaux.objects.create(
            Nom_materiau=nom,
            Unite=unite,
            Quantite_stock=quantite,
            Id_projet=projet
        )

        messages.success(request, "Matériau ajouté avec succès.")
        return redirect('base:materiaux')

@login_required
def materiau_edit(request, pk):
    materiau = get_object_or_404(Materiaux, pk=pk)
    
    if request.method == "POST":
        nom = request.POST.get('Nom_materiau')
        unite = request.POST.get('Unite')
        quantite = request.POST.get('Quantite_stock') or None
        id_projet = request.POST.get('Id_projet')  # Récupérer l'ID du projet

        # Vérifiez si l'ID du projet est fourni
        if id_projet:
            try:
                projet = Projet.objects.get(Id_projet=id_projet)  # Utilisez 'Id_projet' pour la recherche
            except Projet.DoesNotExist:
                projet = None
                messages.error(request, "Le projet sélectionné n'existe pas.")
                return redirect('base:materiaux')
        else:
            projet = None
            messages.error(request, "Veuillez sélectionner un projet.")
            return redirect('base:materiaux')

        # Mettez à jour le matériau
        materiau.Nom_materiau = nom
        materiau.Unite = unite
        materiau.Quantite_stock = quantite
        materiau.Id_projet = projet
        materiau.save()

        messages.success(request, "Matériau modifié avec succès.")
        return redirect('base:materiaux')

    # Si la méthode n'est pas POST, affichez le formulaire avec les données existantes
    return render(request, 'pages/materiaux.html', {
        'materiau': materiau,
        'projets': Projet.objects.all()  # Récupérez tous les projets pour le formulaire
    })

@login_required
def materiau_delete(request, pk):
    materiau = get_object_or_404(Materiaux, pk=pk)
    if request.method == "POST":
        materiau.delete()
        return redirect('base:materiaux')
    return render(request, 'pages/materiaux.html', {'materiau': materiau})


@login_required
def volumes(request):
    volumes_list = Volumes.objects.all()
    return render(request, 'pages/volumes_eaux.html', {'volumes': volumes_list})

@login_required
def volume_add(request):
    if request.method == 'POST':
        form = VolumeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Volume ajouté avec succès.")
            return redirect('base:volumes')
    else:
        form = VolumeForm()
    return render(request, 'pages/volumes_eaux.html', {'form': form})


@login_required
def volume_edit(request, pk):
    volume_obj = get_object_or_404(Volumes, pk=pk)
    if request.method == 'POST':
        form = VolumeForm(request.POST, instance=volume_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Volume modifié avec succès.")
            return redirect('base:volumes')
    else:
        form = VolumeForm(instance=volume_obj)
    return render(request, 'pages/volumes_eaux.html', {'form': form, 'volumes': Volumes.objects.all()})


@login_required
def volume_delete(request, pk):
    volume_obj = get_object_or_404(Volumes, pk=pk)
    volume_obj.delete()
    messages.success(request, "Volume supprimé avec succès.")
    return redirect('base:volumes')


from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Paragraph, Image, Spacer, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen.canvas import Canvas
import os

class FooterCanvas(Canvas):
    def __init__(self, *args, **kwargs):
        Canvas.__init__(self, *args, **kwargs)
        self.pages = []

    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        for page in self.pages:
            self.__dict__.update(page)
            self.draw_footer()
            Canvas.showPage(self)
        Canvas.save(self)

    def draw_footer(self):
        page_num = self._pageNumber
        text = f"Page {page_num}"
        self.setFont("Helvetica", 8)
        self.drawRightString(200 * mm, 10 * mm, text)

@login_required
def bassin_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="bassins.pdf"'

    # Ajustement des marges (réduites pour une mise en page plus étroite)
    doc = SimpleDocTemplate(
        response,
        pagesize=A4,
        rightMargin=20,  # Marges plus petites
        leftMargin=20,   # Marges plus petites
        topMargin=40,    # Marges plus petites
        bottomMargin=20  # Marges plus petites
    )

    elements = []
    styles = getSampleStyleSheet()

    # Style personnalisé pour cellules (y compris Projet)
    cell_style = ParagraphStyle(
        name='CellStyle',
        fontSize=8,
        alignment=0,  # align left
        leading=10
    )

    # Logo (optionnel)
    logo_path = os.path.join("static", "img", "logo.png")
    if os.path.exists(logo_path):
        logo = Image(logo_path, width=50, height=50)
        elements.append(logo)

    # Titre
    elements.append(Paragraph("Liste des Bassins", styles['Title']))
    elements.append(Spacer(1, 12))

    # En-têtes
    data = [[
        'ID', 'Projet', "Volume d'eaux", 'Surface (m²)', 
        'Capacité (l)', 'Date de const', 'Nb de bassins', 'Sel produit (t)'
    ]]

    # Données
    bassins = BassinSalins.objects.all()
    for bassin in bassins:
        projet_nom = Paragraph(bassin.Id_projet.Nom_projet, cell_style) if bassin.Id_projet else 'N/A'
        volume_eaux = bassin.Id_volume.Volume_disponible if bassin.Id_volume else 'N/A'
        surface = bassin.Surface_bassin or 0
        capacite = bassin.Capacite or 0
        date_construction = bassin.Date_construction.strftime('%d/%m/%Y') if bassin.Date_construction else 'N/A'
        nb_bassins = bassin.Nb_bassin or 0
        sel_produit = f"{bassin.Sel_produit:.2f}" if bassin.Sel_produit else 'N/A'

        data.append([
            bassin.Id_bassin,
            projet_nom,
            volume_eaux,
            surface,
            capacite,
            date_construction,
            nb_bassins,
            sel_produit
        ])

    # Colonnes ajustées
    col_widths = [30, 110, 75, 55, 55, 70, 50, 70]

    table = Table(data, colWidths=col_widths, repeatRows=1)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#4F81BD")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (1, 1), (1, -1), 'LEFT'),  # Colonne Projet à gauche
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#E7E6E6")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ]))

    elements.append(KeepTogether(table))

    # Génération du PDF avec pagination
    doc.build(elements, canvasmaker=FooterCanvas)
    return response
