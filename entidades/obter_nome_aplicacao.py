# -*- coding: utf-8 -*-
from reconhece import reconhece
from entidades.busca_entidades import busca_entidades, checa_anterior
import validacoes

def obter_nome_aplicacao(io, resposta, cliente, modo):
	# Checa se o nome da aplicação foi inicialmente fornecido
	principal = u'nome_aplicacao'
	entidades = [principal, u'aplicacao_anterior']
	nome_aplicacao = busca_entidades(principal = principal, entidades = entidades, nova = resposta, antiga = resposta)

	# Checa última aplicação
	nome_aplicacao = checa_anterior(nome_aplicacao,  "mesma aplicação", resposta, principal)

	# Se o nome não foi inicialmente fornecido
	while (nome_aplicacao == "nao encontrado"):
		io.imprime("Diga o nome da aplicação")
		resposta_nome_aplicacao = reconhece(io, cliente, modo)
		validacoes.cancelar_check(resposta_nome_aplicacao)
		nome_aplicacao = busca_entidades(principal = principal, entidades = entidades, nova = resposta_nome_aplicacao, antiga = resposta)
		nome_aplicacao = checa_anterior(nome_aplicacao,  "mesma aplicação", resposta, principal)

	return nome_aplicacao