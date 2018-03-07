# -*- coding: utf-8 -*-
import random
from conversas import salva
from respostas import get_respostas

def greetings_hello(io, msg_analizada):
    respostas = get_respostas(u'greetings_hello')
    resposta = random.choice(respostas)
    io.imprime(resposta)
    salva(msg_analizada)