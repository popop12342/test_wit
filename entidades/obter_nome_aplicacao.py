# -*- coding: utf-8 -*-
from reconhece import reconhece
import validacoes
import conversas

def obter_nome_aplicacao(resposta, cliente, modo):
	# Checa se o nome da aplicação foi inicialmente fornecido
	if (u'nome_aplicacao' in resposta[u'entities']):
		nome_aplicacao = resposta[u'entities'][u'nome_aplicacao'][0][u'value']
		return nome_aplicacao

	# Busca a última aplicação
	if (u'aplicacao_anterior' in resposta[u'entities']):
		resposta[u'entities'][u'nome_aplicacao'] = conversas.busca(u'nome_aplicacao')
		return obter_nome_aplicacao(resposta, cliente, modo)

	# Se o valor não foi inicialmente fornecido
	print("Diga o nome da aplicação")
	resposta_nome_aplicacao = reconhece(cliente, modo)
	validacoes.cancelar_check(resposta_nome_aplicacao)
	if (u'nome_aplicacao' in resposta_nome_aplicacao[u'entities']):
		resposta[u'entities'][u'nome_aplicacao'] = resposta_nome_aplicacao[u'entities'][u'nome_aplicacao']
	elif (u'aplicacao_anterior' in resposta_nome_aplicacao[u'entities']):
		resposta[u'entities'][u'nome_aplicacao'] = conversas.busca(u'nome_aplicacao')

	return obter_nome_aplicacao(resposta, cliente, modo)