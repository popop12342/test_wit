# -*- coding: utf-8 -*-
from recorder import record_audio, read_audio

def reconhece(io, cliente, modo):
	resposta = {}
	if (modo == "1"):
		resposta = reconhece_texto(io, cliente)
	else:
		resposta = reconhece_voz(io, cliente)

	return resposta


def reconhece_texto(io, cliente):
	menssagem = io.le()
	resposta = cliente.message(menssagem)

	return resposta


def reconhece_voz(io, cliente):
	segundos = 4
	# escolhe o arquivo de audio apenas para teste
	nome_arquivo = io.le("Nome do arquivo: ")

	# grava audio
	#record_audio(segundos, nome_arquivo)

	# lê audio
	audio = read_audio(nome_arquivo)

	# definindo header
	header = {'Content-Type': 'audio/wav'}

	resposta = cliente.speech(audio, None, header)

	return resposta


def get_intencao(resposta):
	if (not u'intent' in resposta[u'entities']):
		return "nenhuma"
	return resposta[u'entities'][u'intent'][0][u'value']
