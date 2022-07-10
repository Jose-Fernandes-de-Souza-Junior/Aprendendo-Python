#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade 
# da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calcula

mediaj = 0
jovem = 0
adulto = 0
idoso = 0
somaj=0
somad = 0
somai = 0

for idade in range (0,10):
        idade = float(input("Digite sua idade: "))    

    
        if idade>0 and idade<=25:
            somaj+=idade
            jovem+=1
        
        elif idade>=26 and idade<=60:
            somad+=idade
            adulto+=1
        
        
        elif idade>60:
            somai+=idade
            idoso+=1
        


print ('Número de jovens entrevistados: {}'.format(jovem))
media = somaj/jovem
print ("media de idade dos jovens é: ",media )


print("Número de adultos entrevistados: {}".format(adulto))
media = somad/adulto
print ("media de idade dos adultos é: ",media )

print("Número de Idosos entrevistados: {}".format(idoso))
media = somai/idoso
print ("media de idade dos idosos é: ",media)







