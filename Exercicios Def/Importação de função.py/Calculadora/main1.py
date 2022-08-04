import os
from soma import soma
from subt import subt
from mult import mult
from div import div

print("_____Calculadora______")

print("Escolha o tipo de operação: ")
escolha = (input("[1] Adição\n [2] Subtração\n [3] Multiplicação\n [4] Divisão\n [5] Sair\n Opção: "))

os.system("cls")

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
while True:
    
    if escolha=='5':
        print("Sair!")
        os.system("cls")
        os.system("pause")
        break
    
    elif escolha=='1':
        print ("A soma dos numeros: {} + {} = ".format(num1,num2),soma(num1,num2))
        os.system("cls")
        os.system("pause")
    elif escolha=='2':
        print ("A subtração dos numeros: {} - {} = ".format(num1,num2),subt(num1,num2))
        os.system("cls")
        os.system("pause")
    elif escolha=='3':
        print ("A multiplicação dos numeros: {} x {} = ".format(num1,num2),mult(num1,num2))
        os.system("cls")
        os.system("pause")
    elif escolha=='4':
        print ("A divisão dos numeros: {} / {} = ".format(num1,num2),div(num1,num2))
        os.system("cls")
        os.system("pause")
    

    else: 
        print("Opção invalida. Tente novamente!")
        

    
   
