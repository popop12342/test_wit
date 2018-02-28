# -*- coding: utf-8 -*-
import random
from conversas import salva
from respostas import get_respostas

def get_limite(io, msg_analizada):
	respostas = get_respostas(u'get_limite')
	index = random.randrange(0, len(respostas))
	io.imprime(respostas[index])
	salva(msg_analizada)