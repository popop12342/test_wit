# -*- coding: utf-8 -*-
import random
from respostas import get_respostas
from entidades.obter_nome_aplicacao import obter_nome_aplicacao
from entidades.obter_valor import obter_valor
from conversas import salva

def criar(io, msg_analizada, cliente, modo):
	nome = obter_nome_aplicacao(io=io, msg_analizada=msg_analizada, cliente=cliente, modo=modo)
	respostas = get_respostas("criar_aplicacao")
	index = random.randrange(0, len(respostas))
	resposta = respostas[index]
	resposta = resposta.replace("@nome_aplicacao", nome)
	io.imprime(resposta)
	salva(msg_analizada)

def aplicar(io, msg_analizada, cliente, modo):
	nome = obter_nome_aplicacao(io=io, msg_analizada=msg_analizada, cliente=cliente, modo=modo)
	valor = obter_valor(io, msg_analizada, cliente, modo)
	respostas = get_respostas("aplicar")
	index = random.randrange(0, len(respostas))
	resposta = respostas[index]
	resposta = resposta.replace("@nome_aplicacao", nome).replace("@valor", str(valor))
	io.imprime(resposta)
	salva(msg_analizada)
