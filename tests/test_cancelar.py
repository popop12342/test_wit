import unittest
from exemplo_banco import iniciar
from my_io.IOTest import IOTest

class TestCancelar(unittest.TestCase):

    def setUp(self):
        self.io = IOTest()
        self.modo = "1"
        self.que_fazer = "\nO que você gostaria de fazer hoje?"
        self.esperado = ['Escolha a forma de interação:', "1) texto", "2) audio", self.que_fazer]

    def test_cancelar(self):
        self.io.mensagens = [self.modo, "cancelar"]
        iniciar(self.io)
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_cancelar_transferencia(self):
        self.io.mensagens = [self.modo, "transferir", "cancelar", "cancelar"]
        iniciar(self.io)
        self.esperado.extend(["Diga o número da conta", self.que_fazer])
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_cancelar_aplicacao(self):
        self.io.mensagens = [self.modo, "aplicar", "faculdade", "cancelar", "cancelar"]
        iniciar(self.io)
        self.esperado.extend(["Diga o nome da aplicação", "Diga o valor", self.que_fazer])
        self.assertEqual(self.io.impressoes, self.esperado)