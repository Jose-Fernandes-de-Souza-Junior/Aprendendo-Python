from dadosaluno import dadosaluno

aluno1 = dadosaluno ("Nathan",4545,"Achologia")

aluno1.mostrar()

nome = input("Digite o nome do aluno: ")
matricula = int(input("digite a matricula: "))
curso = input("Digite o nome do curso: ")

aluno1.alterar(nome,matricula,curso)

aluno1.mostrar()