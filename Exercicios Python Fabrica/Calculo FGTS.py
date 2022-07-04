#Exercicio 12
'''12 - Faça um programa para o cálculo de uma folha de
pagamento, sabendo que os descontos são do Imposto de
Renda, que depende do salário bruto (conforme tabela abaixo) e
3% para o Sindicato e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que
deposita).
O Salário Líquido corresponde ao Salário Bruto
menos os descontos. O programa deverá pedir ao usuário o
valor da sua hora e a quantidade de horas trabalhadas no
mês.Desconto do IR:
• Salário Bruto até 900 (inclusive) - isento
• Salário Bruto até 1500 (inclusive) - desconto de 5%
• Salário Bruto até 2500 (inclusive) - desconto de 10%
• Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo
abaixo. No exemplo o valor da hora é 5 e a quantidade de hora
é 220.'''

hora = float(input("Digite a quantidade de horas trabalhadas: "))
vl_hora = float(input("Digite o valor da hora trabalhada: "))



salario = vl_hora*hora
sindicato = salario*0.03
FGTS = salario*0.11


if salario<=900:
    IR = salario*0
    INSS = salario*0.1
    desconto = IR+INSS
    print("Salario Bruto: (",vl_hora,"*",hora,")     : R$ ",salario,
          "\n  (-) IR (5%)                      : R$ ",IR,
          "\n  (-) INSS (10%)                   : R$ ",INSS,
          "\n  (-) Sindicato (3%)               : R$ ",sindicato,
          "\n FGTS (11%)                        : R$ ",FGTS,
          "\n Total de descontos                : R$ ",desconto,
          "\n Salario Liquido                   : R$ ",salario-desconto)

elif salario>900 and salario<=1500:
    IR = salario*0.05
    INSS = salario*0.1
    desconto = IR+INSS
    print("Salario Bruto: (",vl_hora,"*",hora,")     : R$ ",salario,
          "\n  (-) IR (5%)                      : R$ ",IR,
          "\n  (-) INSS (10%)                   : R$ ",INSS,
          "\n  (-) Sindicato (3%)               : R$ ",sindicato,
          "\n FGTS (11%)                        : R$ ",FGTS,
          "\n Total de descontos                : R$ ",desconto,
          "\n Salario Liquido                   : R$ ",salario-desconto)

elif salario>1500 and salario<=2500:
    IR = salario*0.1
    INSS = salario*0.1
    desconto = IR+INSS
    print("Salario Bruto: (",vl_hora,"*",hora,")     : R$ ",salario,
          "\n  (-) IR (10%)                      : R$ ",IR,
          "\n  (-) INSS (10%)                   : R$ ",INSS,
          "\n  (-) Sindicato (3%)               : R$ ",sindicato,
          "\n FGTS (11%)                        : R$ ",FGTS,
          "\n Total de descontos                : R$ ",desconto,
          "\n Salario Liquido                   : R$ ",salario-desconto)

else:
    IR = salario*0.2
    INSS = salario*0.1
    desconto = IR+INSS
    print("Salario Bruto: (",vl_hora,"*",hora,")     : R$ ",salario,
          "\n  (-) IR (20%)                      : R$ ",IR,
          "\n  (-) INSS (10%)                   : R$ ",INSS,
          "\n  (-) Sindicato (3%)               : R$ ",sindicato,
          "\n FGTS (11%)                        : R$ ",FGTS,
          "\n Total de descontos                : R$ ",desconto,
          "\n Salario Liquido                   : R$ ",salario-desconto)

    

    
