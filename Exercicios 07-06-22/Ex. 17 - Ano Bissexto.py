#Exercicio 17
'''18 - Faça um Programa que peça uma
data no formato dd/mm/aaaa e determine se a mesma é uma data válida.'''


dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

etapa1 = ano%4
etapa2 = ano%100
etapa3 = ano%400

if etapa1==0:
    print("O ano ",ano, " é bissexto!")
    
elif etapa2==0:
    print("O ano ",ano, " é bissexto!")
        
elif etapa3==0:
    print("O ano ",ano, " é bissexto!")

else:
    print("O ano ",ano, " não é bissexto!!!")
