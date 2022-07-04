from http.client import OK

while True:
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

    print ("1 - Salvar   2 - Excluir   3 - Sair   4 - Voltar")

    opcao = int(input("Digite a opção: "))

    if opcao==1:
        print("Cadastro de Usuario salvo com sucesso!")

    elif opcao==2:
        print("Deseja exluir o cadastro?")
        confirmacao = int(input("1 - Sim    2 - Não"))
        if confirmacao==1:
            del codigo
        elif confirmacao==2:
            continue
    
    while opcao==3:
        print("Deseja sair?")
    confirmacao = int(input("1 - Sim    2 - Não"))
    if confirmacao==1:
        break
    elif confirmacao==2:
        continue
    else:
        print("Opção invalida! Digite os números 1 ou 2!")