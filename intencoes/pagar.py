# -*- coding: utf-8 -*-
import random
from respostas import get_respostas
from conversas import salva
from intencoes.intencao import Intencao

class Pagar(Intencao):

	def __init__(self, io, msg_analizada, cm, nome="pagar", cliente=None, modo="1"):
		super().__init__(nome, io, msg_analizada, cm)

	def executa(self):
		respostas = get_respostas("pagar")
		
		if (u'datetime' in self.msg_analizada[u'entities']):
			data = self.msg_analizada[u'entities'][u'datetime'][0][u'values'][0][u'value']
			respostas = [resposta for resposta in respostas if "@datetime" in resposta]
			resposta = random.choice(respostas).replace("@datetime", data)
		else:
			respostas = [resposta for resposta in respostas if not "@datetime" in resposta]
			resposta = random.choice(respostas)

		self.io.imprime(resposta)
		salva(self.msg_analizada)