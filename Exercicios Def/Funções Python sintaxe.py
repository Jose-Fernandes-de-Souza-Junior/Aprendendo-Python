
'''def hello():
    print ("olá")
hello()

def fahr_to_celsius(temp):
    return ((temp - 32)*(5/9))

print(round(fahr_to_celsius(100),2))'''

def maior_30(*args):
    print(args)
    for num in args:
        if num>30:
            print(num)
        
maior_30 (10,20,30,40,50,60)


'''def hello(nome,idade):
    print("olá ",nome,"\nSua idade é: ",idade)
hello("José",29)

def calcular_pagamento(qtd_h,valor_h):
    horas = float (qtd_h)
    taxa = float(valor_h)
    if horas<=40:
        salario=horas*taxa
        print(salario)
    else:
        hexcd = horas-40
        salario = 40*taxa+(hexcd*(1.5*taxa))
        print(salario)
calcular_pagamento(55,8)'''
