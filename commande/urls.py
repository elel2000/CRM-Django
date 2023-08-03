
from django.urls import path
from . import views

urlpatterns = [

    path('',views.list_commande),
    path('ajouter_commandes',views.ajouter_commandes,name="ajouter_commandes")
]
