from unidecode import unidecode
import logging
from .models import Decreto, LeiOrdinaria
from django.http import JsonResponse


def conta_matches(df, search):
    matches = [search]
    cont = 0
    laws = {};
    for f in df.itertuples():
        if any(z in f.inteiro_teor.lower() for z in matches):
            cont += 1
            laws[f.lei] = ([f.ano, f.lei, str(f.ementa)[0:100]])
    return cont, laws

def returnLeg(tipo, search):
    #searchClean = unidecode(search).lower()
    #search = request.GET['search']
    searchClean = unidecode(search).lower()
    logging.warning(search)
    if (tipo == 'ordinaria'):
        filterDecretos = LeiOrdinaria.objects.filter(inteiroTeor__icontains=searchClean).order_by('ano', 'lei')
    else:
        #filterDecretos = Decreto.objects.filter(Q(inteiroTeor__icontains=search) | Q(inteiroTeor__icontains=searchClean)).order_by('ano', 'lei')
        filterDecretos = Decreto.objects.filter(inteiroTeor__icontains=searchClean).order_by('ano', 'lei')
    
    contador = {}
    laws = {}
    for d in filterDecretos:
        if (not d.ano in contador):
            contador[d.ano] = 1
        else:
            contador[d.ano] += 1
        if (not d.lei in laws):
            laws[d.lei] = {}
            laws[d.lei]['id'] = {}
            laws[d.lei]['lei'] = {}
            laws[d.lei]['ano'] = {}
            laws[d.lei]['ementa'] = {}
        laws[d.lei]['id'] = d.id
        laws[d.lei]['ano'] = d.ano
        laws[d.lei]['lei'] = d.lei
        laws[d.lei]['ementa'] = d.ementa

    return JsonResponse({'search': search, 'laws': laws, 'type': tipo, 'contador': contador})