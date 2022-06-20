'''14 - Faça um programa que leia as duas notas parciais obtidas por um
aluno numa disciplina ao longo de um semestre, e calcule a sua média.
A atribuição de conceitos obedece à tabela abaixo: 
Média de Aproveitamento Conceito 
Entre 9.0 e 10.0 A 
Entre 7.5 e 9.0 B 
Entre 6.0 e 7.5 C 
Entre 4.0 e 6.0 D 
Entre 4.0 e zero E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente
e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.'''


n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1+n2)/2

if media>9 and media<=10:
    print("A primeira nota foi: ",n1,
          "\n A segunda nota foi: ",n2,
          "\n A media foi: ",media,
          "\n Aluno nota 'A'",
          "\n Aluno APROVADO!!!")

elif media>7.5 and media<=9:
    print("A primeira nota foi: ",n1,
          "\n A segunda nota foi: ",n2,
          "\n A media foi: ",media,
          "\n Aluno nota 'B'",
          "\n Aluno APROVADO!!!")

elif media>6 and media<=7.5:
    print("A primeira nota foi: ",n1,
          "\n A segunda nota foi: ",n2,
          "\n A media foi: ",media,
          "\n Aluno nota 'C'",
          "\n Aluno APROVADO!!!")

elif media>4 and media<=6:
    print("A primeira nota foi: ",n1,
          "\n A segunda nota foi: ",n2,
          "\n A media foi: ",media,
          "\n Aluno nota 'D'",
          "\n Aluno REPROVADO!!!")

else:
    print("A primeira nota foi: ",n1,
          "\n A segunda nota foi: ",n2,
          "\n A media foi: ",media,
          "\n Aluno nota 'E'",
          "\n Aluno REPROVADO!!!")
