# -*- coding: utf-8 -*-

class Contexto:

    def __init__(self, nome=None, tempo_vida=5):
        self.__nome = nome
        self.__entidades = {}
        self.__tempo_vida = tempo_vida

    @property
    def nome(self):
        return self.__nome

    @property
    def entidades(self):
        return self.__entidades

    def diminui_vida(self):
        self.__tempo_vida -= 1

    def busca(self, entidade):
        if (entidade in self.__entidades):
            return self.__entidades[entidade]
        return "nao encontrado"

    def aplicacao(self, nome_aplicacao, amount_of_money=None):
        self.__nome = "aplicacao"
        self.__entidades["nome_aplicacao"] = nome_aplicacao
        if (amount_of_money):
            self.__entidades["amount_of_money"] = amount_of_money

    def transferencia(self, numero_conta, amount_of_money):
        self.__nome = "transferencia"
        self.__entidades["numero_conta"] = numero_conta
        self.__entidades["amount_of_money"] = amount_of_money

    def ativo(self):
        return self.__tempo_vida > 0