# -*- coding: utf-8 -*-
from reconhece import reconhece
from entidades.busca_entidades import busca_entidades, checa_anterior
import validacoes

def obter_valor(io, msg_analizada, cliente, modo):

	#checa se o valor foi inicialmente forncido
	principal = u'amount_of_money'
	entidades = [principal, u'valor', u'valor_anterior']
	valor = busca_entidades(principal = principal, entidades = entidades, nova = msg_analizada, antiga = msg_analizada)

	# busca o último valor transferido
	valor = checa_anterior(valor, "mesmo valor", msg_analizada, principal)

	# Se o valor não foi inicialmente fornecido
	while (valor == "nao encontrado"):
		io.imprime("Diga o valor")
		msg_analizada_valor = reconhece(io, cliente, modo)
		validacoes.cancelar_check(msg_analizada_valor)
		# Aqui diferente do número da conta, um número só é aceita como valor após ser impresso "Diga o valor"
		entidades.append(u'number')
		valor = busca_entidades(principal = principal, entidades = entidades, nova = msg_analizada_valor, antiga = msg_analizada)
		valor = checa_anterior(valor, "mesmo valor", msg_analizada, principal)
	return valor