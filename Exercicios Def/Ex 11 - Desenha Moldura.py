'''11 - Desenha moldura. Construa uma função que desenhe um retângulo
usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois
parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo
igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles
devem ser modificados para valores dentro da faixa de forma elegante.'''

def moldura(linha,coluna,caract):
    x = "__{caract}__"

    for i in range(0,linha):
        print(linha*x)

        print(coluna.x)

linha = int(input("Digite o numero de linhas: "))
coluna = int(input("Digite o numero de colunas: "))
caract = input("")





