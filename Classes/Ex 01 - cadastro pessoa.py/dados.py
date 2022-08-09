class dados:
    def __init__(self,nome,idade,endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco


    def mostrar(self):
        print(f"Nome: {self.nome} \n Idade: {self.idade} \n Endereço: {self.endereco}")

    def alterar(self,novonome,novaidade,novoendereco):
        self.nome = novonome
        self.idade = novaidade
        self.endereco = novoendereco

    






