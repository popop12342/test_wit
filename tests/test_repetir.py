import unittest
import random
from respostas import get_respostas
from exemplo_banco import iniciar
from my_io.IOTest import IOTest

class TestRepetir(unittest.TestCase):

    def setUp(self):
        self.io = IOTest()
        self.modo = "1"
        self.que_fazer = "\nO que você gostaria de fazer hoje?"
        self.esperado = ['Escolha a forma de interação:', "1) texto", "2) audio", self.que_fazer]
        random.seed(0)

    def test_repetir_saldo(self):
        self.possiveis_respostas = get_respostas("get_saldo")
        index1 = random.randrange(0, len(self.possiveis_respostas))
        index2 = random.randrange(0, len(self.possiveis_respostas))
        self.io.mensagens = [self.modo, "Me mostre meu saldo", "repita", "cancelar"]
        random.seed(0)
        iniciar(self.io)
        self.esperado.extend([
            self.possiveis_respostas[index1], 
            self.que_fazer, 
            self.possiveis_respostas[index2], 
            self.que_fazer
        ])
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_repetir_aplicar(self):
        self.io.mensagens = [self.modo, "aplique 30 reais em pe de meia", "repita", "cancelar"]
        iniciar(self.io)

        random.seed(0)
        possiveis_respostas = get_respostas("aplicar")
        resposta1 = random.choice(possiveis_respostas).replace("@valor", "30").replace("@nome_aplicacao", "pé de meia")
        resposta2 = random.choice(possiveis_respostas).replace("@valor", "30").replace("@nome_aplicacao", "pé de meia")
        
        self.esperado.extend([
            resposta1,
            self.que_fazer, 
            resposta2, 
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

        random.seed(0)
        possiveis_respostas = get_respostas("transferir")
        resposta1 = random.choice(possiveis_respostas).replace("@numero_conta", "993200").replace("@valor", "100")
        resposta2 = random.choice(possiveis_respostas).replace("@numero_conta", "993200").replace("@valor", "100")

        self.esperado.extend([
            "Diga o número da conta", 
            "Diga o valor", 
            resposta1, 
            self.que_fazer, 
            resposta2, 
            self.que_fazer
        ])
        self.assertEqual(self.io.impressoes, self.esperado)
