class conta_corrente:

    def __init__(self,numero,nome,saldo):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
       

    def alterarNome(self,nvnumero,nvnome,nvsaldo):
        self.numero = nvnumero
        self.nome = nvnome
        self.saldo = nvsaldo

    def deposito(self,dep):
        self.saldo+=dep
    
    def saque(self,sq):
        self.saldo-=sq


    def mostrarSaldo(self):
        print(f"______RELATORIO______\nConta Corrente: {self.numero}\nNome do correntista: {self.nome}\n")
        
        print(f"Saldo: R$ {self.saldo}")

    