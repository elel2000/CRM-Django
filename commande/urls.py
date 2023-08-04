
from django.urls import path
from . import views

urlpatterns = [

    path('',views.list_commande),
    path('ajouter_commandes',views.ajouter_commandes,name="ajouter_commandes"),
    path('modifier_commande/<str:pk>/',views.modifier_commande,name="modifier_commande"),
    path('supprimer_commande/<str:pk>/',views.supprimer_commande,name="supprimer_commande"),
]
