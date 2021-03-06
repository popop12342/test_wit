# -*- coding: utf-8 -*-

import random
from intencoes.intencao import Intencao
from conversas import salva
from respostas import get_respostas
from entidades.obter_nome_aplicacao import obter_nome_aplicacao
from entidades.obter_valor import obter_valor
from contextos.contexto import Contexto

class Aplicar(Intencao):

    def __init__(self, io, msg_analizada, cliente, modo, cm, nome="aplicar"):
        super().__init__(nome, io, msg_analizada, cm)
        self.cliente = cliente
        self.modo = modo

    def executa(self):
        nome = obter_nome_aplicacao(io=self.io, msg_analizada=self.msg_analizada, cliente=self.cliente, modo=self.modo, cm=self.cm)
        valor = obter_valor(self.io, self.msg_analizada, self.cliente, self.modo, self.cm)
        
        respostas = get_respostas(self.nome)
        resposta = random.choice(respostas)
        resposta = resposta.replace("@nome_aplicacao", nome).replace("@valor", str(valor))

        self.io.imprime(resposta)
        salva(self.msg_analizada)

        contexto = Contexto()
        contexto.aplicacao(nome, valor)
        self.cm.adiciona(contexto)