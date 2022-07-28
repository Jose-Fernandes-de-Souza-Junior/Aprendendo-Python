# Faça um programa, com uma função que necessite de um argumento. 
# A função retorna o valor do caractere 'P', se seu argumento for positivo, e 'N' se seu argumento for negativo ou zero

def num (valor):
    
    if valor>0:
        print("O argumento é : Posititvo")

    elif valor==0:
        print("Numero zero")

    else:
        print("O argumento é: Negativo")

num(25)