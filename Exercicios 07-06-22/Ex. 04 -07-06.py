#Exercicio 04

letra = input("Digite uma letra: ")

if letra.isalpha():
    if letra=="A" or letra=="a":
        print ("Vogal")
    
    elif letra=="E" or letra=="e":
        print("vogal")

    elif letra=="I" or letra=="i":
        print("vogal")

    elif letra=="O" or letra=="o":
        print("vogal")

    elif letra=="U" or letra=="u":
        print("vogal")
    else:
        print ("Consoante")

else:
    print ("Não é letra")
