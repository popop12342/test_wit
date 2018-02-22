import unittest
from exemplo_banco import iniciar
from my_io.IOTest import IOTest

class TestGetSaldo(unittest.TestCase):

    def setUp(self):
        self.io = IOTest()
        self.modo = "1"
        self.que_fazer = '\nO que você gostaria de fazer hoje?'
        self.esperado = ['Escolha a forma de interação:', "1) texto", "2) audio", self.que_fazer, "Seu saldo é de 10 R$", self.que_fazer]

    def test_detecta_get_saldo(self):
        self.io.mensagens = [self.modo, "saldo", "cancelar"]
        iniciar(self.io)
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_detecta_get_saldo_frase(self):
        self.io.mensagens = [self.modo, "Qual é o meu saldo?", "cancelar"]
        iniciar(self.io)
        self.assertEqual(self.io.impressoes, self.esperado)