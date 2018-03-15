import unittest
from wit import Wit
from entidades.obter_nome_aplicacao import obter_nome_aplicacao
from my_io.IOTest import IOTest


class TestObterNomeAplicacao(unittest.TestCase):

    def setUp(self):
        self.io = IOTest()
        self.cliente = Wit("EGYXBUP5MBO2C3FH67L6IP2JNZ3DLRCW")
        self.modo = "1"

    def test_nome_aplicacao_inicialmente_fornecido(self):
        msg_analizada = {'_text': ['aplicar', 'viagem', 'mesmo valor'], 'entities': {'intent': [{'confidence': 0.98450955141391, 'value': 'aplicar'}], 'nome_aplicacao': [{'confidence': 0.94776218843284, 'value': 'viagem', 'type': 'value'}], 'amount_of_money': [{'confidence': 0.9635075, 'value': 100, 'type': 'value', 'unit': 'BRL'}]}, 'msg_id': '0cPX2dM45YObKjVGB'}
        nome_aplicacao = obter_nome_aplicacao(io=self.io, msg_analizada=msg_analizada, cliente=self.cliente, modo=self.modo, cm=None)
        self.assertEqual(nome_aplicacao, 'viagem', "não detecta nome_aplicação")

    def test_nome_aplicacao_inicialmente_nao_fornecido(self):
        msg_analizada = {'_text': ['aplicar'], 'entities': {'intent': [{'confidence': 0.98450955141391, 'value': 'aplicar'}]}, 'msg_id': '0cPX2dM45YObKjVGB'}
        self.io.mensagens = ['carro']
        nome_aplicacao = obter_nome_aplicacao(io=self.io, msg_analizada=msg_analizada, cliente=self.cliente, modo=self.modo, cm=None)
        self.assertEqual(nome_aplicacao, 'carro')
        self.assertEqual(self.io.impressoes[0], 'Diga o nome da aplicação')

    def test_nome_aplicacao_fornecido_na_segunda_vez(self):
        msg_analizada = {'_text': ['aplicar'], 'entities': {'intent': [{'confidence': 0.98450955141391, 'value': 'aplicar'}]}, 'msg_id': '0cPX2dM45YObKjVGB'}
        self.io.mensagens = ['peixe', 'show']
        nome_aplicacao = obter_nome_aplicacao(io=self.io, msg_analizada=msg_analizada, cliente=self.cliente, modo=self.modo, cm=None)
        self.assertEqual(nome_aplicacao, 'show')
        self.assertEqual(self.io.impressoes[0], 'Diga o nome da aplicação')
        self.assertEqual(self.io.impressoes[1], 'Diga o nome da aplicação')

if __name__ == "__main__":
    unittest.main()