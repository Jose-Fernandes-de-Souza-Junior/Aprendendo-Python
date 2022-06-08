idade = int(input("Digite sua idade: "))

if idade>=18: #caso verdadeiro
    print ("Maior de idade")
else: #caso falso
    print("Menor de idade")




idade = int(input("Digite sua idade: "))

if idade>=16: #caso verdadeiro
    print ("pode votar")
else:
    if idade>=16:#caso falso
        print("Pode dirigir")

    else:
        if idade<16:
            print("Apenas estude")



idade = int(input("Digite sua idade: "))

if idade>=16 and idade<18: #caso verdadeiro
    print ("pode votar")
    
elif idade<16:
        print("Apenas estude")

else:
    print("Pode dirigir")
