class IOManager:

    def imprime(self, text):
        print(text)

    def le(self, text=None):
        if text:
            return input(text)
        return input()