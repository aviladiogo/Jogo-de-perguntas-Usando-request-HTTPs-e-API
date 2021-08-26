"""
mandando requisições HTTP para API e uso de JSON
"""
import pip._vendor.requests as requests
import json
import pprint

r = requests.get("https://opentdb.com/api.php?amount=1&category=11&difficulty=easy&type=multiple") #pega as informações do site

pergunta = json.loads(r.text) #transforma as informações do site de um dicionario python para json
print(pprint.pprint(pergunta)) #use este comando para printar o http em JSON e pegar os dados desejados 
print(pergunta["results"][0]["category"])

#como se converte um dicionario python para dicionario json:
pessoa ={"Name": 'John', 'Age': 30}
pessoa_json = json.dumps(pessoa)
