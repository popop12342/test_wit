# -*- coding: utf-8 -*-
from recorder import record_audio, read_audio

# seleciona o tipo de reconhecimento, voz ou texto
def reconhece(io, cliente, modo):
	msg_analizada = {}
	if (modo == "1"):
		msg_analizada = reconhece_texto(io, cliente)
	else:
		msg_analizada = reconhece_voz(io, cliente)

	return msg_analizada


def reconhece_texto(io, cliente):
	menssagem = io.le()
	msg_analizada = cliente.message(menssagem)

	return msg_analizada


def reconhece_voz(io, cliente):
	#segundos = 4
	# escolhe o arquivo de audio apenas para teste
	nome_arquivo = io.le("Nome do arquivo: ")

	# grava audio
	#record_audio(segundos, nome_arquivo)

	# lê audio
	audio = read_audio(nome_arquivo)

	# definindo header
	header = {'Content-Type': 'audio/wav'}

	msg_analizada = cliente.speech(audio, None, header)

	return msg_analizada


def get_intencao(msg_analizada):
	if (not u'intent' in msg_analizada[u'entities']):
		return "nenhuma"
	return msg_analizada[u'entities'][u'intent'][0][u'value']
