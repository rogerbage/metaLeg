from unidecode import unidecode
import logging
from .models import Decreto, LeiOrdinaria
from django.http import JsonResponse
from sentence_transformers import SentenceTransformer, util
from langchain.text_splitter import RecursiveCharacterTextSplitter

import os, json, re
from PyPDF2 import PdfReader

from django.template import loader


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
    searchClean = unidecode(search).lower()
    logging.warning(searchClean)
    if (tipo == 'ordinaria'):
        filterDecretos = LeiOrdinaria.objects.filter(inteiroTeor__icontains=searchClean).order_by('ano', 'lei')
    else:
        logging.warning("DECRETO")
        #filterDecretos = Decreto.objects.filter(Q(inteiroTeor__icontains=search) | Q(inteiroTeor__icontains=searchClean)).order_by('ano', 'lei')
        filterDecretos = Decreto.objects.filter(inteiroTeor__icontains=searchClean).order_by('ano', 'lei')
    
    contador = {}
    laws = {}
    for d in filterDecretos:
        logging.warning('aqui')
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

##################################################################
def loadTemplate(templateUrl, context ):
    try:
        html_template = loader.render_to_string(templateUrl, context)
        return(html_template)
    except Exception as inst:
        print(type(inst))    
        print(inst.args)     
        print(inst)
        return(inst)
###################################################################

def returnFullText(file):
    reader = PdfReader("./apps/data/user_uploads/" + file)
    fullText = ""
    for page in reader.pages:
        fullText = fullText + page.extract_text() 
    return(fullText)

def embbedingDecreto(decreto):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    if not os.path.exists('./apps/data/transformers/decretos/decreto_' + str(decreto.id) + '.json'):
        corpus = simple_text_splitter(decreto.inteiroTeor)
        # corpus = [decreto.inteiroTeor]
        # corpus =  list(set(re.findall('[^!?。.？！]+[!?。.？！]?', decreto.inteiroTeor)))

        print(corpus)
        sentence_embeddings = model.encode(corpus, convert_to_numpy=True)
        with open('./apps/data/transformers/decretos/decreto_' + str(decreto.id) + '.json', 'w') as destination:
            sentence_json = json.dumps(sentence_embeddings.tolist())
            destination.write(sentence_json)

def simple_text_splitter(input):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 200,
            chunk_overlap  = 54,
            length_function = len,
        )
        metadatas = [{"document": 'pagina_web'}]
        texts = text_splitter.create_documents([input], metadatas=metadatas )
        resultado = []
        for t in texts:
            resultado.append(t.page_content)
        return(resultado)

def noOpenaiEmbbeding(input, file): 
    model = SentenceTransformer('all-MiniLM-L6-v2')
    # model = SentenceTransformer('all-roberta-large-v1')
    #model = SentenceTransformer('juridics/bertlaw-base-portuguese-sts-scale')
    #model = SentenceTransformer('neuralmind/bert-base-portuguese-cased')
                

    if not os.path.exists('./apps/data/transformers/' + file + '.json'):
        fullText = returnFullText(file)
        #corpus = splendaRoot.simple_text_splitter(fullText)
        corpus = fullText.split('\n')
        print(corpus)
        sentence_embeddings = model.encode(corpus, convert_to_numpy=True)
        with open('./apps/data/transformers/' + file + '.json', 'wb') as destination:
            sentence_json = json.dumps(sentence_embeddings.tolist())
            # destination.write(sentence_json)
            # pickle.dump({'sentence': sentence_embeddings, 'corpus': corpus} , destination)
    else:
        with open('./apps/data/transformers/' + file + '.json', 'rb') as destination:
            # sentenceText = destination.read()
            sentence_embeddings = json.loads(destination.read())
            # sentence_embeddings = cache_embeddings['sentence']
            # corpus = cache_embeddings['corpus']
    
    query = [input]
    query_embedding = model.encode(query, convert_to_tensor=True)
    hits = util.semantic_search(query_embedding, sentence_embeddings, top_k=10)
    hits = hits[0]      #Get the hits for the first query
    print(hits)

    resultado = []
    strResultado = ""
    for hit in hits:
        resultado.append(corpus[hit['corpus_id']])
        strResultado = strResultado + '\n' + corpus[hit['corpus_id']]
        print(corpus[hit['corpus_id']], "(Score: {:.4f})".format(hit['score']))
    # return(str(list(sentence_embeddings)))
    newQuery = (
        f"Responda a consulta utilizando o texto abaixo como contexto.\n\n"
        f"Consulta: ///// {input} /////\n\n"
        f"Texto: \n ///// \n {strResultado} \n /////\n"
    )
    # resposta = splendaRoot.basicOpenai(newQuery)
    resposta = corpus[hits[0]['corpus_id']]
    return(resposta)