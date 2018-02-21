import unittest
from wit import Wit
from entidades.obter_valor import obter_valor
from my_io.IOTest import IOTest

class TestObterValor(unittest.TestCase):

    def setUp(self):
        self.io = IOTest([])
        self.cliente = Wit("EGYXBUP5MBO2C3FH67L6IP2JNZ3DLRCW")
        self.modo = "1"

    def test_valor_inicialmente_fornecido(self):
        resposta = {'_text': ['aplique 40 reais em show'], 'entities': {'intent': [{'confidence': 0.99932068639867, 'value': 'aplicar'}], 'nome_aplicacao': [{'confidence': 0.89477890285309, 'value': 'show', 'type': 'value'}], 'amount_of_money': [{'confidence': 0.9666425, 'value': 40, 'type': 'value', 'unit': 'BRL'}]}, 'msg_id': '0BQc8Rbe7c8PF7Plq'}
        valor = obter_valor(io=self.io, resposta=resposta, cliente=self.cliente, modo=self.modo)
        self.assertEqual(valor, 40)

    def test_valor_nao_inicialmente_fornecido(self):
        resposta = {'_text': ['aplique'], 'entities': {'intent': [{'confidence': 0.99932068639867, 'value': 'aplicar'}]}, 'msg_id': '0BQc8Rbe7c8PF7Plq'}
        self.io.mensagens = ["20 reais"]
        valor = obter_valor(io=self.io, resposta=resposta, cliente=self.cliente, modo=self.modo)
        self.assertEqual(valor, 20)
        self.assertEqual(self.io.impressoes[0], "Diga o valor")

    def test_valor_fornecido_futuramente(self):
        resposta = {'_text': ['aplique'], 'entities': {'intent': [{'confidence': 0.99932068639867, 'value': 'aplicar'}]}, 'msg_id': '0BQc8Rbe7c8PF7Plq'}
        self.io.mensagens = ["qualquer", "nenhum", "60 reais"]
        valor = obter_valor(io=self.io, resposta=resposta, cliente=self.cliente, modo=self.modo)
        self.assertEqual(valor, 60)
        for impressao in self.io.impressoes:
            self.assertEqual(impressao, "Diga o valor")
        self.assertEqual(len(self.io.impressoes), 3)