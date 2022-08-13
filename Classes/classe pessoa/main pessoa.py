import os
import time

from people import people
print("____ANTES___")

pessoa1 = people ("Jose",29,63.5,1.67)

pessoa1.mostrar()

print("___DEPOIS___")

pessoa1.engordar()

pessoa1.emagrecer()

pessoa1.mostrar()

time.sleep(10)
os.system("cls")

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

pessoa1.alterar(nome,idade,peso,altura)

pessoa1.engordar()

pessoa1.emagrecer()

pessoa1.mostrar()








