class Pilha:

	def __init__(self):
		self.dados = []

	def push(self, item):
		self.dados.append(item)

	def pop(self):
		return self.dados.pop()

	def is_empty(self):
		return self.dados == []