print("_________MENU PRINCIPAL_________",

"\n 1 - Usuario", 
"\n 2 - Estoque",
"\n 3 - Colaboradores",
"\n 4 - Fornecedores",
"\n 5 - Cuidador",
"\n 6 - Cursos",
"\n 7 - Sair")

codigo = int(input("Digite a opção desejada: "))

if codigo ==1:
	print("_______Usuario_______")
nome = input("Insira o Nome: ")
endereço = input("Insira o Endereço: ")
telefone = input("Insira o telefone: ") 
email = input("Insira o E-mail: ")
sexo = input("Insira o sexo: ")
data_nasc = input("Data de nascimento: ")
renda = float(input("Renda: "))
doenca = input("Doença: ")
codNIS = int(input("NIS: "))
