import unittest
from wit import Wit
from exemplo_banco import iniciar
from my_io.IOTest import IOTest

class TestGetLimite(unittest.TestCase):

    def setUp(self):
        self.cliente = Wit("EGYXBUP5MBO2C3FH67L6IP2JNZ3DLRCW")
        self.io = IOTest()
        self.modo = "1"
        self.que_fazer = '\nO que você gostaria de fazer hoje?'
        self.esperado = ['Escolha a forma de interação:', "1) texto", "2) audio", self.que_fazer, "Seu limite é de 100 R$", self.que_fazer]

    def test_detecta_get_limite(self):
        self.io.mensagens = [self.modo, "limite", "cancelar"]
        iniciar(self.io)
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_detecta_get_limite_frase(self):
        self.io.mensagens = [self.modo, "Gostaria de saber meu limite", "Cancelar"]
        iniciar(self.io)
        self.assertEqual(self.io.impressoes, self.esperado)