# -*- coding: utf-8 -*-
import validacoes
from reconhece import reconhece
from entidades.obter_valor import obter_valor
from entidades.obter_numero_conta import obter_numero_conta
from conversas import salva


def transferir(io, resposta, cliente, modo):
	numero_conta = obter_numero_conta(io=io, resposta=resposta, cliente=cliente, modo=modo)
	valor = obter_valor(io=io, resposta=resposta, cliente=cliente, modo=modo)
	
	io.imprime("Transferindo {} R$ para a conta {}".format(valor, numero_conta))
	salva(resposta)
