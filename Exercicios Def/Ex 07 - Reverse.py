'''7 - Reverso do número. Faça uma função que retorne o reverso de um
número inteiro informado. Por exemplo: 127 -> 721.'''

def reverse(valor):
   
   novovalor = valor[::-1]
   print(novovalor)
   return (novovalor)

valor = input("informe o valor a ser invertido: ")
reverse(valor)

  
