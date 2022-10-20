class Funcionario(object):
    def __init__(self,nome,salario):
        self.nome = nome

        self.__salario = salario

    def __calculaSalarioMensal(self):
        print("\nSalario mensal Piso: "+str(self.__salario))

    
    def __calculaSalarioAnual(self):
        print("Salario anual Piso: "+str(self.__salario*12))   

    def retornaSalarios(self):
        self.__calculaSalarioMensal()
        self.__calculaSalarioAnual()
    

class Engenheiro (Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
    
        self.__salario = salario

    def __calculaSalarioMensal(self):
        self.__salario += self.__salario*0.2
        print("\nSalario mensal Engenheiro: "+str(self.__salario))

    
    def __calculaSalarioAnual(self):
        self.__salario += (self.__salario+(self.__salario*0.2))*12
        print("Salario anual Engenheiro: "+str(self.__salario))

    def retornaSalarios(self):
        self.__calculaSalarioMensal()
        self.__calculaSalarioAnual()


class Desenvolvedor (Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

        self.__salario = salario

    def __calculaSalarioMensal(self):
        self.__salario += self.__salario*0.3
        print("\nSalario mensal Desenvolvedor: "+str(self.__salario))

    
    def __calculaSalarioAnual(self):
        self.__salario += (self.__salario+(self.__salario*0.3))*12
        print("Salario anual Desenvolvedor: "+str(self.__salario))

    def retornaSalarios(self):
        self.__calculaSalarioMensal()
        self.__calculaSalarioAnual()

class Analista (Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

        self.__salario = salario

    def __calculaSalarioMensal(self):
        self.__salario += self.__salario*0.25
        print("\nSalario mensal Analista: "+str(self.__salario))

    def __calculaSalarioAnual(self):
        self.__salario += (self.__salario+(self.__salario*0.25))*12
        print("Salario anual Analista: "+str(self.__salario))

    def retornaSalarios(self):
        self.__calculaSalarioMensal()
        self.__calculaSalarioAnual()

salario = float(input("Digite o valor do piso salarial: R$ "))

func = Funcionario ("José",salario)
func.retornaSalarios()

eng = Engenheiro("Alberto",salario)
eng.retornaSalarios()


dev = Desenvolvedor("Carlos",salario)
dev.retornaSalarios()


analista = Analista("Maria",salario)
analista.retornaSalarios()





    

    