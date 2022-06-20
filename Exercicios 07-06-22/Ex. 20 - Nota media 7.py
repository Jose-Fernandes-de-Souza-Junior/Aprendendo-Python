#Exercicio 20
'''20 - Faça um Programa para leitura de três notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''


n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1+n2+n3)/3

if media>=7 and media<10:
    print("A primeira nota foi: ",n1,
          "\n A segunda nota foi: ",n2,
          "\n A segunda nota foi: ",n3,
          "\n A media foi: ",media,
          "\n Aluno APROVADO!!!")

elif media==10:
    print("A primeira nota foi: ",n1,
          "\n A segunda nota foi: ",n2,
          "\n A segunda nota foi: ",n3,
          "\n A media foi: ",media,
          "\n Aluno APROVADO COM DISTINÇÃO!!!")


else:
    print("A primeira nota foi: ",n1,
          "\n A segunda nota foi: ",n2,
          "\n A segunda nota foi: ",n3,
          "\n A media foi: ",media,
          "\n Aluno REPROVADO!!!")

