#Exercicio 08
P1 = float(input("Digite o preço do primeiro produto: "))
P2 = float(input("Digite o preço do segundo produto: "))
P3 = float(input("Digite o preço do terceiro produto: "))


if P1<P2 and P2<P3:
    print ("Você deve comprar o primeiro produto!!!")

elif P2<P1 and P1<P3:
    print ("Você deve comprar o segundo produto!!!")

else:
    print ("Você deve comprar o terceiro produto!!!")
