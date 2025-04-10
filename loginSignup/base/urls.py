from django.urls import path, include
from .views import authView, bassins, fournisseurs, home, materiaux, projets, volumes

urlpatterns = [
 path("", home, name="home"),
 path('projets/', projets, name='projets'),
    path('bassins/', bassins, name='bassins'),
    path('fournisseurs/', fournisseurs, name='fournisseurs'),
    path('materiaux/', materiaux, name='materiaux'),
    path('volumes/', volumes, name='volumes'),
 path("signup/", authView, name="authView"),
 path("accounts/", include("django.contrib.auth.urls")),
]
