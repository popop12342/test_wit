# -*- coding: utf-8 -*-
from entidades.obter_nome_aplicacao import obter_nome_aplicacao
from entidades.obter_valor import obter_valor
from conversas import salva

def criar(io, resposta, cliente, modo):
	nome = obter_nome_aplicacao(io=io, resposta=resposta, cliente=cliente, modo=modo)
	io.imprime("Criando aplicação {}".format(nome))
	salva(resposta)

def aplicar(io, resposta, cliente, modo):
	nome = obter_nome_aplicacao(io=io, resposta=resposta, cliente=cliente, modo=modo)
	valor = obter_valor(io, resposta, cliente, modo)
	io.imprime("Aplicando {} R$ em {}".format(valor, nome))
	salva(resposta)
