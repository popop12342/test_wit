import unittest
from exemplo_banco import iniciar
from my_io.IOTest import IOTest

class TestRepetir(unittest.TestCase):

    def setUp(self):
        self.io = IOTest()
        self.modo = "1"
        self.que_fazer = "\nO que você gostaria de fazer hoje?"
        self.esperado = ['Escolha a forma de interação:', "1) texto", "2) audio", self.que_fazer]

    def test_repetir_saldo(self):
        self.io.mensagens = [self.modo, "Me mostre meu saldo", "repita", "cancelar"]
        iniciar(self.io)
        self.esperado.extend([
            "Seu saldo é de 10 R$", 
            self.que_fazer, 
            "Seu saldo é de 10 R$", 
            self.que_fazer
        ])
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_repetir_aplicar(self):
        self.io.mensagens = [self.modo, "aplique 30 reais em pe de meia", "repita", "cancelar"]
        iniciar(self.io)
        self.esperado.extend([
            "Aplicando 30 R$ em pé de meia",
            self.que_fazer, 
            "Aplicando 30 R$ em pé de meia", 
            self.que_fazer
        ])
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_repetir_transferir(self):
        self.io.mensagens = [
            self.modo, 
            "transferir", 
            "993200", 
            "100", 
            "repetir", 
            "cancelar"
        ]
        iniciar(self.io)
        self.esperado.extend([
            "Diga o número da conta", 
            "Diga o valor", 
            "Transferindo 100 R$ para a conta 993200", 
            self.que_fazer, 
            "Transferindo 100 R$ para a conta 993200", 
            self.que_fazer
        ])
        self.assertEqual(self.io.impressoes, self.esperado)
