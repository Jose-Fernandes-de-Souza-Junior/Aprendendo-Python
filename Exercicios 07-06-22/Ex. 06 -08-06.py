#Exercicio 6

Num1 = int(input("Digite primeiro numero: "))
Num2 = int(input("Digite o segundo numero: "))
Num3 = int(input("Digite o terceiro numero: "))



if Num1>Num2 and Num2>Num3:
    print ("O numero maior é: ",Num1)

elif Num2>Num1 and Num2>Num3:
    print ("O numero maior é: ",Num2)

else:
    print ("O numero maior é: ",Num3)
