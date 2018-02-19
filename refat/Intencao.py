class Intencao:

	self.__entidades = []

	def __init__(self, nome):
		self.__nome = nome

	def executar(self):
		print("executando a intencao {}".format(self.__nome))