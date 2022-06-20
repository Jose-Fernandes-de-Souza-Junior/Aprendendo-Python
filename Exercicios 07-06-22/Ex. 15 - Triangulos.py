'''15 - Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
 '''
L1 = float(input("Informe o primeiro lado do triangulo: "))
L2 = float(input("Informe o segundo lado do triangulo: "))
L3 = float(input("Informe o terceiro lado do triangulo: "))

if L1==L2 and L1==L3:
    print("Triangulo Equilatero")

elif L1==L2 and L2!=L3:
    print("Triangulo Isóceles")

elif L1!=L2 and L2==L3:
    print("Triangulo Isóceles")

elif L1!=L2 and L1==L3:
    print("Triangulo Isóceles")

elif L1!=L2 and L2!=L3:
    print("Triangulo Escaleno")
