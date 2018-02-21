# -*- coding: utf-8 -*-
from estrutura_dados.pilha import Pilha

def salva(resposta):
	f = open("conversas.txt", 'a')
	f.write(str(resposta))
	f.write("\n")
	f.close()

def carrega():
	conversas = Pilha()
	with open("conversas.txt") as f:
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
