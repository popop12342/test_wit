# -*- coding: utf-8 -*-
import validacoes
import random
from respostas import get_respostas
from reconhece import reconhece
from entidades.obter_valor import obter_valor
from entidades.obter_numero_conta import obter_numero_conta
from conversas import salva


def transferir(io, msg_analizada, cliente, modo):
	numero_conta = obter_numero_conta(io=io, msg_analizada=msg_analizada, cliente=cliente, modo=modo)
	valor = obter_valor(io=io, msg_analizada=msg_analizada, cliente=cliente, modo=modo)
	
	respostas = get_respostas("transferir")
	index = random.randrange(0, len(respostas))
	resposta = respostas[index].replace("@valor", str(valor)).replace("@numero_conta", "{:06d}")
	io.imprime(resposta.format(numero_conta))
	salva(msg_analizada)
