# -- 7 – Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto,
# --  o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte 
# --  a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de 
# --  dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa 
# --  também deve ser informados os códigos e valores do cliente mais alto, do mais baixo, do mais 
# -- gordo e do mais magro, além da média das alturas e dos pesos dos clientes

maior_alt=0
codalt=0
pesoalt=0
menoralt=1000
menorpeso=1000
codmenor=1000
cont = 0
soma = 0
media=0
somap=0
while True:

	print("Digite os dados do cliente:")
	cod = float(input("Digite o codigo: "))
	if cod==0:		
		break
	alt = float(input("Digite a altura: "))
	peso = float(input("Digite o peso: "))
	somap = somap +peso
	soma = soma + alt
	cont = cont + 1

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

	
media = soma /cont
print("A media de altura é: ",media)
media = somap /cont
print("A media de peso é: ",media)
