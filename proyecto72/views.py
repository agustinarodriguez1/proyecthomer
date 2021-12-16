from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
from django.view import generic 
from .models import Persona 
def index (request): 
    return HttpResponse("Hola Mundo, Nombre de App")
    class IndexView(generic.ListView): 
    template_name='clase_app/index.html'
    context_object_name = 'persona_list'
    def get_queryset(self) 
    return Perosna.objects.order_by('-id')