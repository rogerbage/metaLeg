import json
import os
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer, util
import torch
from langchain.text_splitter import RecursiveCharacterTextSplitter
from unidecode import unidecode
from apps.home.models import Decreto, LeiOrdinaria
import logging
from django.http import JsonResponse







class MetaLeg:
    def __init__(self):
        self.initMetaLeg = True
	
    def getExtruturedAndIndexFile(self, file, model):
        
        sentenceAndCorpus = {}
        
        if not os.path.exists('./apps/data/transformers/indexados/' + file + '.json'):

            fullText = self.returnFullText(file)
            # sentenceAndCorpus['corpus'] = splendaRoot.simple_text_splitter(fullText)
            sentenceAndCorpus['corpus'] = fullText.split('\n')
            sentenceAndCorpus['sentence'] = model.encode(
                sentenceAndCorpus['corpus'], convert_to_numpy=True).tolist()

            with open('./apps/data/transformers/indexados/' + file + '.json', 'w') as destination:
                sc_json = json.dumps(sentenceAndCorpus)
                destination.write(sc_json)
        else:
            with open('./apps/data/transformers/indexados/' + file + '.json', 'r') as destination:
                sentenceAndCorpus = json.loads(destination.read())
                sentenceAndCorpus['sentence'] = sentenceAndCorpus['sentence']

        return sentenceAndCorpus

    def returnFullText(self, file):
        reader = PdfReader("./apps/data/user_uploads/" + file)
        fullText = ""
        for page in reader.pages:
            fullText = fullText + page.extract_text()
        return(fullText)

    def noOpenaiEmbbeding(self, query, leg): 
        model = SentenceTransformer('all-MiniLM-L6-v2') #O melhor para busca por linha
        # model = SentenceTransformer('alfaneo/jurisbert-base-portuguese-sts')
        # model = SentenceTransformer('alfaneo/jurisbert-base-portuguese-uncased')
        # model = SentenceTransformer('neuralmind/bert-base-portuguese-cased')
        # model = SentenceTransformer('sentence-transformers/all-MiniLM-L12-v2')
        
        
        sentenceAndCorpus = MetaLeg.getExtruturedAndIndexFile(leg, model)
        sentence_embeddings = torch.FloatTensor(sentenceAndCorpus['sentence'])
        corpus = sentenceAndCorpus['corpus']
        print(corpus)
        return(corpus)
        # queue = Queue()
        # threads = []
        # resultado = []
        # i = 0
        # for l in listOriginal:
        #     i += 2
        #     # strJson = '{ "' + l['campo'] + '": "?" }'
        #     dicionario = [{
        #             'chave': {
        #                 'nome': l['campo'],
        #                 'exemplo': l['exemplos'][0],
        #                 'resposta': '?',
        #                 'certeza': '?',
        #                 'observacoes': '?',
        #             }
        #     }]
        #     strJson = json.dumps(dicionario)
        #     # resultado.append(splendaRoot.getByExampleProximity(l, sentence_embeddings, corpus, model))
        #     strResultado = splendaRoot.getByExampleProximity(l, sentence_embeddings, corpus, model)
            
        #     if (len(strResultado) > 0):
        #         thread = threading.Thread(
        #             target=splendaRoot.foundField,
        #             args=[strJson, strResultado, queue, i]
        #         )
                
        #         thread.start()
        #         threads.append(thread)
            
        # for thread in threads:
        #     thread.join()
        
        # queue.join()
        
            

        
        # return(json.dumps(resultado))
        # return(json.dumps(globalFinal))

    def embbedingEmentas(self, decretos, ano):
        model = SentenceTransformer('all-MiniLM-L6-v2')
        url = f"./apps/data/transformers/decretos/ementas/ementa_{ano}.json"
        os.makedirs(os.path.dirname(url), exist_ok=True)
        decretosAno = {}
        for decreto in decretos:
            decretosAno[decreto.id] = model.encode(decreto.ementa, convert_to_numpy=True).tolist()
                                
        with open(url, 'w') as destination:
            sentence_json = json.dumps(decretosAno)
            destination.write(sentence_json)

    def embbedingDecreto(self, ementas, ano):
        model = SentenceTransformer('all-MiniLM-L6-v2')
        # url = f"./apps/data/transformers/decretos/{decreto.ano}/ementas/decreto_{decreto.id}.json"
        url = f"./apps/data/transformers/decretos/decreto_{ano}.json"
        os.makedirs(os.path.dirname(url), exist_ok=True)
        if not os.path.exists(url):
            # corpus = self.simple_text_splitter(decreto.inteiroTeor)
            # corpus = [decreto.inteiroTeor]
            # corpus =  list(set(re.findall('[^!?。.？！]+[!?。.？！]?', decreto.inteiroTeor)))

            # print(corpus)
            sentence_embeddings = model.encode(ementas, convert_to_numpy=True)
            
            with open(url, 'w') as destination:
                sentence_json = json.dumps(sentence_embeddings.tolist())
                destination.write(sentence_json)

    def simple_text_splitter(self, input):
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
    
    def returnLegSemantic(tipo, search):
        searchClean = unidecode(search).lower()
        logging.warning(search)
        model = SentenceTransformer('all-MiniLM-L6-v2')
        searchEmbedding = model.encode([search], convert_to_numpy=True)
        indexUrl = './apps/data/transformers/decretos/ementas/'
        allFiles = [f for f in os.listdir(indexUrl) if os.path.isfile(os.path.join(indexUrl, f))]
        melhores = []
        for fileName in allFiles:
            url = indexUrl + fileName
            with open(url, 'r') as fileIndex:
                loadIndexes = json.loads(fileIndex.read())

            indexes = []
            indexesKeys = []
            for loadIndex in loadIndexes:
                
                indexes.append(torch.FloatTensor(loadIndexes[loadIndex]))
                indexesKeys.append(loadIndex)

            todas = util.semantic_search(searchEmbedding, indexes , top_k=10)[0]
            for cada in todas:
                print("score: ", cada['score'])
                if (cada['score'] > 0.7):
                    melhores.append(indexesKeys[cada['corpus_id']])

        print(melhores)

        if (tipo == 'ordinaria'):
            Blog.objects.filter(pk__in=[1, 4, 7])
            filterDecretos = LeiOrdinaria.objects.filter(id__in=melhores).order_by('ano', 'lei')
        else:
            #filterDecretos = Decreto.objects.filter(Q(inteiroTeor__icontains=search) | Q(inteiroTeor__icontains=searchClean)).order_by('ano', 'lei')
            filterDecretos = Decreto.objects.filter(id__in=melhores).order_by('ano', 'lei')
        
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