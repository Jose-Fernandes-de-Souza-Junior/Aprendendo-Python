class quad:

	def __init__(self,lado):
		self.lado = lado

	def tamanho(self):
		self.area = self.lado*self.lado

	def alterar(self,novoValor):
		self.lado = novoValor

	def retornar(self):
		print(f"O tamanho do lado é: {self.lado} mts\n A area do quadrado é: {self.area}m²")