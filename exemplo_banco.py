# -*- coding: utf-8 -*-
import wit
from wit import Wit
from reconhece import reconhece, get_intencao
import Cancelar
from my_io.IOManager import IOManager
from intencoes.pagar import Pagar
from intencoes.transferir import Transferir
from intencoes.repetir import repetir
from intencoes.intencao import Intencao
from intencoes.aplicar import Aplicar
from intencoes.criar_aplicacao import Criar_aplicacao

def iniciar(io):
	cliente = Wit("EGYXBUP5MBO2C3FH67L6IP2JNZ3DLRCW")

	io.imprime("Escolha a forma de interação:")
	io.imprime("1) texto")
	io.imprime("2) audio")
	modo = io.le()
	
	intencoes = {
		"get_saldo": Intencao, 
		"get_limite": Intencao, 
		"get_extrato": Intencao, 
		"greetings_hello": Intencao,
		"pagar": Pagar,
		"transferir": Transferir,
		"criar_aplicacao": Criar_aplicacao,
		"aplicar": Aplicar,
		"cancelar_cartao": Intencao,
		"desbloquear_cartao": Intencao
	}

	while (True):
		try:
			io.imprime("\nO que você gostaria de fazer hoje?")
			msg_analizada = reconhece(io, cliente, modo)
			intencao = get_intencao(msg_analizada)

			msg_analizada[u'_text'] = [msg_analizada[u'_text']]
			

			if (intencao in intencoes):
				intencoes[intencao](nome=intencao, io=io, msg_analizada=msg_analizada, cliente=cliente, modo=modo).executa()
			elif (intencao == "cancelar"):
				break
			elif (intencao == "repetir"):
				repetir(io=io, msg_analizada=msg_analizada, cliente=cliente, modo=modo)
			else:
				io.imprime("Não compreendi sua intenção")

		except Cancelar.Cancelar:
			continue

		except wit.wit.WitError:
			io.imprime("Não compreendi o que você disse")


if (__name__ == "__main__"):
	iniciar(IOManager())