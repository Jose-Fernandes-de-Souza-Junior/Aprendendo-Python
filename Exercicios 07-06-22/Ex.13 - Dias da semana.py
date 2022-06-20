'''13 - Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''

#13 - Faça um Programa que leia um número e exiba o dia correspondente da semana.
#(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.


dias = int(input("Digite um numero entre 1 e 7 para escolher o dia da semana: "))


if dias == 1:
    print("O dia da semanda é Domingo")

elif dias == 2:
    print("O dia da semanda é Segunda")

elif dias == 3:
    print("O dia da semanda é Terça")

elif dias == 4:
    print("O dia da semanda é Quarta")

elif dias == 5:
    print("O dia da semanda é Quinta")

elif dias == 6:
    print("O dia da semanda é Sexta")

elif dias == 7:
    print("O dia da semanda é Sabado")

else:
    print("Valor invalido!")

