# -*- coding: utf-8 -*-
from reconhece import reconhece
import validacoes
import conversas

def obter_valor(resposta, cliente, modo):

	#checa se o valor foi inicialmente forncido
	if (u'amount_of_money'in resposta[u'entities']):
		return resposta[u'entities'][u'amount_of_money'][0][u'value']
	
	if (u'valor' in resposta[u'entities']):
		resposta[u'entities'][u'amount_of_money'] = resposta[u'entities'][u'valor']
		return obter_valor(resposta, cliente, modo)

	# busca o último valor transferido
	if (u'valor_anterior' in resposta[u'entities']):
		resposta[u'entities'][u'amount_of_money'] = conversas.busca(u'amount_of_money')
		return obter_valor(resposta, cliente, modo)

	# Se o valor não foi inicialmente fornecido
	print("Diga o valor")
	resposta_valor = reconhece(cliente, modo)
	validacoes.cancelar_check(resposta_valor)
	if (u'amount_of_money'in resposta_valor[u'entities']):
		resposta[u'entities'][u'amount_of_money'] = resposta_valor[u'entities'][u'amount_of_money']
	if (u'number' in resposta_valor[u'entities']):
		resposta[u'entities'][u'amount_of_money'] = resposta_valor[u'entities'][u'number']
	if (u'valor_anterior' in resposta_valor[u'entities']):
		resposta[u'entities'][u'amount_of_money'] = conversas.busca(u'amount_of_money')
	return obter_valor(resposta, cliente, modo)
	# Aqui diferente do número da conta, um número só é aceita como valor após ser impresso "Diga o valor"
