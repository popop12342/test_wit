# -*- coding:utf-8 -*-
import conversas

# Busca pelas entidades em resposta
# se encontrar copia essa entidade na entidade principal
def busca_entidades(principal, antiga, nova, entidades=[]):
	for entidade in entidades:
		if (entidade in nova[u'entities']):
			if (nova != antiga):
				antiga[u'_text'].append(nova[u'_text'])

			antiga[u'entities'][principal] = nova[u'entities'].pop(entidade)
			return antiga[u'entities'][principal][0][u'value']

	return "nao encontrado"


# Checa se o usuário quer utilizar um valor anterior
def checa_anterior(valor, valor_padrao, resposta, principal):
	if (valor == valor_padrao):
		entidade = conversas.busca(principal)
		resposta[u'entities'][principal] = entidade
		return entidade[0][u'value']
	return valor