class Produto:
    def __init__(self,nome,preco):
        self.nome = nome 
        self.preco = preco
    

    def desconto (self,percentual):
        self.preco  = self.preco - (self.preco*(percentual/100))

    def quantidade (self,unidades):
        self.unidades = unidades

    @property 
    def preco (self):
        return self._preco
    
    @preco.setter
    def preco (self,valor):
        if isinstance (valor,str):
            valor = float (valor.replace ('R$ ',''))

        self.preco = valor

   
        

p1 = Produto("Vestido",100)
p1.desconto('R$ 10')
p1.quantidade(5)
print ("Total Liquido: ",p1.preco*p1.unidades)

