from django.urls import path, include
from .views import (
    authView,
    bassins,
    fournisseur_add,
    fournisseur_delete,
    fournisseur_edit,
    fournisseurs,
    home,
    materiau_add,
    materiau_delete,
    materiau_edit,
    materiaux,
    projet_add,
    delete_projet,
    projet_edit,
    projets,
    volumes,
)

urlpatterns = [
    path("", home, name="home"),
    path('projets/', projets, name='projets'),
    path('projets/add/', projet_add, name='projet_add'),  # Assurez-vous que cette ligne est présente
    path('projets/edit/<int:pk>/', projet_edit, name='projet_edit'),
   path('projets/delete/<int:pk>/', delete_projet, name='projet_delete'),
    path('bassins/', bassins, name='bassins'),
    path('fournisseurs/', fournisseurs, name='fournisseurs'),
    path('fournisseurs/add/', fournisseur_add, name='fournisseur_add'),
    path('fournisseurs/edit/<int:pk>/', fournisseur_edit, name='fournisseur_edit'),
    path('fournisseurs/delete/<int:pk>/', fournisseur_delete, name='fournisseur_delete'),
    path('materiaux/', materiaux, name='materiaux'),
    path('materiaux/add/', materiau_add, name='materiau_add'),
    path('materiaux/edit/<int:pk>/', materiau_edit, name='materiau_edit'),
    path('materiaux/delete/<int:pk>/', materiau_delete, name='materiau_delete'),
    path('volumes/', volumes, name='volumes'),
    path("signup/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
]