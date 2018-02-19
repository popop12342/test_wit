# -*- coding: utf-8 -*-
from reconhece import reconhece
import validacoes
import conversas

def obter_numero_conta(resposta, cliente, modo):
	resposta = detecta_number_conta(resposta, resposta)

	# Checa se o numero da conta foi inicialmente fornecido
	if (u'numero_conta' in resposta[u'entities']):
		numero_conta = resposta[u'entities'][u'numero_conta'][0][u'value']
		if (validacoes.numero_conta_valido(numero_conta)):
			return numero_conta

	# busca o número da última conta transferida
	if (u'conta_anterior' in resposta[u'entities']):
		resposta[u'entities'][u'numero_conta'] = conversas.busca(u'numero_conta')
		return obter_numero_conta(resposta, cliente, modo)

	#Se o numero da conta não foi inicialmente fornecido
	print("Diga o numero da conta")
	resposta_numero_conta = reconhece(cliente, modo)

	# Se o usuário disse o número da conta, transforma o número em texto manda novamente a mensagem como texto
	if (modo == "2"):
		resposta_numero_conta = validacoes.formata_numero(resposta_numero_conta)
		resposta_numero_conta = cliente.message(resposta_numero_conta['_text'])

	validacoes.cancelar_check(resposta_numero_conta)
	if (u'numero_conta' in resposta_numero_conta[u'entities']):
		resposta[u'entities'][u'numero_conta'] = resposta_numero_conta[u'entities'][u'numero_conta']
	resposta = detecta_number_conta(antiga = resposta, nova = resposta_numero_conta)
	return obter_numero_conta(resposta, cliente, modo)
	

def detecta_number_conta(antiga, nova):
	# Se existir um número na mensagem ele será considerado como numero da conta
	if (u'number' in nova[u'entities']):
		antiga[u'entities'][u'numero_conta'] = nova[u'entities'][u'number']
		antiga[u'entities'][u'numero_conta'][0][u'value'] = str(antiga[u'entities'][u'numero_conta'][0][u'value'])
	elif (u'conta' in nova[u'entities']):
		antiga[u'entities'][u'numero_conta'] = nova[u'entities'][u'conta']
		antiga[u'entities'][u'numero_conta'][0][u'value'] = str(antiga[u'entities'][u'numero_conta'][0][u'value'])
	elif (u'conta_anterior' in nova[u'entities']):
		antiga[u'entities'][u'numero_conta'] = conversas.busca(u'numero_conta')
	return antiga
