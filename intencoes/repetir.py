# -*- coding: utf-8 -*-
from conversas import carrega
from intencoes.get_saldo import get_saldo
from intencoes.pagar import pagar
from intencoes.get_limite import get_limite
from intencoes.transferir import transferir
from intencoes.get_extrato import get_extrato
from intencoes.aplicacao import criar, aplicar

def repetir(resposta, cliente, modo):
	conversas = carrega()

	ultima = conversas.pop()
	intencao = ultima[u'entities'][u'intent'][0][u'value']

	if (intencao == "get_saldo"):
		get_saldo(ultima)
	elif (intencao == "pagar"):
		pagar(ultima)
	elif (intencao == "get_limite"):
		get_limite(ultima)
	elif (intencao == "transferir"):
		transferir(ultima, cliente, modo)
	elif (intencao == "extrato"):
		get_extrato(ultima)
	elif (intencao == "criar_aplicacao"):
		criar(ultima, cliente, modo)
	elif (intencao == "aplicar"):
		aplicar(ultima, cliente, modo)