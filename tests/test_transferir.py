import unittest
from wit import Wit
from exemplo_banco import iniciar
from my_io.IOTest import IOTest

class TestTransferir(unittest.TestCase):

    def setUp(self):
        self.cliente = Wit("EGYXBUP5MBO2C3FH67L6IP2JNZ3DLRCW")
        self.io = IOTest()
        self.modo = "1"
        self.que_fazer = '\nO que você gostaria de fazer hoje?'
        self.esperado = ['Escolha a forma de interação:', "1) texto", "2) audio", self.que_fazer]

    def test_detecta_transferir(self):
        self.io.mensagens = [self.modo, "transfira 30 reais para a conta 300195", "cancelar"]
        iniciar(self.io)
        self.esperado.append("Transferindo 30 R$ para a conta 300195")
        self.esperado.append(self.que_fazer)
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_detecta_transferir_sem_valor(self):
        self.io.mensagens = [self.modo, "transfira para a conta 399201", "50", "cancelar"]
        iniciar(self.io)
        self.esperado.extend(["Diga o valor", "Transferindo 50 R$ para a conta 399201", self.que_fazer])
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_detecta_transferir_sem_conta(self):
        self.io.mensagens = [self.modo, "transferir 60 reais", "003229", "cancelar"]
        iniciar(self.io)
        self.esperado.extend(["Diga o número da conta", "Transferindo 60 R$ para a conta 003229", self.que_fazer])
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_detecta_transferir_sem_parametros(self):
        self.io.mensagens = [self.modo, "transferir", "488290", "40 R$", "cancelar"]
        iniciar(self.io)
        self.esperado.extend(["Diga o número da conta", "Diga o valor", "Transferindo 40 R$ para a conta 488290", self.que_fazer])
        self.assertEqual(self.io.impressoes, self.esperado)