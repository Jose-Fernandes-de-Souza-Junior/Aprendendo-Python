class Funcionario(object):
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario

    def calculaSalarioMensal(self):
        print("\nSalario mensal Piso: "+str(self.salario))

    def calculaSalarioAnual(self):
        print("Salario anual Piso: "+str(self.salario*12))

class Engenheiro (Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
    
    def calculaSalarioMensal(self):
        self.salario += self.salario*0.2
        print("\nSalario mensal Engenheiro: "+str(self.salario))

    def calculaSalarioAnual(self):
        self.salario += (self.salario+(self.salario*0.2))*12
        print("Salario anual Engenheiro: "+str(self.salario))

class Desenvolvedor (Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calculaSalarioMensal(self):
        self.salario += self.salario*0.3
        print("\nSalario mensal Desenvolvedor: "+str(self.salario))

    def calculaSalarioAnual(self):
        self.salario += (self.salario+(self.salario*0.3))*12
        print("Salario anual Desenvolvedor: "+str(self.salario))

class Analista (Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calculaSalarioMensal(self):
        self.salario += self.salario*0.25
        print("\nSalario mensal Analista: "+str(self.salario))

    def calculaSalarioAnual(self):
        self.salario += (self.salario+(self.salario*0.25))*12
        print("Salario anual Analista: "+str(self.salario))


salario = float(input("Digite o valor do piso salarial: R$ "))

func = Funcionario ("José",salario)
func.calculaSalarioMensal()
func.calculaSalarioAnual()

eng = Engenheiro("Alberto",salario)
eng.calculaSalarioMensal()
eng.calculaSalarioAnual()

dev = Desenvolvedor("Carlos",salario)
dev.calculaSalarioMensal()
dev.calculaSalarioAnual()

analista = Analista("Maria",salario)
analista.calculaSalarioMensal()
analista.calculaSalarioAnual()




    

    