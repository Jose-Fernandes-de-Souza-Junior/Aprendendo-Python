import os

while True:
	print("_________MENU PRINCIPAL_________",

    "\n 1 - Usuario", 
    "\n 2 - Cuidador",
    "\n 3 - Colaboradores",
    "\n 4 - Fornecedores",
    "\n 5 - Estoque",
    "\n 6 - Cursos",
    "\n 7 - Sair")

	
	codigo = int(input("Digite a opção desejada: "))
	os.system("cls")
	
	

	if codigo==1:
		while True:
			print ("1 - Incluir\n 2 - Excluir\n 3 - Relatorio\n 4 - Voltar\n ")
			opcao = int(input("Digite a opção: "))
			os.system("cls")

			if opcao==4:
				break

			elif opcao==1:	
				print("_______Usuario_______")
				nome = input("Insira o Nome: ")
				endereco = input("Insira o Endereço: ")
				telefone = input("Insira o telefone: ")
				email = input("Insira o E-mail: ")
				sexo = input("Insira o sexo: ")
				data_nasc = input("Data de nascimento: ")
				renda = float(input("Renda: "))
				doenca = input("Doença: ")
				codNIS = int(input("NIS: "))

			elif opcao==2:
				print("Excluir")

			elif opcao==3:
				print("Relatorio: \n", nome, "\n",endereco, "\n",telefone,"\n",email,"\n",sexo,"\n",data_nasc,"\n",renda,"\n",doenca,"\n",codNIS)

	elif codigo==2:
		while True:

			print ("1 - Incluir\n 2 - Excluir\n 3 - Relatorio\n 4 - Voltar\n ")
			opcao = int(input("Digite a opção: "))
			os.system("cls")
			
			if opcao==4:
				break
				
			elif opcao==1:
				print("_______Cuidador_______")
			nome = input("Insira o Nome: ")
			endereco = input("Insira o Endereço: ")
			telefone = input("Insira o telefone: ")
			email = input("Insira o E-mail: ")
			sexo = input("Insira o sexo: ")
			data_nasc = input("Data de nascimento: ")
			renda = float(input("Renda: "))
			
			if opcao==2:
				print("Excluir")

			elif opcao==3:
				print("Relatorio: \n", nome, "\n",endereco, "\n",telefone,"\n",email,"\n",sexo,"\n",data_nasc,"\n",renda)
				

	elif codigo==3:
		while True:
			print ("1 - Incluir\n 2 - Excluir\n 3 - Relatorio\n 4 - Voltar\n ")
			opcao = int(input("Digite a opção: "))
			os.system("cls")
			if opcao==4:
				break
			
			elif opcao==1:
				print("_______Colaborador_______")
			nome = input("Insira o Nome: ")
			endereco = input("Insira o Endereço: ")
			telefone = input("Insira o telefone: ")
			email = input("Insira o E-mail: ")
			sexo = input("Insira o sexo: ")
			data_nasc = input("Data de nascimento: ")

			if opcao==2:
				print("Excluir")

			elif opcao==3:
				print("Relatorio: \n", nome, "\n",endereco, "\n",telefone,"\n",email,"\n",sexo,"\n",data_nasc)

	elif codigo==4:
		while True:
			print ("1 - Incluir\n 2 - Excluir\n 3 - Relatorio\n 4 - Voltar\n ")
			opcao = int(input("Digite a opção: "))
			os.system("cls")
			if opcao==4:
				break
					
			elif opcao==1:
				print("_______Fornecedor_______")
			razao = input("Insira o Nome: ")
			cnpj= input("Digite o CNPJ: ")
			endereco = input("Insira o Endereço: ")
			telefone = input("Insira o telefone: ")
			email = input("Insira o E-mail: ")

			if opcao==2:
				print("Excluir")

			elif opcao==3:
				print("Relatorio: \n", razao, "\n",cnpj,"\n", endereco, "\n",telefone,"\n",email)
	
	
	elif codigo==5:
		while True:
			print ("1 - Incluir\n 2 - Excluir\n 3 - Relatorio\n 4 - Voltar\n ")
			opcao = int(input("Digite a opção: "))
			os.system("cls")
			if opcao==4:
				break
					
			elif opcao==1:
				print("_______Estoque_______")
			cod = input("Insira o codigo do Produto: ")
			desc= input("Insira a descrição do Produto: ")
			valor = input("Insira o valor: ")
			quant = input("Insira a quantidade: ")
			cat = input("Insira a categoria: ")
			obs= input("Insira as observações: ")

			if opcao==2:
				print("Excluir")

			elif opcao==3:
				print("Relatorio: \n", cod, "\n",desc,"\n", valor, "\n",quant,"\n",cat,"\n",obs)
	elif codigo==6:
		while True:

			print ("1 - Incluir\n 2 - Excluir\n 3 - Relatorio\n 4 - Voltar\n ")
			opcao = int(input("Digite a opção: "))
			os.system("cls")
			if opcao==4:
				break
					
			elif opcao==1:
				print("_______Cursos_______")
			nome = input("Insira o nome do curso: ")
			datai= input("Insira a data de inicio: ")
			datac = input("Insira a data de conclusão: ")
			partic = input("Insira o nome do participante: ")
			

			if opcao==2:
				print("Excluir")

			elif opcao==3:
				print("Relatorio: \n", nome, "\n",datai,"\n", datac, "\n",partic)

		
	elif codigo==7:
		break

	else:
		print("opção invalida")	


	
	
