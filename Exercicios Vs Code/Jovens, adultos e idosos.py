#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade 
# da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
from socket import IPPROTO_DSTOPTS

somaj = 0
jovens = 0
adultos = 0
idoso = 0
cont=0
while True:



	idade = int(input("Digite sua idade: "))

	for idade in range (0,100):
	
		if idade ==0:
			break

		elif idade>0 and idade<=25:
			jovens = jovens + 1
			
		elif idade>=26 and idade<=60:
			adultos = adultos + 1

		elif idade>60:
			idoso = idoso + 1
			
		

print ("A soma de Jovens: ",jovens, "\n A media de idade dos jovens é: ",somaj)
print("A soma de Adultos: ",adultos)
print("A soma de Idosos: ",idoso)








