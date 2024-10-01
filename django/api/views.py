from django.shortcuts import render
from django.http import HttpResponse
from . import views
# Create your views here.
def home(request):
    return HttpResponse("<h1>Minha View</h1>")

def sobre(request):
    return HttpResponse("<h1>Sobre nos</h1>")

def contato(request):
    return HttpResponse("<h1>Meus contatos</h1>")

def main(request):
    return HttpResponse("<h1>Raiz</h1>")