from django.shortcuts import render
from .models import Proyecto 

def index(request):

    proyectos_del_portafolio = Proyecto.objects.all()
    context = {
        'proyectos': proyectos_del_portafolio,
    }
    return render(request, 'portafolio_app/index.html', context)