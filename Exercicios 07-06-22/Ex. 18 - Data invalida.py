'''18 - Faça um Programa que peça uma data no formato dd/mm/aaaa
e determine se a mesma é uma data válida. '''

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano (quatro algarismos): "))
          
if dia>=1 and dia <=31:
print("Data: ",dia,"/",mes,"/",ano)
else:
        print("Data inválida")
    
if mes>=1 and dia <=12:

    print("Data: ",dia,"/",mes,"/",ano)
else:
        print("Data inválida")

if ano<=1:
    print("Data: ",dia,"/",mes,"/",ano)

else:
        print("Data inválida")


