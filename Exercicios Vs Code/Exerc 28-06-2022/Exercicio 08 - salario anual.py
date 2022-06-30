#8 – Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
# Faça um programa que determine o salário atual desse funcionário. 
# Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

sal=1000
aumento = 0.015
ano = 1996
cont = 0
sal_atual=sal+sal*aumento

for ano in range(1996,2023):
	
	print(ano,": ","Salario: R$ ",sal_atual)
	
	sal_atual = sal_atual+sal_atual*(aumento*2)