import random
import unittest
from respostas import get_respostas
from exemplo_banco import iniciar
from my_io.IOTest import IOTest

class TestGetLimite(unittest.TestCase):

    def setUp(self):
        self.io = IOTest()
        self.modo = "1"
        self.que_fazer = '\nO que você gostaria de fazer hoje?'
        self.possiveis_respostas = get_respostas("get_limite")
        random.seed(0)
        index = random.randrange(0, len(self.possiveis_respostas))
        self.esperado = ['Escolha a forma de interação:', "1) texto", "2) audio", self.que_fazer, self.possiveis_respostas[index], self.que_fazer]
        random.seed(0)

    def test_detecta_get_limite(self):
        self.io.mensagens = [self.modo, "limite", "cancelar"]
        iniciar(self.io)
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_detecta_get_limite_frase(self):
        self.io.mensagens = [self.modo, "Gostaria de saber meu limite", "Cancelar"]
        iniciar(self.io)
        self.assertEqual(self.io.impressoes, self.esperado)