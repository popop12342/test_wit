# -*- coding: utf-8 -*-
import validacoes
import random
from respostas import get_respostas
from reconhece import reconhece
from entidades.obter_valor import obter_valor
from entidades.obter_numero_conta import obter_numero_conta
from conversas import salva
from intencoes.intencao import Intencao
from contextos.contexto import Contexto

class Transferir(Intencao):

	def __init__(self, io, msg_analizada, cliente, modo, cm, nome="transferir"):
		super().__init__(nome, io, msg_analizada, cm)
		self.cliente = cliente
		self.modo = modo

	def executa(self):
		numero_conta = obter_numero_conta(io=self.io, msg_analizada=self.msg_analizada, cliente=self.cliente, modo=self.modo, cm=self.cm)
		valor = obter_valor(io=self.io, msg_analizada=self.msg_analizada, cliente=self.cliente, modo=self.modo, cm=self.cm)
		
		respostas = get_respostas("transferir")
		resposta = random.choice(respostas)
		resposta = resposta.replace("@valor", str(valor)).replace("@numero_conta", "{:06d}")
		self.io.imprime(resposta.format(numero_conta))
		salva(self.msg_analizada)

		contexto = Contexto()
		contexto.transferencia(numero_conta, valor)
		self.cm.adiciona(contexto)