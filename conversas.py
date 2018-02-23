# -*- coding: utf-8 -*-
import codecs
from estrutura_dados.pilha import Pilha

def salva(resposta):
	f = codecs.open("conversas.txt", 'a', encoding="utf-8")
	f.write(str(resposta))
	f.write("\n")
	f.close()

def carrega():
	conversas = Pilha()
	with codecs.open("conversas.txt",encoding="utf-8") as f:
		for linha in f:
			conversa = eval(linha)
			conversas.push(conversa)

	return conversas

# Busca e retorna a entidade mais recente
def busca(entidade):
	conversas = carrega()

	while (not conversas.is_empty()):
		ultima = conversas.pop()
		if (entidade in ultima[u'entities']):
			return ultima[u'entities'][entidade]
