from my_io.IOManager import IOManager

class IOTest(IOManager):

    def __init__(self, mensagens):
        self.mensagens = mensagens
        self.impressoes = []

    def le(self):
        return self.mensagens.pop(0)

    def imprime(self, text):
        self.impressoes.append(text)

        