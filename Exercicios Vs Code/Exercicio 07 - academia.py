media=0
maior_alt=0
codalt=0
pesoalt=0
menoralt=1000
menorpeso=1000
codmenor=1000
cont = 0
soma = 0
while True:

	print("Digite os dados do cliente:")
	cod = float(input("Digite o codigo: "))
	if cod==0:
		break
	alt = float(input("Digite a altura: "))
	peso = float(input("Digite o peso: "))


	cont = cont+1
	soma = soma + alt

	
	if alt>maior_alt:
		maior_alt=alt
		codalt=cod
		pesoalt=peso

	elif alt<menoralt:
		menoralt=alt
		codmenor=cod
		menorpeso=peso

	elif peso>pesoalt:
		menoralt=alt
		codmenor=cod
		menorpeso=peso

	elif peso<pesoalt:
		menoralt=alt
		codmenor=cod
		menorpeso=peso

media =soma/cont
print("A media de altura é: ",media)		







