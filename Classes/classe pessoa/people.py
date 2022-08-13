class people:
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome  
        self.peso = peso
        self.idade = idade
        self.altura = altura

    def engordar(self):
        self.peso+=2

    def emagrecer(self):
        self.peso-=1


    def crescer (self):
        self.altura = self.altura+0.5

    def alterar(self,nvnome,nvidade,nvpeso,nvaltura):
        self.nome = nvnome  
        self.peso = nvpeso
        self.idade = nvidade
        self.altura = nvaltura

    def mostrar (self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso} kg \nAltura: {self.altura} m")