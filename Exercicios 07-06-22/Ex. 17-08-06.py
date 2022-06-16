#Exercicio 17
'''17 - Faça um Programa que peça um número correspondente a um determinado
ano e em seguida informe se este ano é ou não bissexto.'''


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
