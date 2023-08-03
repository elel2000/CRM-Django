from django.shortcuts import render, redirect
from .forms import CommandeForm
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
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