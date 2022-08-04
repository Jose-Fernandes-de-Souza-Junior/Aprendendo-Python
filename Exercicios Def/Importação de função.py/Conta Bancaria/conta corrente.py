import os
import time
from entrada import entrada
from saida import saida

credito = []
debito = []

print ("Bem vindo ao Banco DigiBank! \n Escolha a operação que deseja realizar\n")
escolha = input("[1] Deposito\n [2] Transferencia\n [3] Extrato\n [4] Sair\n Opção: ")
try:
    while True:
        

        if escolha=='1':
            valor = float(input("Digite o valor que deseja depositar R$: "))
            entrada(valor)
            credito.append(valor)
        elif escolha=='2':
            valor = float(input("Digite o valor que deseja transferir R$: "))
            saida(valor)
            debito.append(valor)
        elif escolha=='3':

            if credito>0:
                saldo = credito-debito
                os.system("cls")
                time.sleep(3)
                print("_____Extrato______\n")
                print("Entradas: \n R$ ",credito,
                "\n Saídas R$ ",debito,
                "\n Saldo R$ ",saldo)
                
                break
            
except ValueError:
    print("Operação invalida! Tente novamente!")
