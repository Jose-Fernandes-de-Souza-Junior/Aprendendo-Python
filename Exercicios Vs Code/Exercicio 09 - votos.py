#9 – Em uma eleição presidencial existem quatro candidatos. 
#Os votos são informados através de códigos. Os dados utilizados para a contagem dos votos obedecem à seguinte codificação: 
#1,2,3,4 = voto para os respectivos candidatos; 
#5 = voto nulo; 
#6 = voto em branco; 

#Elabore um programa que leia o código votado por vários eleitores. Como finalizador da entrada de dados, considere o código zero. 
#Ao final, calcule e escreva: 
#total de votos para cada candidato; 
#- total de votos nulos; 
#- total de votos em branco;
votovalid = 0
cont = 0
votonulo = 0
votobrc = 0
votos = 0
cod=0
cand1 = 0
cand2 = 0
cand3= 0
cand4=0

while True:

	voto = int(input("Digite o numero do candidato: "))

	
	
	
	if voto==1:
		cand1=cand1+1
		
	elif voto==2:
		cand2 = cand2+1
		
	elif voto==3:
		cand3 = cand3+1
		
	elif voto==4:
		cand4 = cand4+1
		
	elif voto==5:
		votonulo = votonulo + 1
		
	elif voto==6:
		votobrc = votobrc + 1
		
	elif voto==0:
		break

	else:
		print("Numero invalido escolha entre os numeros: 1,2,3,4,5 ou 6.")



print("Total de votos candidato 01: ",cand1)
print("Total de votos candidato 02: ",cand2)
print("Total de votos candidato 03: ",cand3)
print("Total de votos candidato 04: ",cand4)
print("Total de votos nulos: ",votonulo)
print("Total de votos em branco: ",votobrc)










