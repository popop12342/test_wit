import unittest
from wit import Wit
from my_io.IOTest import IOTest
from entidades.obter_numero_conta import obter_numero_conta

class TestObterNumeroConta(unittest.TestCase):

    def setUp(self):
        self.io = IOTest()
        self.cliente = Wit("EGYXBUP5MBO2C3FH67L6IP2JNZ3DLRCW")
        self.modo = "1"

    def test_numero_inicialmente_fornecido(self):
        msg_analizada = {'_text': ['transfira 50 reias para a conta 488192'], 'entities': {'intent': [{'confidence': 0.999996102388, 'value': 'transferir'}], 'numero_conta': [{'confidence': 0.96676956764313, 'value': 488192, 'type': 'value'}], 'amount_of_money': [{'confidence': 0.75993545605875, 'value': 50, 'type': 'value'}]}, 'msg_id': '0FaTzFtaBI9mEE9dB'}
        numero_conta = obter_numero_conta(io=self.io, msg_analizada=msg_analizada, cliente=self.cliente, modo=self.modo, cm=None)
        self.assertEqual(numero_conta, 488192)

    def test_numero_nao_inicialmente_fornecido(self):
        msg_analizada = {'_text': ['transferir'], 'entities': {'intent': [{'confidence': 0.999996102388, 'value': 'transferir'}]}, 'msg_id': '0FaTzFtaBI9mEE9dB'}
        self.io.mensagens = ["399301"]
        numero_conta = obter_numero_conta(io=self.io, msg_analizada=msg_analizada, cliente=self.cliente, modo=self.modo, cm=None)
        self.assertEqual(numero_conta, 399301)
        self.assertEqual(self.io.impressoes[0], "Diga o número da conta")

    def test_numero_fornecido_futuramente(self):
        msg_analizada = {'_text': ['transferir'], 'entities': {'intent': [{'confidence': 0.999996102388, 'value': 'transferir'}]}, 'msg_id': '0FaTzFtaBI9mEE9dB'}
        self.io.mensagens = ["esqueci", "continha", "399011"]
        numero_conta = obter_numero_conta(io=self.io, msg_analizada=msg_analizada, cliente=self.cliente, modo=self.modo, cm=None)
        self.assertEqual(numero_conta, 399011)
        for impressao in self.io.impressoes:
            self.assertEqual(impressao, "Diga o número da conta")
        self.assertEqual(len(self.io.impressoes), 3)