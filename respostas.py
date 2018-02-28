import csv
import codecs

def get_respostas(intencao):
    arquivo = codecs.open("respostas.csv", mode='r', encoding='utf-8')
    leitor = csv.reader(arquivo)

    for respostas in leitor:
        if (respostas[0] == intencao):
            respostas.pop(0)
            return respostas 