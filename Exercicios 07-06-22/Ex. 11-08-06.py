'''11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhe contrataram para desenvolver o programa que calculará os
reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual:

salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado,
informe na tela:

o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

salario = (float (input("Digite o salario do colaborador: R$ ")))

                 
if salario<=280:
    msg = "20%"
    percent = 0.2
    aumento = salario*percent
    reajuste = salario+aumento
    print(
    "Salário antes do reajuste: ",salario, "\n",
    "Percentual de aumento aplicado: ",msg," \n",
    "Valor do aumento: R$ ",aumento,"\n",
    "Novo salário: R$ ",reajuste)

elif salario>280 and salario<=700:
    msg = "15%"
    percent = 0.15
    aumento = salario*percent
    reajuste = salario+aumento
    print(
    "Salário antes do reajuste: ",salario, "\n",
    "Percentual de aumento aplicado: ",msg," \n",
    "Valor do aumento: R$ ",aumento,"\n",
    "Novo salário: R$ ",reajuste)


elif salario>700 and salario<1500:
    msg = "10%"
    percent = 0.10
    aumento = salario*percent
    reajuste = salario+aumento
    print(
    "Salário antes do reajuste: ",salario, "\n",
    "Percentual de aumento aplicado: ",msg," \n",
    "Valor do aumento: R$ ",aumento,"\n",
    "Novo salário: R$ ",reajuste)

else:
    msg = "5%"
    percent = 0.05
    aumento = salario*percent
    reajuste = salario+aumento
    print(
    "Salário antes do reajuste: ",salario, "\n",
    "Percentual de aumento aplicado: ",msg," \n",
    "Valor do aumento: R$ ",aumento,"\n",
    "Novo salário: R$ ",reajuste)
