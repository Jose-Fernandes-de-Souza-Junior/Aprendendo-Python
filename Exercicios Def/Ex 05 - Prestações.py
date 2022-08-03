import os
import time

'''5 - Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação 
de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e 
passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao 
programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa 
deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero
para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a 
quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma.
Para pagamentos sem atraso, cobrar o valor da prestação. 

Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
'''
listaPrest = []
atraso = []
def valorPagamento (prest,dias):
    try:
        while True:
            prest= float(input("Digite o valor da prestação: R$ "))
            if prest==0:
                print("Programa encerrado!\n")
                time.sleep(3)
                os.system("cls")
                print("______Relatorio do dia______\n",
                "Prestações: R$ ",(sum(listaPrest)), "\n Dias de atraso: ",(sum(atraso)))
                break 
            
            elif prest!=0:
                dias = int(input("Digite os dias em atraso: "))    
                if dias==0:
                        print("O valor da prestação é: R$ ",prest)

                elif dias>0:
                        atraso.append(dias)
                        multa = prest*0.03
                        juros = (prest*0.01)*dias
                        prest = prest+multa+juros
                        
                        print("O valor da prestação é: R$ ",prest)
                        listaPrest.append(prest)

            
    except ValueError: 
        print("Valor invalido tente novamente!")


prest = listaPrest
dias = atraso
os.system("cls")

valorPagamento(prest,dias)


