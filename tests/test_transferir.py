import unittest
import random
from respostas import get_respostas
from exemplo_banco import iniciar
from my_io.IOTest import IOTest

class TestTransferir(unittest.TestCase):

    def setUp(self):
        self.io = IOTest()
        self.modo = "1"
        self.que_fazer = '\nO que você gostaria de fazer hoje?'
        self.esperado = ['Escolha a forma de interação:', "1) texto", "2) audio", self.que_fazer]
        random.seed(0)
        self.possiveis_respostas = get_respostas("transferir")

    def test_detecta_transferir(self):
        self.io.mensagens = [self.modo, "transfira 30 reais para a conta 300195", "cancelar"]
        iniciar(self.io)

        random.seed(0)
        resposta = random.choice(self.possiveis_respostas).replace("@numero_conta", "300195").replace("@valor", "30")
        
        self.esperado.append(resposta)
        self.esperado.append(self.que_fazer)
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_detecta_transferir_sem_valor(self):
        self.io.mensagens = [self.modo, "transfira para a conta 399201", "50", "cancelar"]
        iniciar(self.io)

        random.seed(0)
        resposta = random.choice(self.possiveis_respostas).replace("@numero_conta", "399201").replace("@valor", "50")

        self.esperado.extend([
            "Diga o valor", 
            resposta, 
            self.que_fazer
        ])
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_detecta_transferir_sem_conta(self):
        self.io.mensagens = [self.modo, "transferir 60 reais", "003229", "cancelar"]
        iniciar(self.io)

        random.seed(0)
        resposta = random.choice(self.possiveis_respostas).replace("@numero_conta", "003229").replace("@valor", "60")

        self.esperado.extend([
            "Diga o número da conta", 
            resposta,
            self.que_fazer
        ])
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_detecta_transferir_sem_parametros(self):
        self.io.mensagens = [self.modo, "transferir", "488290", "40 R$", "cancelar"]
        iniciar(self.io)

        random.seed(0)
        resposta = random.choice(self.possiveis_respostas).replace("@numero_conta", "488290").replace("@valor", "40")
        
        self.esperado.extend([
            "Diga o número da conta", 
            "Diga o valor", 
            resposta, 
            self.que_fazer
        ])
        self.assertEqual(self.io.impressoes, self.esperado)