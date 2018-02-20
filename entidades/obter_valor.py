# -*- coding: utf-8 -*-
from reconhece import reconhece
from entidades.busca_entidades import busca_entidades, checa_anterior
import validacoes

def obter_valor(resposta, cliente, modo):

	#checa se o valor foi inicialmente forncido
	principal = u'amount_of_money'
	entidades = [principal, u'valor', u'valor_anterior']
	valor = busca_entidades(principal = principal, entidades = entidades, nova = resposta, antiga = resposta)

	# busca o último valor transferido
	valor = checa_anterior(valor, "mesmo valor", resposta, principal)

	# Se o valor não foi inicialmente fornecido
	while (valor == "nao encontrado"):
		print("Diga o valor")
		resposta_valor = reconhece(cliente, modo)
		validacoes.cancelar_check(resposta_valor)
		# Aqui diferente do número da conta, um número só é aceita como valor após ser impresso "Diga o valor"
		entidades.append(u'number')
		valor = busca_entidades(principal = principal, entidades = entidades, nova = resposta_valor, antiga = resposta)
		valor = checa_anterior(valor, "mesmo valor", resposta, principal)
	return valor