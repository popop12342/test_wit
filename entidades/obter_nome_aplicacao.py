# -*- coding: utf-8 -*-
from reconhece import reconhece
from entidades.busca_entidades import busca_entidades, checa_anterior
import validacoes

def obter_nome_aplicacao(io, msg_analizada, cliente, modo, cm):
	# Checa se o nome da aplicação foi inicialmente fornecido
	principal = u'nome_aplicacao'
	entidades = [principal, u'aplicacao_anterior']
	nome_aplicacao = busca_entidades(principal = principal, entidades = entidades, nova = msg_analizada, antiga = msg_analizada)

	# Checa última aplicação
	nome_aplicacao = checa_anterior(valor=nome_aplicacao,  valor_padrao="mesma aplicação", entidade=principal, cm=cm, contexto="aplicacao")

	# Se o nome não foi inicialmente fornecido
	while (nome_aplicacao == "nao encontrado"):
		io.imprime("Diga o nome da aplicação")
		msg_analizada_nome_aplicacao = reconhece(io, cliente, modo)
		validacoes.cancelar_check(msg_analizada_nome_aplicacao)
		nome_aplicacao = busca_entidades(principal = principal, entidades = entidades, nova = msg_analizada_nome_aplicacao, antiga = msg_analizada)
		nome_aplicacao = checa_anterior(valor=nome_aplicacao,  valor_padrao="mesma aplicação", entidade=principal, cm=cm, contexto="aplicacao")

	return nome_aplicacao