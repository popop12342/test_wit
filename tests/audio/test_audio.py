import unittest
import random
from respostas import get_respostas
from exemplo_banco import iniciar
from my_io.IOTest import IOTest
from recorder import read_audio

class TestAudio(unittest.TestCase):

    def setUp(self):
        self.io = IOTest()
        self.modo = "2"
        self.que_fazer = "\nO que você gostaria de fazer hoje?"
        self.esperado = ['Escolha a forma de interação:', "1) texto", "2) audio", self.que_fazer]
        random.seed(0)

    def test_saldo(self):
        self.io.mensagens = [self.modo, "wav/saldo.wav", "wav/cancelar.wav"]
        iniciar(self.io)

        random.seed(0)
        possiveis_respostas = get_respostas("get_saldo")
        resposta = random.choice(possiveis_respostas)

        self.esperado.extend([resposta, self.que_fazer])
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_extrato(self):
        self.io.mensagens = [self.modo, "wav/extrato.wav", "wav/cancelar.wav"]
        iniciar(self.io)

        random.seed(0)
        possiveis_respostas = get_respostas("get_extrato")
        resposta = random.choice(possiveis_respostas)

        self.esperado.extend([resposta, self.que_fazer])
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_limite(self):
        self.io.mensagens = [self.modo, "wav/limite.wav", "wav/cancelar.wav"]
        iniciar(self.io)

        random.seed(0)
        possiveis_respostas = get_respostas("get_limite")
        resposta = random.choice(possiveis_respostas)

        self.esperado.extend([resposta, self.que_fazer])
        self.assertEqual(self.io.impressoes, self.esperado)

    @unittest.expectedFailure
    def test_pagar(self):
        self.io.mensagens = [self.modo, "wav/pagar.wav", "wav/cancelar.wav"]
        iniciar(self.io)
        self.esperado.extend(["Pagamento agendado para agora", self.que_fazer])
        self.assertEqual(self.io.impressoes, self.esperado, "Não reconhece audio pagar")

    def test_criar_aplicacao(self):
        self.io.mensagens = [self.modo, "wav/criar_aplicacao.wav", "wav/nome_aplicacao.wav", "wav/cancelar.wav"]
        iniciar(self.io)

        random.seed(0)
        possiveis_respostas = get_respostas("criar_aplicacao")
        resposta = random.choice(possiveis_respostas).replace("@nome_aplicacao", "viagem")

        self.esperado.extend(["Diga o nome da aplicação", resposta, self.que_fazer])
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_aplicar(self):
        self.io.mensagens = [
            self.modo,
            "wav/aplicar.wav", 
            "wav/nome_aplicacao.wav", 
            "wav/50reais.wav", 
            "wav/cancelar.wav"
        ]
        iniciar(self.io)

        random.seed(0)
        possiveis_respostas = get_respostas("aplicar")
        resposta = random.choice(possiveis_respostas).replace("@nome_aplicacao", "viagem").replace("@valor", "50")

        self.esperado.extend([
            "Diga o nome da aplicação", 
            "Diga o valor", 
            resposta, 
            self.que_fazer
        ])
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_transferir(self):
        self.io.mensagens = [
            self.modo, 
            "wav/transferir.wav", 
            "wav/numero_conta.wav", 
            "wav/50reais.wav", 
            "wav/cancelar.wav"
        ]
        iniciar(self.io)

        random.seed(0)
        possiveis_respostas = get_respostas("transferir")
        resposta = random.choice(possiveis_respostas).replace("@numero_conta", "123456").replace("@valor", "50")

        self.esperado.extend([
            "Diga o número da conta", 
            "Diga o valor", 
            resposta, 
            self.que_fazer
        ])
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_mesma_conta(self):
        self.io.mensagens = [
            self.modo, 
            "wav/transferir.wav", 
            "wav/numero_conta.wav", 
            "wav/50reais.wav", 
            "wav/transferir.wav", 
            "wav/mesma_conta.wav", 
            "wav/50reais.wav", 
            "wav/cancelar.wav"
        ]
        iniciar(self.io)

        random.seed(0)
        possiveis_respostas = get_respostas("transferir")
        resposta1 = random.choice(possiveis_respostas).replace("@numero_conta", "123456").replace("@valor", "50")
        resposta2 = random.choice(possiveis_respostas).replace("@numero_conta", "123456").replace("@valor", "50")

        self.esperado.extend([
            "Diga o número da conta",
            "Diga o valor",
            resposta1,
            self.que_fazer,
            "Diga o número da conta", 
            "Diga o valor",
            resposta2,
            self.que_fazer
        ])
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_mesmo_valor(self):
        self.io.mensagens = [
            self.modo,
            "wav/transferir.wav",
            "wav/numero_conta.wav",
            "wav/50reais.wav",
            "wav/aplicar.wav", 
            "wav/nome_aplicacao.wav",
            "wav/mesmo_valor.wav",
            "wav/cancelar.wav"
        ]
        iniciar(self.io)

        random.seed(0)
        possiveis_respostas = get_respostas("transferir")
        resposta1 = random.choice(possiveis_respostas).replace("@numero_conta", "123456").replace("@valor", "50")

        possiveis_respostas = get_respostas("aplicar")
        resposta2 = random.choice(possiveis_respostas).replace("@valor", "50").replace("@nome_aplicacao", "viagem")

        self.esperado.extend([
            "Diga o número da conta",
            "Diga o valor",
            resposta1, 
            self.que_fazer,
            "Diga o nome da aplicação",
            "Diga o valor", 
            resposta2, 
            self.que_fazer 
        ])
        self.assertEqual(self.io.impressoes, self.esperado)

    @unittest.expectedFailure
    def test_mesma_aplicacao(self):
        self.io.mensagens = [
            self.modo,
            "wav/criar_aplicacao.wav",
            "wav/nome_aplicacao.wav",
            "wav/aplicar.wav",
            "wav/mesma_aplicacao.wav", 
            "wav/50reais.wav",
            "wav/cancelar.wav"
        ]
        iniciar(self.io)

        random.seed(0)
        possiveis_respostas = get_respostas("criar_aplicacao")
        resposta1 = random.choice(possiveis_respostas)

        possiveis_respostas = get_respostas("aplicar")
        resposta2 = random.choice(possiveis_respostas)

        self.esperado.extend([
            "Diga o nome da aplicação",
            resposta1,
            self.que_fazer,
            "Diga o nome da aplicação",
            "Diga o valor",
            resposta2,
            self.que_fazer
        ])
        self.assertEqual(self.io.impressoes, self.esperado)