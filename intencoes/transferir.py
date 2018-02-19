# -*- coding: utf-8 -*-
import validacoes
from reconhece import reconhece
from entidades.obter_valor import obter_valor
from entidades.obter_numero_conta import obter_numero_conta
from conversas import salva


def transferir(resposta, cliente, modo):
	numero_conta = obter_numero_conta(resposta, cliente, modo)
	valor = obter_valor(resposta, cliente, modo)
	
	print("Transferindo {} R$ para a conta {}".format(valor, numero_conta))
	salva(resposta)
