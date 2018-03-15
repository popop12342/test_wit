# -*- coding: utf-8 -*-
import random
from respostas import get_respostas
from entidades.obter_nome_aplicacao import obter_nome_aplicacao
from conversas import salva
from intencoes.intencao import Intencao
from contextos.contexto import Contexto

class Criar_aplicacao(Intencao):

    def __init__(self, io, msg_analizada, cliente, modo, cm, nome="criar_aplicacao"):
        super().__init__(nome, io, msg_analizada, cm)
        self.cliente = cliente
        self.modo = modo
        self.cm = cm

    def executa(self):
        nome = obter_nome_aplicacao(io=self.io, msg_analizada=self.msg_analizada, cliente=self.cliente, modo=self.modo, cm=self.cm)
        
        respostas = get_respostas("criar_aplicacao")
        resposta = random.choice(respostas)
        resposta = resposta.replace("@nome_aplicacao", nome)

        self.io.imprime(resposta)
        salva(self.msg_analizada)
        
        contexto = Contexto()
        contexto.aplicacao(nome)
        self.cm.adiciona(contexto)