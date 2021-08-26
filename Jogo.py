"""
crie um jogo de perguntas, usando HTTP request to the open trivia api
a cada rodada o jogo deve pegar uma nova pergunta e apresentar para o 
usuario responder. ao fim de cada round pergunte ao usuario se ele quer
jogar novamente. continue jogando ate o usario digitar 'quit'.
"""
import pip._vendor.requests as requests
import json
import random
import html

print("seja bem vindo ao jogo de perguntas e respostas: ")
pontos = 0
total = 0
validação = ""
while validação != "quit": 
    input("Quando quiser começar aperte enter.")
    print("")
    total +=1

    r = requests.get("https://opentdb.com/api.php?amount=1&category=11&difficulty=easy&type=multiple") #pega as informações do site
    pergunta = json.loads(r.text) #transforma as informações do site de um dicionario python para json
    if(r.status_code != 200):
        validação = input("sinto muito ocorreu um problema a pegar as perguntas. aperte enter para tentar novamente ou digite 'quit' para sair")
    else:
        questao = pergunta["results"][0]["question"]
        print(html.unescape(questao) +"\n") #extrai a pergunta
        Resposta = pergunta["results"][0]["correct_answer"] #armazena a resposta e as alternativas
        Alternativas = pergunta["results"][0]["incorrect_answers"]
        Alternativas.insert(random.randint(0,3), Resposta) #embaralha

        for answer in Alternativas:
            print(html.unescape(answer)) #Ajeita alguns problemas de tradução
        chute = input("\ninsira a sua resposta: \n")

        if(chute.lower() == Resposta.lower()):
            pontos += 1
            print("\nAcertou\n")
        else:
            print("\nErrou\n")
            print("a resposta era: "+Resposta)
        print("Deseja jogar novamente ?")
        print("digite quit para sair" )
        validação = input("")

print("seu Score foi: " + str(pontos) + "/" + str(total))