# -*- coding: utf-8 -*-

class ContextoManager:

    def __init__(self):
        self.contextos = {}

    def adiciona(self, contexto):
        self.contextos[contexto.nome] = contexto

    def busca(self, contexto, entidade):
        if (contexto in self.contextos):
            valor = self.contextos[contexto].busca(entidade)
            if (not self.contextos[contexto].ativo()):
                self.contextos.pop(contexto)
            return valor
        return "nao encontrado"

    def atualiza(self):
        for contexto in self.contextos:
            self.contextos[contexto].diminui_vida()