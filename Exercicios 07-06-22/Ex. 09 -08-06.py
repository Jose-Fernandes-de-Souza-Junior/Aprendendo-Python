#Exercicio 9

Num1 = int(input("Digite primeiro numero: "))
Num2 = int(input("Digite o segundo numero: "))
Num3 = int(input("Digite o terceiro numero: "))


if Num1>Num2 and Num2>Num3:
    print("A ordem decrescente é: ",Num1,Num2,Num3)
  


elif Num2>Num1 and Num1>Num3:
    print("A ordem decrescente é: ",Num2,Num1,Num3)


elif Num3>Num1 and Num1>Num2:
    print("A ordem decrescente é: ",Num3,Num1,Num2)

elif Num2>Num3 and Num3>Num1:
    print("A ordem decrescente é: ",Num2,Num3,Num1)
