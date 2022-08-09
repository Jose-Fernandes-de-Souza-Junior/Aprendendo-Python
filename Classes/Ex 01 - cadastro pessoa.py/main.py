from dados import dados

pessoa1 = dados ("Jose",29," rua do Cruzeiro")

pessoa1.mostrar()

nome = input("Digite o nome: ")
idade = input("Digite o idade: ")
endereco = input("Digite o endereço: ")

pessoa1.alterar (nome,idade,endereco)

pessoa1.mostrar()



