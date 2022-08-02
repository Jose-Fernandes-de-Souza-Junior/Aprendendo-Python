'''5 - Faça um programa que use a função valorPagamento para determinar o
valor a ser pago por uma prestação de uma conta. O programa deverá solicitar
ao usuário o valor da prestação e o número de dias em atraso e passar estes
valores para a função valorPagamento, que calculará o valor a ser pago e
devolverá este valor ao programa que a chamou. O programa deverá então
exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a
pedir outro valor de prestação e assim continuar até que seja informado um
valor igual a zero para a prestação. Neste momento o programa deverá ser
encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total
de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte
forma. 

Para pagamentos sem atraso, cobrar o valor da prestação. Quando
houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.'''
lista = []
def valorPagamento (prestação,dias):
    while True:
        
        if dias>0:
        
            juros = (prestação*0.001)*dias
            multa = prestação*0.03
            prestação+=multa+juros
            print("O valor a ser pago será de: R$ ",prestação)
            break
        elif dias ==0:
            print("O valor a ser pago será de: R$ ",prestação)
            break

valor =float(1) 
total =float(0)
prest =float(0)
while valor!=0:
    valor = float(input("Digite o valor da prestação: "))
    dias = int(input("Digite os dias de atraso: "))
    total+=valorPagamento(valor,dias)
    

print("_______Relatorio do Dia________\n","Prestações: R$ ",(total))

    
    
    
    





