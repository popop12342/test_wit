import unittest
from exemplo_banco import iniciar
from my_io.IOTest import IOTest
from recorder import read_audio

class TestAudio(unittest.TestCase):

    def setUp(self):
        self.io = IOTest()
        self.modo = "2"
        self.que_fazer = "\nO que você gostaria de fazer hoje?"
        self.esperado = ['Escolha a forma de interação:', "1) texto", "2) audio", self.que_fazer]

    def test_saldo(self):
        self.io.mensagens = [self.modo, "wav/saldo.wav", "wav/cancelar.wav"]
        iniciar(self.io)
        self.esperado.extend(["Seu saldo é de 10 R$", self.que_fazer])
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_extrato(self):
        self.io.mensagens = [self.modo, "wav/extrato.wav", "wav/cancelar.wav"]
        iniciar(self.io)
        self.esperado.extend(["Mostrando extrato", self.que_fazer])
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_limite(self):
        self.io.mensagens = [self.modo, "wav/limite.wav", "wav/cancelar.wav"]
        iniciar(self.io)
        self.esperado.extend(["Seu limite é de 100 R$", self.que_fazer])
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
        self.esperado.extend(["Diga o nome da aplicação", "Criando aplicação viagem", self.que_fazer])
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
        self.esperado.extend([
            "Diga o nome da aplicação", 
            "Diga o valor", 
            "Aplicando 50 R$ em viagem", 
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
        self.esperado.extend([
            "Diga o número da conta", 
            "Diga o valor", 
            "Transferindo 50 R$ para a conta 123456", 
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
        self.esperado.extend([
            "Diga o número da conta",
            "Diga o valor",
            "Transferindo 50 R$ para a conta 123456",
            self.que_fazer,
            "Diga o número da conta", 
            "Diga o valor",
            "Transferindo 50 R$ para a conta 123456",
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
        self.esperado.extend([
            "Diga o número da conta",
            "Diga o valor",
            "Transferindo 50 R$ para a conta 123456", 
            self.que_fazer,
            "Diga o nome da aplicação",
            "Diga o valor", 
            "Aplicando 50 R$ em viagem", 
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
        self.esperado.extend([
            "Diga o nome da aplicação",
            "Criando aplicação viagem",
            self.que_fazer,
            "Diga o nome da aplicação",
            "Diga o valor",
            "Aplicando 50 R$ em viagem",
            self.que_fazer
        ])
        self.assertEqual(self.io.impressoes, self.esperado)