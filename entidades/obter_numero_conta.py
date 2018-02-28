# -*- coding: utf-8 -*-
from reconhece import reconhece
from entidades.busca_entidades import busca_entidades, checa_anterior
import validacoes

def obter_numero_conta(io, msg_analizada, cliente, modo):
	# Checa se o número da conta foi inicialmente fornecido
	msg_analizada = numero_falado(msg_analizada, cliente, modo)
	principal = u'numero_conta'
	entidades = [principal, u'conta_anterior', u'number', u'conta']
	numero_conta = busca_entidades(principal = principal, entidades = entidades, nova = msg_analizada, antiga = msg_analizada)

	# Checa conta anterior
	numero_conta = checa_anterior(numero_conta, "mesma conta", msg_analizada, principal)

	# Se o numero não foi inicialment fornecido
	while (numero_conta == "nao encontrado"):
		io.imprime("Diga o número da conta")
		msg_analizada_numero_conta = reconhece(io, cliente, modo)
		msg_analizada_numero_conta = numero_falado(msg_analizada_numero_conta, cliente, modo)
		validacoes.cancelar_check(msg_analizada_numero_conta)
		numero_conta = busca_entidades(principal = principal, entidades = entidades, nova = msg_analizada_numero_conta, antiga = msg_analizada)
		numero_conta = checa_anterior(numero_conta, "mesma conta", msg_analizada, principal)

	return numero_conta

# Caso o usuário diga o número dígito a dígito
# Ex: "conta um dois três quatro"
def numero_falado(msg_analizada, cliente, modo):
	if (modo == "2" and u'number' in msg_analizada[u'entities']):
		msg_analizada = validacoes.formata_numero(msg_analizada)
		msg_analizada = cliente.message(msg_analizada['_text'])
	return msg_analizada