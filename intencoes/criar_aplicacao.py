# -*- coding: utf-8 -*-
import random
from respostas import get_respostas
from entidades.obter_nome_aplicacao import obter_nome_aplicacao
from conversas import salva
from intencoes.intencao import Intencao

class Criar_aplicacao(Intencao):

    def __init__(self, io, msg_analizada, cliente, modo, nome="criar_aplicacao"):
        super().__init__(nome, io, msg_analizada)
        self.cliente = cliente
        self.modo = modo

    def executa(self):
        nome = obter_nome_aplicacao(io=self.io, msg_analizada=self.msg_analizada, cliente=self.cliente, modo=self.modo)
        
        respostas = get_respostas("criar_aplicacao")
        resposta = random.choice(respostas)
        resposta = resposta.replace("@nome_aplicacao", nome)

        self.io.imprime(resposta)
        salva(self.msg_analizada)