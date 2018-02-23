import unittest
import datetime
from exemplo_banco import iniciar
from my_io.IOTest import IOTest

class TestPagar(unittest.TestCase):

    def setUp(self):
        self.io = IOTest()
        self.modo = "1"
        self.que_fazer = '\nO que você gostaria de fazer hoje?'
        self.esperado = ['Escolha a forma de interação:', "1) texto", "2) audio", self.que_fazer]

    def test_detecta_pagar_agora(self):
        self.io.mensagens = [self.modo, "pagar", "cancelar"]
        iniciar(self.io)
        self.esperado.append("Pagamento agendado para agora")
        self.esperado.append(self.que_fazer)
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_detecta_pagar_frase(self):
        self.io.mensagens = [self.modo, "pagar uma conta", "cancelar"]
        iniciar(self.io)
        self.esperado.append("Pagamento agendado para agora")
        self.esperado.append(self.que_fazer)
        self.assertEqual(self.io.impressoes, self.esperado)

    def test_detecta_pagar_amanha(self):
        self.io.mensagens = [self.modo, "pagar o boleto amanhã", "cancelar"]
        iniciar(self.io)
        amanha = datetime.date.today() + datetime.timedelta(days=1)
        data = "20{}T00:00:00.000-08:00".format(amanha.strftime("%y-%m-%d"))
        self.esperado.append("Pagamento agendado para {}".format(data))
        self.esperado.append(self.que_fazer)
        self.assertEqual(self.io.impressoes, self.esperado)