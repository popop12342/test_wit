import unittest
import datetime
import random
from respostas import get_respostas
from exemplo_banco import iniciar
from my_io.IOTest import IOTest

class TestPagar(unittest.TestCase):

    def setUp(self):
        self.io = IOTest()
        self.modo = "1"
        self.que_fazer = '\nO que você gostaria de fazer hoje?'
        self.esperado = ['Escolha a forma de interação:', "1) texto", "2) audio", self.que_fazer]
        random.seed(0)
        self.possiveis_respostas = get_respostas("pagar")

    def test_detecta_pagar_agora(self):
        self.io.mensagens = [self.modo, "pagar", "cancelar"]
        iniciar(self.io)

        random.seed(0)
        self.possiveis_respostas = [resposta for resposta in self.possiveis_respostas if not "@datetime" in resposta]
        resposta = random.choice(self.possiveis_respostas)

        self.esperado.append(resposta)
        self.esperado.append(self.que_fazer)
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_detecta_pagar_frase(self):
        self.io.mensagens = [self.modo, "pagar uma conta", "cancelar"]
        iniciar(self.io)

        random.seed(0)
        self.possiveis_respostas = [resposta for resposta in self.possiveis_respostas if not "@datetime" in resposta]
        resposta = random.choice(self.possiveis_respostas)

        self.esperado.append(resposta)
        self.esperado.append(self.que_fazer)
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_detecta_pagar_amanha(self):
        self.io.mensagens = [self.modo, "pagar o boleto amanhã", "cancelar"]
        iniciar(self.io)

        random.seed(0)
        self.possiveis_respostas = [resposta for resposta in self.possiveis_respostas if "@datetime" in resposta]
        resposta = random.choice(self.possiveis_respostas)

        amanha = datetime.date.today() + datetime.timedelta(days=1)
        data = "20{}T00:00:00.000-07:00".format(amanha.strftime("%y-%m-%d"))
        self.esperado.append(resposta.replace("@datetime", data))
        self.esperado.append(self.que_fazer)
        self.assertEqual(self.io.impressoes, self.esperado)