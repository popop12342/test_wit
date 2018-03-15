# -*- coding: utf-8 -*-
from conversas import carrega
from intencoes.pagar import Pagar
from intencoes.transferir import Transferir
from intencoes.intencao import Intencao
from intencoes.aplicar import Aplicar
from intencoes.criar_aplicacao import Criar_aplicacao

def repetir(io, msg_analizada, cliente, modo, cm):
	conversas = carrega()

	ultima = conversas.pop()
	intencao = ultima[u'entities'][u'intent'][0][u'value']

	intencoes = {
		"get_saldo": Intencao, 
		"get_limite": Intencao, 
		"get_extrato": Intencao, 
		"greetings_hello": Intencao,
		"pagar": Pagar,
		"transferir": Transferir,
		"criar_aplicacao": Criar_aplicacao,
		"aplicar": Aplicar,
		"cancelar_cartao": Intencao,
		"desbloquear_cartao": Intencao
	}

	if (intencao in intencoes):
		intencoes[intencao](io=io, nome=intencao, msg_analizada=ultima, cliente=cliente, modo=modo, cm=cm).executa()