from django.shortcuts import render
from .models import Client
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def list_client(request,pk):
    client = Client.objects.get(id=pk)
    context = {'client':client}
    
    return render(request,'client/list_client.html',context)