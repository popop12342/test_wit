# -*- coding: utf-8 -*-
import random
from respostas import get_respostas
from conversas import salva

def get_extrato(io, msg_analizada):
	respostas = get_respostas("get_extrato")
	index = random.randrange(0, len(respostas))
	io.imprime(respostas[index])
	salva(msg_analizada)