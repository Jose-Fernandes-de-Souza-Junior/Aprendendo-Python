# 9 – Em uma eleição presidencial existem quatro candidatos. 
# Os votos são informados através de códigos. Os dados utilizados para a contagem dos votos obedecem 
# à seguinte codificação: 
# 1,2,3,4 = voto para os respectivos candidatos; 
# 5 = voto nulo; 
# 6 = voto em branco; 

# Elabore um programa que leia o código votado por vários eleitores. Como finalizador da entrada de dados, considere o código zero. 
# Ao final, calcule e escreva: 
# total de votos para cada candidato; 
# - total de votos nulos; 
# - total de votos em branco;

from itertools import count


cand1=1
cand2 = 2
cand3= 3
cand4 = 4
vtnulo= 5
vtbranco = 6
totalcand1 = count(cand1)

