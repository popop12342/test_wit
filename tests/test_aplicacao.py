# -*- coding: utf-8 -*-

import unittest
import random
from respostas import get_respostas
from exemplo_banco import iniciar
from my_io.IOTest import IOTest

class TestAplicacao(unittest.TestCase):

    def setUp(self):
        self.io = IOTest()
        self.modo = "1"
        self.que_fazer = '\nO que você gostaria de fazer hoje?'
        self.esperado = ['Escolha a forma de interação:', "1) texto", "2) audio", self.que_fazer]
        random.seed(0)

    def test_detecta_criar_aplicacao(self):
        self.io.mensagens = [self.modo, 'crie uma aplicação chamada carro', "cancelar"]
        iniciar(self.io)

        random.seed(0)
        possiveis_respostas = get_respostas("criar_aplicacao")
        resposta = random.choice(possiveis_respostas).replace("@nome_aplicacao", "carro")

        self.esperado.append(resposta)
        self.esperado.append(self.que_fazer)
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_criar_aplicacao_passos(self):
        self.io.mensagens = [self.modo, "criar uma aplicação", "pe de meia", "cancelar"]
        iniciar(self.io)
        
        random.seed(0)
        possiveis_respostas = get_respostas("criar_aplicacao")
        resposta = random.choice(possiveis_respostas).replace("@nome_aplicacao", "pé de meia")

        self.esperado.extend(["Diga o nome da aplicação", resposta, self.que_fazer])
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_detecta_aplicar(self):
        self.io.mensagens = [self.modo, "aplique 50 reais em faculdade", "cancelar"]
        iniciar(self.io)

        random.seed(0)
        possiveis_respostas = get_respostas("aplicar")
        resposta = random.choice(possiveis_respostas).replace("@nome_aplicacao", "faculdade").replace("@valor", "50")

        self.esperado.extend([resposta, self.que_fazer])
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_aplicar_em_passos(self):
        self.io.mensagens = [self.modo, "aplicar", "viagem", "100", "cancelar"]
        iniciar(self.io)

        random.seed(0)
        possiveis_respostas = get_respostas("aplicar")
        resposta = random.choice(possiveis_respostas).replace("@nome_aplicacao", "viagem").replace("@valor", "100")

        self.esperado.extend(["Diga o nome da aplicação", "Diga o valor", resposta, self.que_fazer])
        self.assertEqual(self.io.impressoes, self.esperado)
        