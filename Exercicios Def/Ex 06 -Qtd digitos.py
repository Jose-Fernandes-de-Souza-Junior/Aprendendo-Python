'''6 - Faça uma função que informe a quantidade de dígitos de um determinado
número inteiro informado.'''
import math
num=0
digito = 0
def digi(num):
    num = int(input("Digite um numero: "))
    
    if num==0:
        print("O numero digitado tem ",num,"Dígitos")

digi(num)