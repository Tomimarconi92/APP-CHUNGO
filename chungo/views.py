from django.shortcuts import render
from core.models import GustoHelado

def helados_view(request):
    return render(request, 'helados.html')


def helados_view(request):
    cremas = GustoHelado.objects.filter(categoria='CREMAS').all()
    cremas_frutales = GustoHelado.objects.filter(categoria='CREMAS FRUTALES').all()
    chocolate = GustoHelado.objects.filter(categoria='CHOCOLATE').all() 
    dulce_de_leche = GustoHelado.objects.filter(categoria='DULCE DE LECHE').all()
    frutales = GustoHelado.objects.filter(categoria='FRUTALES').all()
    return render(request, 'helados.html',{'cremas' : cremas,
                                           'cremas_frutales' : cremas_frutales,
                                           'chocolate' : chocolate,
                                           'dulce_de_leche' : dulce_de_leche,
                                           'frutales' : frutales
                                           })
