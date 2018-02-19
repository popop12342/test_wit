# -*- coding: utf-8 -*-
from entidades.obter_nome_aplicacao import obter_nome_aplicacao
from entidades.obter_valor import obter_valor
from conversas import salva

def criar(resposta, cliente, modo):
	nome = obter_nome_aplicacao(resposta, cliente, modo)
	print("Criando aplicação {}".format(nome))
	salva(resposta)

def aplicar(resposta, cliente, modo):
	nome = obter_nome_aplicacao(resposta, cliente, modo)
	valor = obter_valor(resposta, cliente, modo)
	print("Aplicando {} R$ em {}".format(valor, nome))
	salva(resposta)
