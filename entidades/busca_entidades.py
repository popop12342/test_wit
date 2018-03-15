# -*- coding:utf-8 -*-
import conversas

# Busca pelas entidades em msg_analizada
# se encontrar copia essa entidade na entidade principal
def busca_entidades(principal, antiga, nova, entidades=[]):
	for entidade in entidades:
		if (entidade in nova[u'entities']):
			if (nova != antiga):
				antiga[u'_text'].append(nova[u'_text'])

			antiga[u'entities'][principal] = nova[u'entities'].pop(entidade)
			return antiga[u'entities'][principal][0][u'value']

	return "nao encontrado"


def checa_anterior(valor, valor_padrao, entidade, cm, contexto):
	if (valor == valor_padrao):
		if (isinstance(contexto, list)):
			for c in contexto:
				v = cm.busca(c, entidade)
				if (v != "nao encontrado"):
					return v
		else:
			return cm.busca(contexto, entidade)
	return valor
# Checa se o usuário quer utilizar um valor anterior
# def checa_anterior(valor, valor_padrao, msg_analizada, principal):
	# if (valor == valor_padrao):
	# 	entidade = conversas.busca(principal) 
	# 	msg_analizada[u'entities'][principal] = entidade
	# 	return entidade[0][u'value']
	# return valor