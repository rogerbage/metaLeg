# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.http import JsonResponse
import logging
import pandas as pd
import glob
from unidecode import unidecode
from .functions import returnLeg, embbedingDecreto
from .models import Decreto, LeiOrdinaria
from libs.MetaLeg.MetaLeg import MetaLeg
from libs.MetaLeg.chat import chat
import json

@login_required(login_url="/login/")
def api(request):
    search = request.GET['search']
    #searchClean = unidecode(search).lower()
    logging.warning('api')
    if(request.GET['semantic'] == 'true'):
        return MetaLeg.returnLegSemantic(request.GET['type'], request.GET['search'])
    return returnLeg(request.GET['type'], search)
    
@login_required(login_url="/login/")
def getSummary(request):
    id = request.GET['id']
    decreto = Decreto.objects.filter(id=id).first()
    result = {}
    if (decreto.lei):
        logging.warning(decreto.lei)
        result['id'] =  decreto.id
        result['ano'] = decreto.ano
        result['lei'] = decreto.lei
        result['ementa'] = decreto.ementa
        result['inteiroTeor'] = decreto.inteiroTeor

        lei = {
            'ano': decreto.ano,
            'lei': decreto.lei,
            'ementa': decreto.ementa,
            'intiero_teor': decreto.inteiroTeor
        }

        prompt = (
            f"Faça um resumo com até 256 palavras sobre a lei brasileira abaixo: \n"
            f"/////\n"
            f"Lei: \n"
            f"```\n"
            f"{json.dumps(lei)}\n"
            f"```\n"
            f"/////"
        )

        resposta = chat.basicOpenai(prompt)

        result['resumo'] = resposta

    return JsonResponse({'search': id, 'result': result})




@login_required(login_url="/login/")
def getDecreto(request):
    id = request.GET['id']
    decreto = Decreto.objects.filter(id=id).first()
    result = {}
    if (decreto.lei):
        logging.warning(decreto.lei)
        result['id'] =  decreto.id
        result['ano'] = decreto.ano
        result['lei'] = decreto.lei
        result['ementa'] = decreto.ementa
        result['inteiroTeor'] = decreto.inteiroTeor

    return JsonResponse({'search': id, 'result': result})


@login_required(login_url="/login/")
def getLeg(request):
    idLeg = request.GET['id']
    typeLeg = request.GET['type']
    if (typeLeg == 'ordinaria'):
        d = LeiOrdinaria.objects.filter(id=idLeg).first()
    else:
        d = Decreto.objects.filter(id=idLeg).first()
    result = {}
    if (d.lei):
        logging.warning(d.lei)
        result['id'] =  d.id
        result['ano'] = d.ano
        result['lei'] = d.lei
        result['ementa'] = d.ementa
        result['inteiroTeor'] = d.inteiroTeor
    return JsonResponse({'search': idLeg, 'type': typeLeg, 'result': result})

    
@login_required(login_url="/login/")
def cleanDecreto(request):
    for row in Decreto.objects.all():
        logging.warning(row.lei[0:20])
        row.leiClean = unidecode(row.lei).lower()
        row.ementaClean = unidecode(row.ementa).lower()
        row.inteiroTeorClean = unidecode(row.inteiroTeor).lower()
        row.save()
    return JsonResponse({'response': 'ok'})


def indexDecreto(request):
    for row in Decreto.objects.all():
        resposta = "ok"
    return JsonResponse({'response': 'ok'})

def cleanOrdinarias(request):
    for row in LeiOrdinaria.objects.all():
        logging.warning(row.lei[0:20])
        row.leiClean = unidecode(row.lei).lower()
        row.ementaClean = unidecode(row.ementa).lower()
        row.inteiroTeorClean = unidecode(row.inteiroTeor).lower()
        row.save()
    return JsonResponse({'response': 'ok'})

@login_required(login_url="/login/")
def updateDecretos(request):
    path = r'apps/static/assets/csvs/decretos' # use your path
    all_files = glob.glob(path + "/*.csv")
    for filename in all_files:
        df = pd.read_csv(filename, sep=';')
        for f in df.itertuples():
            decreto = Decreto.objects.filter(lei=f.lei).first()
            if (not decreto): 
                decreto = Decreto(lei=f.lei)  
                decreto.ano = f.ano 
                decreto.lei = f.lei 
                decreto.ementa = f.ementa 
                decreto.inteiroTeor = f.inteiro_teor
                decreto.save()
                logging.warning('saving')
                logging.warning(f.ano)
                logging.warning(f.lei)
            else:
                logging.warning('already exist')
                logging.warning(f.lei)
            
    context = {'segment': 'index'}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def updateOrdinarias(request):
    path = r'apps/static/assets/csvs/ordinarias' # use your path
    all_files = glob.glob(path + "/*.csv")
    for filename in all_files:
        df = pd.read_csv(filename, sep=';')
        for f in df.itertuples():
            d = LeiOrdinaria.objects.filter(lei=f.lei).first()
            if (not d): 
                d = LeiOrdinaria(lei=f.lei)   
                d.ano = f.ano 
                d.lei = f.lei 
                d.ementa = f.ementa 
                d.inteiroTeor = f.inteiro_teor
                d.save()
                logging.warning('saving')
                logging.warning(f.ano)
                logging.warning(f.lei)
            else:
                logging.warning('already exist')
                logging.warning(f.lei)
            
    context = {'segment': 'index'}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def embeddingDecretos(request):
    ano = 1862
    while ano <= 2023:
        decretos = Decreto.objects.filter(ano=ano).order_by('id')
        metaLeg = MetaLeg()
       
        metaLeg.embbedingEmentas(decretos, ano)
        ano += 1
    return JsonResponse({'response': 'ok'})

@login_required(login_url="/login/")
def embeddingOrdinarias(request):
    ano = 1862
    while ano <= 2023:
        ordinarias = LeiOrdinaria.objects.filter(ano=ano).order_by('id')
        metaLeg = MetaLeg()
       
        metaLeg.embbedingEmentasOrdinarias(ordinarias, ano)
        ano += 1
    return JsonResponse({'response': 'ok'})


@login_required(login_url="/login/")
def index(request):
    if ('type' in request.GET ):
        tipo = request.GET['type']
        search = request.GET['search']
    else:
        tipo = 'decreto'
        search = 'Gás'
    context = {
            'segment': 'index',
            'tipo': tipo,
            'search': search,
    }
    if ('ordinaria' in tipo):
        html_template = loader.get_template('home/leis-ordinarias.html')
        context['segment'] = 'leis-ordinarias'
    else:
        html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template
    
        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
