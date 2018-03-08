# -*- coding: utf-8 -*-
from conversas import carrega
from intencoes.pagar import Pagar
from intencoes.transferir import Transferir
from intencoes.intencao import Intencao
from intencoes.aplicar import Aplicar
from intencoes.criar_aplicacao import Criar_aplicacao

def repetir(io, msg_analizada, cliente, modo):
	conversas = carrega()

	ultima = conversas.pop()
	intencao = ultima[u'entities'][u'intent'][0][u'value']

	if (intencao == "get_saldo"):
		Intencao("get_saldo", io, msg_analizada).executa()
	elif (intencao == "pagar"):
		Pagar(io, ultima).executa()
	elif (intencao == "get_limite"):
		Intencao("get_limite", io, msg_analizada).executa()
	elif (intencao == "transferir"):
		Transferir(io, ultima, cliente, modo).executa()
	elif (intencao == "extrato"):
		Intencao("get_extrato", io, msg_analizada).executa()
	elif (intencao == "criar_aplicacao"):
		Criar_aplicacao(io, ultima, cliente, modo).executa()
	elif (intencao == "aplicar"):
		Aplicar(io, ultima, cliente, modo).executa()