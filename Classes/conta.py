from socket import NI_NUMERICHOST


class conta: 
    def __init__(self, numero,cpf,nomeTitular,saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar (self,valor):
        self.saldo+=valor
        
    def sacar (self,valor):
        self.saldo-=valor

    def extrato(self):
        print(f"numero = {self.numero} \n CPF: {self.cpf}\n Nome: {self.nomeTitular} \n Saldo: {self.saldo} ")
