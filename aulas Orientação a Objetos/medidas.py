class Forma:
    def __init__(self,area,perimetro):
        self.area= area
        self.perimetro = perimetro

class Retangulo(Forma):
    def __init__(self, area, perimetro):
        super().__init__(area, perimetro)

    def calculaArea (self,base,lado):
        self.area = (base*lado)
        print(f"Area Retangulo: {self.area}")

    def calculaPerimetro(self,base,lado):
        self.perimetro = 2*(base+lado)
        print(f"Perimetro Retangulo: {self.perimetro}")
class Triangulo (Forma):
    def __init__(self, area, perimetro,altura):
        super().__init__(area, perimetro)
        self.altura = altura

    def calculaArea (self,base,altura):
        self.area = (base*altura)/2
        print(f"Area Triangulo: {self.area}")

    def calculaPerimetro(self,base,altura):
        self.perimetro = base+base+altura
        print(f"Perimetro Triangulo: {self.perimetro}")

retang = Retangulo(20,30)
retang.calculaArea(10,5)
retang.calculaPerimetro(20,10)
print (isinstance(retang,Retangulo))

triang = Triangulo(10,10,10)
triang.calculaArea(10,5)
triang.calculaPerimetro(5,10)
print(isinstance(triang,Triangulo))
