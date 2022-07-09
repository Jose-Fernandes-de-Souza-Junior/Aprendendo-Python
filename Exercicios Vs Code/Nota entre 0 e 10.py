#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
while True:
	nota = int(input("Insira uma nota: "))

	for nota in range (nota,11):
	
		if nota>=0 and nota<=10:
		
			print ("A nota é: ",nota)
		
		else:
			print("Nota invalida digite outra!")
			
	