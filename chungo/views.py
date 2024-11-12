from django.shortcuts import render
from core.models import GustoHelado

def helados_view(request):
    return render(request, 'helados.html')



def helados_view(request):
    helados = GustoHelado.objects.filter().all()
    return render(request, 'helados.html',{'gustos' : helados})
