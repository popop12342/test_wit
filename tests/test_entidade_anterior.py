import unittest
from exemplo_banco import iniciar
from my_io.IOTest import IOTest

class TestEntidadeAnterior(unittest.TestCase):

    def setUp(self):
        self.io = IOTest()
        self.modo = "1"
        self.que_fazer = "\nO que você gostaria de fazer hoje?"
        self.esperado = ['Escolha a forma de interação:', "1) texto", "2) audio", self.que_fazer]

    def test_nome_aplicacao_anterior(self):
        self.io.mensagens = [
            self.modo, 
            "crie uma aplicação chamada faculdade", 
            "aplique 30 reais nessa aplicação", 
            "cancelar"
        ]
        iniciar(self.io)
        self.esperado.extend([
            "Criando aplicação faculdade", 
            self.que_fazer, 
            "Aplicando 30 R$ em faculdade", 
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
        self.esperado.extend([
            "Criando aplicação pé de meia", 
            self.que_fazer, 
            "Diga o nome da aplicação", 
            "Diga o valor", 
            "Aplicando 20 R$ em pé de meia", 
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
        self.esperado.extend([
            "Transferindo 40 R$ para a conta 399200", 
            self.que_fazer, 
            "Transferindo 100 R$ para a conta 399200", 
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
        self.esperado.extend([
            "Transferindo 100 R$ para a conta 399203", 
            self.que_fazer, 
            "Diga o número da conta", 
            "Transferindo 50 R$ para a conta 399203", 
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
        self.esperado.extend([
            "Aplicando 50 R$ em viagem", 
            self.que_fazer, 
            "Transferindo 50 R$ para a conta 499012", 
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
        self.esperado.extend([
            "Transferindo 70 R$ para a conta 399450", 
            self.que_fazer, 
            "Diga o valor", 
            "Aplicando 70 R$ em carro", 
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
        self.esperado.extend([
            "Transferindo 100 R$ para a conta 499200", 
            self.que_fazer, 
            "Transferindo 100 R$ para a conta 499200", 
            self.que_fazer
        ])
        self.assertEqual(self.io.impressoes, self.esperado)