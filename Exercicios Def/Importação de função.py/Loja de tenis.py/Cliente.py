class Cliente:

    def __init__(self,nome:str,idade:int,endereco:str,fone:str,sexo:str):
        self.nome = input("Digite o nome do cliente: ",nome)
        self.idade = input("Digite a idade: ",idade)
        self.endereco = input("Digite o endereço: ", endereco)
        self.fone = input("Digite o telefone: ",fone)
        self.sexo = input("Digite o sexo: ",sexo)

    print(f'Nome: {self.nome},idade: {idade},endereço:{self.endereco},telefone:{self.fone},sexo:{self.sexo}')
        
  



