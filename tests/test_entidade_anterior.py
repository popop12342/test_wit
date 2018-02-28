import unittest
import random
from respostas import get_respostas
from exemplo_banco import iniciar
from my_io.IOTest import IOTest

class TestEntidadeAnterior(unittest.TestCase):

    def setUp(self):
        self.io = IOTest()
        self.modo = "1"
        self.que_fazer = "\nO que você gostaria de fazer hoje?"
        self.esperado = ['Escolha a forma de interação:', "1) texto", "2) audio", self.que_fazer]
        random.seed(0)

    def test_nome_aplicacao_anterior(self):
        self.io.mensagens = [
            self.modo, 
            "crie uma aplicação chamada faculdade", 
            "aplique 30 reais nessa aplicação", 
            "cancelar"
        ]
        iniciar(self.io)

        possiveis_respostas = get_respostas("criar_aplicacao")
        random.seed(0)
        resposta1 = random.choice(possiveis_respostas).replace("@nome_aplicacao", "faculdade")

        possiveis_respostas = get_respostas("aplicar")
        resposta2 = random.choice(possiveis_respostas).replace("@nome_aplicacao", "faculdade").replace("@valor", "30")

        self.esperado.extend([
            resposta1, 
            self.que_fazer, 
            resposta2, 
            self.que_fazer
        ])
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_nome_aplicacao_anterior_etapas(self):
        self.io.mensagens = [
            self.modo, 
            "crie uma aplicação chamada pé de meia", 
            "aplicar", 
            "mesma aplicação", 
            "20 R$", 
            "cancelar"
        ]
        iniciar(self.io)

        random.seed(0)
        possiveis_respostas = get_respostas("criar_aplicacao")
        resposta1 = random.choice(possiveis_respostas).replace("@nome_aplicacao", "pé de meia")

        possiveis_respostas = get_respostas("aplicar")
        resposta2 = random.choice(possiveis_respostas).replace("@nome_aplicacao", "pé de meia").replace("@valor", "20")

        self.esperado.extend([
            resposta1, 
            self.que_fazer, 
            "Diga o nome da aplicação", 
            "Diga o valor", 
            resposta2, 
            self.que_fazer
        ])
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_numero_conta_anterior(self):
        self.io.mensagens = [
            self.modo, 
            "transfira 40 reais em 399200", 
            "transfira 100 reais na mesma conta", 
            "cancelar"
        ]
        iniciar(self.io)

        random.seed(0)
        possiveis_respostas = get_respostas("transferir")
        resposta1 = random.choice(possiveis_respostas).replace("@numero_conta", "399200").replace("@valor", "40")
        resposta2 = random.choice(possiveis_respostas).replace("@numero_conta", "399200").replace("@valor", "100")

        self.esperado.extend([
            resposta1, 
            self.que_fazer, 
            resposta2, 
            self.que_fazer
        ])
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_numero_conta_anterior_etapas(self):
        self.io.mensagens = [
            self.modo,
            "transfira 100 reais para a conta 399203", 
            "transferir 50 reais", 
            "mesma conta", 
            "cancelar"
        ]
        iniciar(self.io)

        random.seed(0)
        possiveis_respostas = get_respostas("transferir")
        resposta1 = random.choice(possiveis_respostas).replace("@numero_conta", "399203").replace("@valor", "100")
        resposta2 = random.choice(possiveis_respostas).replace("@numero_conta", "399203").replace("@valor", "50")

        self.esperado.extend([
            resposta1, 
            self.que_fazer, 
            "Diga o número da conta", 
            resposta2, 
            self.que_fazer
        ])
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_valor_anterior(self):
        self.io.mensagens = [
            self.modo, 
            "aplique 50 reais em viagem", 
            "transfira o mesmo valor para 499012", 
            "cancelar"
        ]
        iniciar(self.io)

        random.seed(0)
        possiveis_respostas = get_respostas("aplicar")
        resposta1 = random.choice(possiveis_respostas).replace("@nome_aplicacao", "viagem").replace("@valor", "50")

        possiveis_respostas = get_respostas("transferir")
        resposta2 = random.choice(possiveis_respostas).replace("@numero_conta", "499012").replace("@valor", "50")

        self.esperado.extend([
            resposta1, 
            self.que_fazer, 
            resposta2, 
            self.que_fazer
        ])
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_valor_anterior_etapas(self):
        self.io.mensagens = [
            self.modo, 
            "transfira 70 reais para 399450", 
            "aplicar em carro", 
            "o valor anterior", 
            "cancelar"
        ]
        iniciar(self.io)

        random.seed(0)
        possiveis_respostas = get_respostas("transferir")
        resposta1 = random.choice(possiveis_respostas).replace("@valor", "70").replace("@numero_conta", "399450")

        possiveis_respostas = get_respostas("aplicar")
        resposta2 = random.choice(possiveis_respostas).replace("@nome_aplicacao", "carro").replace("@valor", "70")

        self.esperado.extend([
            resposta1, 
            self.que_fazer, 
            "Diga o valor", 
            resposta2, 
            self.que_fazer
        ])
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_valor_e_conta_anterior(self):
        self.io.mensagens = [
            self.modo, 
            "transfira 100 reais para a conta 499200", 
            "transfira o mesmo valor para a mesma conta", 
            "cancelar"
        ]
        iniciar(self.io)

        random.seed(0)
        possiveis_respostas = get_respostas("transferir")
        resposta1 = random.choice(possiveis_respostas).replace("@numero_conta", "499200").replace("@valor", "100")
        resposta2 = random.choice(possiveis_respostas).replace("@numero_conta", "499200").replace("@valor", "100")

        self.esperado.extend([
            resposta1, 
            self.que_fazer, 
            resposta2, 
            self.que_fazer
        ])
        self.assertEqual(self.io.impressoes, self.esperado)