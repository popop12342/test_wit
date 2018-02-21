# -*- coding: utf-8 -*-
from reconhece import reconhece
from entidades.busca_entidades import busca_entidades, checa_anterior
import validacoes

def obter_numero_conta(io, resposta, cliente, modo):
	# Checa se o número da conta foi inicialmente fornecido
	resposta = numero_falado(resposta, cliente, modo)
	principal = u'numero_conta'
	entidades = [principal, u'conta_anterior', u'number', u'conta']
	numero_conta = busca_entidades(principal = principal, entidades = entidades, nova = resposta, antiga = resposta)

	# Checa conta anterior
	numero_conta = checa_anterior(numero_conta, "mesma conta", resposta, principal)

	# Se o numero não foi inicialment fornecido
	while (numero_conta == "nao encontrado"):
		io.imprime("Diga o numero da conta")
		resposta_numero_conta = reconhece(io, cliente, modo)
		resposta_numero_conta = numero_falado(resposta_numero_conta, cliente, modo)
		validacoes.cancelar_check(resposta_numero_conta)
		numero_conta = busca_entidades(principal = principal, entidades = entidades, nova = resposta_numero_conta, antiga = resposta)
		numero_conta = checa_anterior(numero_conta, "mesma conta", resposta, principal)

	return numero_conta

# Caso o usuário diga o número dígito a dígito
# Ex: "conta um dois três quatro"
def numero_falado(resposta, cliente, modo):
	if (modo == "2"):
		resposta = validacoes.formata_numero(resposta)
		resposta = cliente.message(resposta['_text'])
	return resposta