# -*- coding: utf-8 -*-
import random
from respostas import get_respostas
from conversas import salva

class Intencao:


    def __init__(self, nome, io, msg_analizada, cm, cliente=None, modo="1"):
        self.nome = nome
        self.io = io
        self.msg_analizada = msg_analizada
        self.cm = cm

    def executa(self):
        respostas = get_respostas(self.nome)
        resposta = random.choice(respostas)
        self.io.imprime(resposta)
        salva(self.msg_analizada)