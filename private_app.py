# -*- coding: utf-8 -*-

from wit import Wit
from reconhece import reconhece, get_intencao
import Cancelar
from intencoes.aplicacao import aplicar, criar
from intencoes.get_extrato import get_extrato
from intencoes.get_limite import get_limite
from intencoes.get_saldo import get_saldo
from intencoes.pagar import pagar
from intencoes.transferir import transferir
from intencoes.repetir import repetir

def iniciar():
	cliente = Wit("EGYXBUP5MBO2C3FH67L6IP2JNZ3DLRCW")

	print("Escolha a forma de interação:")
	print("1) texto")
	print("2) audio")
	modo = input()

	while (True):
		try:
			print("\nO que você gostaria de fazer hoje?")
			resposta = reconhece(cliente, modo)
			intencao = get_intencao(resposta)
			
			
			if (intencao == "get_saldo"):
				get_saldo(resposta)
			elif (intencao == "pagar"):
				pagar(resposta)
			elif (intencao == "get_limite"):
				get_limite(resposta)
			elif (intencao == "transferir"):
				transferir(resposta, cliente, modo)
			elif (intencao == "extrato"):
				get_extrato(resposta)
			elif (intencao == "cancelar"):
				break;
			elif (intencao == "criar_aplicacao"):
				criar(resposta, cliente, modo)
			elif (intencao == "aplicar"):
				aplicar(resposta, cliente, modo)
			elif (intencao == "repetir"):
				repetir(resposta, cliente, modo)
			else:
				print("Não compreendi sua intenção")

		except Cancelar.Cancelar:
			continue


if (__name__ == "__main__"):
	iniciar()