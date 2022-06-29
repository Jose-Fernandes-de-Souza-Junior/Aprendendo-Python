

maior_alt=0
codalt=0
pesoalt=0
menoralt=1000
menorpeso=1000
codmenor=1000
cont = 1
soma = 0
while True:

	print("Digite os dados do cliente:")
	cod = float(input("Digite o codigo: "))
	if cod==0:
		soma = soma + maior_alt
		media = round (soma/(cont+1),cont)
		print("A media de altura é: ",media)
		break
	alt = float(input("Digite a altura: "))
	peso = float(input("Digite o peso: "))
	
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

		







