# Faça um programa com uma função chamada somaImposto. A função possui dois parametros formais: taxaimposto, que é a quantia 
#de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função "altera" o valor para o imposto sobre vendas.

def somaImposto (taxaImposto,custo):

    
    lucro = custo+custo*0.03
    vl_venda = taxaImposto+lucro
    
    print("O valor de venda é: ",vl_venda)

somaImposto(0.17,50)