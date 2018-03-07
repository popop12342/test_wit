# -*- coding: utf-8 -*-
import wit
from wit import Wit
from reconhece import reconhece, get_intencao
import Cancelar
from my_io.IOManager import IOManager
from intencoes.aplicacao import aplicar, criar
from intencoes.get_extrato import get_extrato
from intencoes.get_limite import get_limite
from intencoes.get_saldo import get_saldo
from intencoes.pagar import pagar
from intencoes.transferir import transferir
from intencoes.repetir import repetir
from intencoes.greetings import greetings_hello

def iniciar(io):
	cliente = Wit("EGYXBUP5MBO2C3FH67L6IP2JNZ3DLRCW")

	io.imprime("Escolha a forma de interação:")
	io.imprime("1) texto")
	io.imprime("2) audio")
	modo = io.le()
	
	while (True):
		try:
			io.imprime("\nO que você gostaria de fazer hoje?")
			msg_analizada = reconhece(io, cliente, modo)
			intencao = get_intencao(msg_analizada)

			msg_analizada[u'_text'] = [msg_analizada[u'_text']]
			
			if (intencao == "get_saldo"):
				get_saldo(io, msg_analizada)
			elif (intencao == "pagar"):
				pagar(io, msg_analizada)
			elif (intencao == "get_limite"):
				get_limite(io, msg_analizada)
			elif (intencao == "transferir"):
				transferir(io, msg_analizada, cliente, modo)
			elif (intencao == "extrato"):
				get_extrato(io, msg_analizada)
			elif (intencao == "cancelar"):
				break
			elif (intencao == "criar_aplicacao"):
				criar(io, msg_analizada, cliente, modo)
			elif (intencao == "aplicar"):
				aplicar(io, msg_analizada, cliente, modo)
			elif (intencao == "repetir"):
				repetir(io=io, msg_analizada=msg_analizada, cliente=cliente, modo=modo)
			elif (intencao == "greetings_hello"):
				greetings_hello(io, msg_analizada)
			else:
				io.imprime("Não compreendi sua intenção")

		except Cancelar.Cancelar:
			continue

		except wit.wit.WitError:
			io.imprime("Não compreendi o que você disse")


if (__name__ == "__main__"):
	iniciar(IOManager())