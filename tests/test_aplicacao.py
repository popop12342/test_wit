# -*- coding: utf-8 -*-

import unittest
from wit import Wit
from exemplo_banco import iniciar
from my_io.IOTest import IOTest

class TestAplicacao(unittest.TestCase):

    def setUp(self):
        self.cliente = Wit("EGYXBUP5MBO2C3FH67L6IP2JNZ3DLRCW")
        self.io = IOTest()
        self.modo = "1"
        self.que_fazer = '\nO que você gostaria de fazer hoje?'
        self.esperado = ['Escolha a forma de interação:', "1) texto", "2) audio", self.que_fazer]

    def test_detecta_criar_aplicacao(self):
        self.io.mensagens = [self.modo, 'crie uma aplicação chamada carro', "cancelar"]
        iniciar(self.io)
        self.esperado.append('Criando aplicação carro')
        self.esperado.append(self.que_fazer)
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_criar_aplicacao_passos(self):
        self.io.mensagens = [self.modo, "criar uma aplicação", "pe de meia", "cancelar"]
        iniciar(self.io)
        self.esperado.append("Diga o nome da aplicação")
        self.esperado.append("Criando aplicação pé de meia")
        self.esperado.append(self.que_fazer)
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_detecta_aplicar(self):
        self.io.mensagens = [self.modo, "aplique 50 reais em faculdade", "cancelar"]
        iniciar(self.io)
        self.esperado.append("Aplicando 50 R$ em faculdade")
        self.esperado.append(self.que_fazer)
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_aplicar_em_passos(self):
        self.io.mensagens = [self.modo, "aplicar", "viagem", "100", "cancelar"]
        iniciar(self.io)
        self.esperado.append("Diga o nome da aplicação")
        self.esperado.append("Diga o valor")
        self.esperado.append("Aplicando 100 R$ em viagem")
        self.esperado.append(self.que_fazer)
        self.assertEqual(self.io.impressoes, self.esperado)
        