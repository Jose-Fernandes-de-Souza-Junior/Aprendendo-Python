class Funcionario(object):
    def __init__(self,nome,salario):
        self.nome = nome
        self.__salario = salario

    def __getCalculaSalario(self):
        s = self.__salario
        print(s)

    def retornaSalario(self):

        self.__getCalculaSalario()

        if self.__salario>=500:
            
            print ("Você é rico")

        else:
            print("Você é pobre")


func = Funcionario("Jose",400)
print(func.nome)
func.retornaSalario()