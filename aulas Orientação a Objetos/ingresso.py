class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprimeValor(self):
        print(f"Valor: {self.valor}")

class VIP(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)
        
    
    def imprimeVIP(self):
        self.valor_adicional = self.valor+self.valor*0.1
        print(f"VIP: {self.valor_adicional}")

class Camarote (Ingresso):
    def __init__(self, valor):
        super().__init__(valor)
        
    def imprimeCamarote(self):
        self.valor_add = self.valor+self.valor*0.35
        print(f"Camarote: {self.valor_add}")


preco1 = Ingresso(245)
preco1.imprimeValor()

preco2 = VIP(preco1.valor)
preco2.imprimeVIP()


preco3 = Camarote (preco1.valor)
preco3.imprimeCamarote()

