8# – Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
#Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
# Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
aumento = 0.015
sal = 1000
sal_atual = sal + aumento
ano = 1996
for ano in range(1996,2023):

	print(ano,"Salario: R$ ",sal_atual)
	ano = ano + 1
	sal_atual = sal_atual+aumento*2
