from django.shortcuts import render, redirect,HttpResponse
from .forms import CommandeForm
from .models import Commande

# Create your views here.
def list_commande(request):
    return render(request, 'commande/list_commande.html')

def ajouter_commandes(request):
    form = CommandeForm()
    if request.method == "POST":
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form' : form}
    return render(request,'commande/ajouter_commandes.html',context)

def modifier_commande(request,pk):
    commande = Commande.objects.get(id=pk)
    form = CommandeForm(instance=commande)

    if request.method == "POST":
        form = CommandeForm(request.POST,instance=commande)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form' : form}
    return render(request,'commande/ajouter_commandes.html',context)

def supprimer_commande(request,pk):
    commande = Commande.objects.get(id=pk)

    if request.method == "POST":    
        return redirect('/')
    context = {'item' : commande}
    return render(request,'commande/supprimer_commande.html',context)