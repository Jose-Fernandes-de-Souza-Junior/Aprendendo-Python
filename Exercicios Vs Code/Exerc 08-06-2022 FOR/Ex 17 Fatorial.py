#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

num = int(input("Digite um numero inteiro a ser fatorado: "))
total = 0
for num in range (num,0,-1):
    while num>=0:
        total=num*num
        print(num,".",end='')
        break
print(" = ",num)
