class retangulo:
    def __init__(self,ladoA,ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudarValor(self,ladoL,ladoC): #ladoL = largura / ladoC = comprimento
        self.ladoA = ladoL
        self.ladoB = ladoC

    def retornarValor(self):
        print(f"A altura do retangulo é: {self.ladoA} cm \n A base do retangulo é: {self.ladoB} cm \n A area é: {self.area} cm²\n O perimetro é: {self.per} cm")

    def calc_Area (self):
        self.area = self.ladoA*self.ladoB

    def calc_Perimetro(self):
        self.per = 2*(self.ladoA+self.ladoB)
