# -*- coding: utf-8 -*-
import Cancelar

# verifica se o numero da conta é válido
# para ser válido o numero da conta deve ter numeros e '-'
def numero_conta_valido(numero_conta):
	valido = True

	for s in numero_conta:
		if ((not s.isdigit()) and s != '-'):
			valido = False

	return valido


# Joga uma exeção se o usuário cancelar a operação de transferir
def cancelar_check(resposta):
	if (not u'intent' in resposta[u'entities']):
		return
	if (resposta[u'entities'][u'intent'][0][u'value'] == "cancelar"):
		raise Cancelar.Cancelar()

# substitui numeros escritos por dígitos
def formata_numero(resposta):
	numeros = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]

	texto = resposta[u'_text']
	palavras = texto.split()

	
	for i in range(len(palavras)):
		if (palavras[i] in numeros):
			palavras[i] = str(numeros.index(palavras[i]))
	
	palavras_novas = []
	prev = "0"
	for palavra in palavras:
		if (not palavra.isdigit()):
			palavras_novas.append(" ")
		elif (not prev.isdigit()):
			palavras_novas.append(" ")
		palavras_novas.append(palavra)
		prev = palavra

	resposta[u'_text'] = ''.join(palavras_novas)
	return resposta