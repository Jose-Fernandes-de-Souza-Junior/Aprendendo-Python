class Calculadora (object):
    def __init__(self,num1,num2,operacao):
        self.num1 = num1
        self.num2 = num2
        self.operacao = operacao
        

    def __somar(self):
        self.result = self.num1+self.num2
        print(f"Somando: {self.num1} + {self.num2} = {self.result} ")

    def __subtrair(self):
        self.result = self.num1-self.num2
        print(f"Subtraindo: {self.num1} - {self.num2} = {self.result} ")

    def __multiplicar(self):
        self.result = self.num1*self.num2
        print(f"Multiplicando: {self.num1} x {self.num2} = {self.result} ")

    def __dividir(self):
        self.result = self.num1/self.num2
        print(f"Dividindo: {self.num1} / {self.num2} = {self.result} ")
        

    

    def calcular(self):

        
        self.operacao = operacao

        if self.operacao==1:
            self.operacao = self.__somar()

        elif self.operacao==2:
            self.operacao=self.__subtrair()
        
        elif self.operacao==3:
            self.operacao=self.__multiplicar()

        elif self.operacao==4:
            self.operacao=self.__dividir()

        else:
            print("Operação invalida!")


num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o primeiro numero: "))
print("Escolha a operação a ser realizada: \n[ 1 ] Soma \n[ 2 ] Subtrair \n[ 3 ] Multiplicar \n[ 4 ] Dividir")
operacao = int(input("Operação: "))

calc = Calculadora(num1,num2,operacao)
calc.calcular()