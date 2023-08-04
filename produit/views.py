from django.shortcuts import render, HttpResponse
from commande.models import Commande
from client.models import Client

# Create your views here.
def home(request):
    commandes = Commande.objects.all()
    clients = Client.objects.all() # type: ignore
    context = {'commande' : commandes,'client' : clients}

    return render(request,'produit/acceuil.html',context)