from django.urls import path, include
from .views import (
    authView,
    bassins,
    fournisseurs,
    home,
    materiaux,
    projet_add,
    projet_delete,
    projet_edit,
    projets,
    volumes,
)

urlpatterns = [
    path("", home, name="home"),
    path('projets/', projets, name='projets'),
    path('projets/add/', projet_add, name='projet_add'),  # Assurez-vous que cette ligne est présente
    # path('projets/edit/<int:pk>/', projet_edit, name='projet_edit'),
    # path('projets/delete/<int:pk>/', projet_delete, name='projet_delete'),
    path('bassins/', bassins, name='bassins'),
    path('fournisseurs/', fournisseurs, name='fournisseurs'),
    path('materiaux/', materiaux, name='materiaux'),
    path('volumes/', volumes, name='volumes'),
    path("signup/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
]